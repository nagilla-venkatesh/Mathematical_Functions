# Use isfinite() to check for regular numbers or either of the special values inf or nan.

# isfinite() returns false for either of the exceptional cases, and true otherwise.

import math

for f in [0.0, 1.0, math.pi, math.e, math.inf, math.nan]:
    print('{:5.2f} {!s}'.format(f, math.isfinite(f)))

