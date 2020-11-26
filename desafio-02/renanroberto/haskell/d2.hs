module Main where


-- Use Sieve of Eratosthenes to generate the primes
sieve :: [Int] -> [Int]
sieve [] = []
sieve (x:xs) = x : (sieve rest)
  where rest = [n | n <- xs, n `mod` x /= 0]

main :: IO ()
main = do
  traverse print (sieve [2 .. 10000])
  return ()
