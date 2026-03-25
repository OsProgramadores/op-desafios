module Desafio02 where

import Data.List

calculate_primes m = ps where ps = map head $ takeWhile (not.null) $ scanl (\\) [2..m] [[p, p+p..m] | p <- ps]

main = calculate_primes 10000