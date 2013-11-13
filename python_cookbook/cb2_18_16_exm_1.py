# Show failure of the associative law
u, v, w = F(11111113), F(-11111111), F(7.51111111)
assert (u+v)+w == 9.5111111
assert u+(v+w) == 10
# Show failure of the commutative law for addition
assert u+v+w != v+w+u
# Show failure of the distributive law
u, v, w = F(20000), F(-6), F(6.0000003)
assert u*v == -120000
assert u*w == 120000.01
assert v+w == .0000003
assert (u*v) + (u*w) == .01
assert u * (v+w) == .006
