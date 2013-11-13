compose(f, g, x)(y) = f(g(y), x)
mcompose(f, g, x)(y) = f(*g(y), x)
