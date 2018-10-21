# Floating point calculations can result in two types of exceptional values. INF (“infinity”) appears when the double used to hold a floating point value overflows from a value with a large absolute value.

import math

print('{:^3}  {:6}  {:6}  {:6}'.format('e', 'x', 'x**2', 'isinf'))
print('{:-^3}  {:-^6}  {:-^6}  {:-^6}'.format('', '', '', ''))

for e in range(0, 201, 20):
    x = 10.0 ** e
    y = x*x
    print('{:3d}  {!s:6}  {!s:6}  {!s:6}'.format(e, x, y, math.isinf(y)))