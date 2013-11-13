qsort [] = []
qsort (x:xs) = qsort elts_lt_x ++ [x] ++ qsort elts_greq_x
                 where
                   elts_lt_x = [y | y <- xs, y < x]
                   elts_greq_x = [y | y <- xs, y >= x]
