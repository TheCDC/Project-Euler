module Common where
    
fibgo :: (Eq t, Num t, Num b) => t -> (b, b) -> b
fibgo 0 (a,b) = a
fibgo 1 (a,b) = b
fibgo n (a,b) = fibgo (n-1) (b,a+b)

fib :: (Eq t, Num t, Num b) => t -> b
fib n = fibgo n (0,1)