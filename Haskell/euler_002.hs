import Common

gengo :: (Num t1, Num a, Eq t1) => t1 -> [a] -> [a]
gengo n s = if fib n > 4000000
    then []
    else gengo (n+1)   s ++ [fib n] 

solve = sum [n | n<- gengo 0 [], even n]
