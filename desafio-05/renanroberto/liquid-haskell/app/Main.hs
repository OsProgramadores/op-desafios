{-# language OverloadedStrings, DeriveGeneric #-}

module Main where

import System.Environment (getArgs)
import System.Directory (doesFileExist)
import GHC.Generics (Generic)
import Numeric (showFFloat)

import Control.Parallel.Strategies (using, rdeepseq, parList)
import Control.Monad.Except
  ( ExceptT
  , runExceptT
  , catchError
  , lift
  , throwError
  )

import Data.Text (Text, unpack)
import Data.List (intercalate, foldl')
import Data.Maybe (catMaybes)
import Data.Function ((&))
import Data.Functor ((<&>))
import Data.Bifunctor (first)
import Data.Aeson
  ( ToJSON
  , FromJSON
  , toJSON
  , parseJSON
  , genericToJSON
  , genericParseJSON
  , defaultOptions
  , fieldLabelModifier
  )
import Data.JsonStream.Parser
  ( Parser
  , arrayOf
  , parseLazyByteString
  , value
  , (.:)
  )

import qualified Data.ByteString.Lazy as BL
import qualified Data.Map.Strict as M


{-@ type NonEmpty a = {v:[a] | len v > 0} @-}

data ProgramError
  = NoFileProvided
  | FileNotFound FilePath
  | NoEmployeesFound
  | GenericError String
  | NoError

data Funcionario = Funcionario
  { funcionario_id :: Int
  , funcionario_nome :: Text
  , funcionario_sobrenome :: Text
  , funcionario_salario :: Double
  , funcionario_area :: String
  } deriving Generic

instance ToJSON Funcionario where
  toJSON =
    genericToJSON defaultOptions { fieldLabelModifier = drop 12 }

instance FromJSON Funcionario where
  parseJSON =
    genericParseJSON defaultOptions { fieldLabelModifier = drop 12 }


type AreaCode = String
type AreaName = String

type Area = (AreaCode, AreaName)
type Areas = M.Map AreaCode AreaName


showMoney :: Double -> String
showMoney num = showFFloat (Just 2) num ""

avg :: [Double] -> Double
avg [] = 0
avg xs = let size = (fromIntegral . length) xs in
  (foldl' (+) 0 xs) / size

{-@
minsBy :: (a -> a -> Ordering) -> v:[a] -> {u:[a] | len v > 0 => len u > 0}
@-}
minsBy :: (a -> a -> Ordering) -> [a] -> [a]
minsBy ord zs = mins' [] zs
  where mins' xs [] = xs
        mins' [] (y:ys) = mins' [y] ys
        mins' (x:xs) (y:ys) =
          case ord y x of
            LT -> mins' [y] ys
            EQ -> mins' (y:x:xs) ys
            GT -> mins' (x:xs) ys

{-@
maxsBy :: (a -> a -> Ordering) -> v:[a] -> {u:[a] | len v > 0 => len u > 0}
@-}
maxsBy :: (a -> a -> Ordering) -> [a] -> [a]
maxsBy ord zs = maxs' [] zs
  where maxs' xs [] = xs
        maxs' [] (y:ys) = maxs' [y] ys
        maxs' (x:xs) (y:ys) =
          case ord y x of
            LT -> maxs' (x:xs) ys
            EQ -> maxs' (y:x:xs) ys
            GT -> maxs' [y] ys

compareBy :: Ord b => (a -> b) -> a -> a -> Ordering
compareBy f x y = f x `compare` f y

eqBy :: Eq b => (a -> b) -> a -> a -> Bool
eqBy f x y = f x == f y


{-@ groupBy :: _ -> v:[a] -> {u:[[a]] | len v > 0 => len u > 0} @-}
groupBy :: (a -> a -> Bool) -> [a] -> [[a]]
groupBy _ [] = []
groupBy f (x:xs) = group:(groupBy f rest)
  where group = takeWhile (f x) (x:xs)
        rest  = dropWhile (f x) (xs)

{-@ sortBy :: _ -> v:[a] -> {u:[a] | len v == len u} @-}
sortBy :: (a -> a -> Ordering) -> [a] -> [a]
sortBy _ [] = []
sortBy _ [x] = [x]
sortBy f xs = merge f (sortBy f left) (sortBy f right)
  where n     = length xs `div` 2
        left  = take n xs
        right = drop n xs

{-@
merge :: _
-> v:[a]
-> u:[a]
-> {w:[a] | len w == len u + len v} / [len v, len u]
@-}
merge :: (a -> a -> Ordering) -> [a] -> [a] -> [a]
merge _ xs [] = xs
merge _ [] ys = ys
merge f (x:xs) (y:ys) =
  case x `f` y of
    GT -> y:(merge f (x:xs) ys)
    _  -> x:(merge f xs (y:ys))

{-@
aggregateBy :: (Eq b, Ord b) => (a -> b)
-> v:[a]
-> {u:[[a]] | len v > 0 => len u > 0}
@-}
aggregateBy :: (Eq b, Ord b) => (a -> b) -> [a] -> [[a]]
aggregateBy f =
  groupBy (eqBy f) . sortBy (compareBy f)

bimap :: (a -> b) -> (a -> c) -> a -> (b, c)
bimap f g x = (f x, g x)

headflat :: [[a]] -> [a]
headflat [] = []
headflat (l:ls) = if length l > 0
  then head l : headflat ls
  else headflat ls


areaByEmployee :: Areas -> Funcionario -> Maybe AreaName
areaByEmployee areas f = M.lookup (funcionario_area f) areas

areasFromMap :: [M.Map String String] -> Areas
areasFromMap = M.fromList . catMaybes . map areaFromMap

areaFromMap :: M.Map String String -> Maybe (AreaCode, AreaName)
areaFromMap x =
  case sequence [M.lookup "codigo" x, M.lookup "nome" x] of
    Just [code, name] -> Just (code, name)
    _ -> Nothing

employeesToAreas :: Areas -> [Funcionario] -> [AreaName]
employeesToAreas areas =
  catMaybes . map (areaByEmployee areas)

completeName :: Funcionario -> Text
completeName employee =
  funcionario_nome employee <> " " <> funcionario_sobrenome employee


-- Q1. Quem mais recebe e quem menos recebe na empresa
-- e a média salarial da empresa

{-@
globalMax :: v:[Funcionario] -> {u:[Funcionario] | len v > 0 => len u > 0}
@-}
globalMax :: [Funcionario] -> [Funcionario]
globalMax = maxsBy (compareBy funcionario_salario)

{-@
globalMin :: v:[Funcionario] -> {u:[Funcionario] | len v > 0 => len u > 0}
@-}
globalMin :: [Funcionario] -> [Funcionario]
globalMin = minsBy (compareBy funcionario_salario)

globalAvg :: [Funcionario] -> Double
globalAvg = avg . fmap funcionario_salario


printGlobal :: String -> [Funcionario] -> [String]
printGlobal label = fmap (\f -> intercalate "|"
  [ label
  , (unpack . completeName) f
  , (showMoney . funcionario_salario) f
  ])

printGlobalMax :: [Funcionario] -> [String]
printGlobalMax = printGlobal "global_max"

printGlobalMin :: [Funcionario] -> [String]
printGlobalMin = printGlobal "global_min"

printGlobalAvg :: Double -> [String]
printGlobalAvg = pure . ("global_avg|" <>) . showMoney

solveQ1 :: [Funcionario] -> [String]
solveQ1 fs = concat $
  [ printGlobalMax . globalMax
  , printGlobalMin . globalMin
  , printGlobalAvg . globalAvg
  ] <*> pure fs


-- Q2. Quem mais recebe e quem menos recebe em cada área
-- e a média salarial em cada área

byArea :: ([Funcionario] -> a)
           -> Area
           -> [Funcionario]
           -> (AreaName, a)
byArea trans (code, area) fs =
  ( area
  , trans . filter ((== code) . funcionario_area) $ fs
  )

byAreas :: ([Funcionario] -> a)
        -> Areas
        -> [Funcionario]
        -> [(AreaName, a)]
byAreas trans areas fs = M.elems $
  M.mapWithKey (\code area -> byArea trans (code, area) fs) areas

areasMax :: Areas -> [Funcionario] -> [(AreaName, [Funcionario])]
areasMax = byAreas globalMax

areasMin :: Areas -> [Funcionario] -> [(AreaName, [Funcionario])]
areasMin = byAreas globalMin

areasAvg :: Areas -> [Funcionario] -> [(AreaName, Double)]
areasAvg areas fs = fs
  & byAreas globalAvg areas
  & filter ((/= 0) . snd)


printArea :: String -> (AreaName, [Funcionario]) -> [String]
printArea label (area, fs) =
  (\f -> intercalate "|"
    [ label
    , area
    , (unpack . completeName) f
    , (showMoney . funcionario_salario) f
    ]
  ) <$> fs

printAreas :: String -> [(AreaName, [Funcionario])] -> [String]
printAreas label = concat . fmap (printArea label)

printAreaMax :: [(AreaName, [Funcionario])] -> [String]
printAreaMax = printAreas "area_max"

printAreaMin :: [(AreaName, [Funcionario])] -> [String]
printAreaMin = printAreas "area_min"

printAreaAvg :: [(AreaName, Double)] -> [String]
printAreaAvg =
  fmap (\(area, payment) -> intercalate "|"
         [ "area_avg"
         , area
         , showMoney payment
         ])


solveQ2 :: Areas -> [Funcionario] -> [String]
solveQ2 areas fs = concat $
  [ printAreaMax . areasMax areas
  , printAreaMin . areasMin areas
  , printAreaAvg . areasAvg areas
  ] <*> pure fs


-- Q3. Área(s) com o maior e menor número de funcionários

type AreaCount = ([AreaName], Int)


{-@ mostEmployees :: Areas -> NonEmpty [Funcionario] -> AreaCount @-}
mostEmployees :: Areas -> [[Funcionario]] -> AreaCount
mostEmployees areas ls = ls
  & maxsBy (compareBy length)
  & bimap id (length . head)
  & first (employeesToAreas areas . headflat)

{-@ leastEmployees :: Areas -> NonEmpty [Funcionario] -> AreaCount @-}
leastEmployees ::Areas -> [[Funcionario]] -> AreaCount
leastEmployees areas ls = ls
  & minsBy (compareBy length)
  & bimap id (length . head)
  & first (employeesToAreas areas . headflat)

{-@ countEmployees :: Areas -> NonEmpty Funcionario -> _ @-}
countEmployees :: Areas -> [Funcionario] -> (AreaCount, AreaCount)
countEmployees areas fs = fs
  & aggregateBy funcionario_area
  & bimap (leastEmployees areas) (mostEmployees areas)


printEmployees :: String -> AreaCount -> [String]
printEmployees _ ([], _) = []
printEmployees label (areas, len) =
  (\area -> intercalate "|"
    [ label
    , area
    , show len
    ]) <$> areas

printMostEmployees :: AreaCount -> [String]
printMostEmployees = printEmployees "most_employees"

printLeastEmployees :: AreaCount -> [String]
printLeastEmployees = printEmployees "least_employees"

{-@ solveQ3 :: Areas -> NonEmpty Funcionario -> [String] @-}
solveQ3 :: Areas -> [Funcionario] -> [String]
solveQ3 areas fs =
  let
    (least, most) = countEmployees areas fs
  in
    concat $
    [ printMostEmployees most
    , printLeastEmployees least
    ]


-- Q4. Maiores salários para funcionários com o mesmo sobrenome

lastNameMax :: [Funcionario] -> [Funcionario]
lastNameMax fs = fs
  & aggregateBy funcionario_sobrenome
  & filter (\l -> length l > 1)
  <&> maxsBy (compareBy funcionario_salario)
  & concat


printLastNameMax :: [Funcionario] -> [String]
printLastNameMax = fmap (\f -> intercalate "|"
  [ "last_name_max"
  , (unpack . funcionario_sobrenome) f
  , (unpack . completeName) f
  , (showMoney . funcionario_salario) f
  ])

solveQ4 :: [Funcionario] -> [String]
solveQ4 = printLastNameMax . lastNameMax


{-@ solve :: Areas -> NonEmpty Funcionario -> _ @-}
solve :: Areas -> [Funcionario] -> [String]
solve areas fs =
  let values =
        [ solveQ1 fs
        , solveQ2 areas fs
        , solveQ3 areas fs
        , solveQ4 fs
        ]
  in concat (values `using` parList rdeepseq)


run :: ExceptT ProgramError IO ()
run = do
  filepath <- getFilepath `catchError` showError
  fileExist filepath `catchError` showError
  content <- lift $ BL.readFile filepath

  let employeeParser = "funcionarios" .: arrayOf value :: Parser Funcionario
  let areaParser = "areas" .: arrayOf value :: Parser (M.Map String String)

  let employees = parseLazyByteString employeeParser content
  let areasMap = parseLazyByteString areaParser content

  let areas = areasFromMap areasMap

  thereIsEmployees employees `catchError` showError

  if length employees > 0
    then lift . putStr . unlines . solve areas $ employees
    else absurd  "Length was already verified"


getFilepath :: ExceptT ProgramError IO String
getFilepath = do
  args <- lift getArgs
  if length args > 0
    then (return . head) args
    else throwError NoFileProvided

fileExist :: FilePath -> ExceptT ProgramError IO ()
fileExist filepath = do
  exist <- lift $ doesFileExist filepath
  if exist
    then return ()
    else throwError (FileNotFound filepath)

thereIsEmployees :: [Funcionario] -> ExceptT ProgramError IO ()
thereIsEmployees employees = if not (null employees)
  then return ()
  else throwError NoEmployeesFound


showError :: ProgramError -> ExceptT ProgramError IO a
showError NoFileProvided =
  printError "No file provided. Missing arguments"
showError (FileNotFound filepath) =
  printError ("File '" <> filepath <> "' was not found")
showError NoEmployeesFound =
  printError "No employee found"
showError (GenericError err) =
  printError err
showError NoError = throwError NoError

printError :: String -> ExceptT ProgramError IO a
printError err =
  (lift . putStrLn) ("Error: " <> err) >> throwError NoError


-- Should never happen
absurd :: String -> a
absurd _ = undefined

main :: IO ()
main = runExceptT run >> return ()
