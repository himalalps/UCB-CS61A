# Call expressions
from math import pi
from operator import add, mul
max(2, 3)
min(1, -2, 3, -4, 5)
pow(100, 2)
pow(2, 100)

add(2, 3)
mul(2, add(1, 2))


# Print
-2
print(-2)
print(1, 2, 3)
x = print(-2)
x
print(x)

None
1
'hi'
abs

print(None)
print(1, 2, 3)
print(None, None)
print(print(1), print(2))


# Assignment
r = 10
2 * pi * r
area = pi * r * r
r = 20
area


def area():
    return pi * r * r


area()
r = 20
area()
r = 100
area()
