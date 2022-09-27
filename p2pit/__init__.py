# This file exists because if you're in the dir above,
# and do `import p2pit` then it'll load this dir as an
# implicit package, which isn't what we want.

# what was that about explicit being better than implicit?

from .p2pit import *  # noqa
