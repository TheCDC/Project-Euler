test x = mod x 3 == 0 || mod x 5 == 0
solve = sum [x | x <- [1..1000], test x]