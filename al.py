# MuLTIPLY(x,y,n):
#     import math
#     if n = 1 then
#         return x*y
#     else:
#         m = n/2###四舍五入
#         a = int(x/power(2,m))
#         b = int(x mod power(2,m))
#         c = int(y/power(2,m))
#         d = int(y mod power(2,m))
#         e = MuLTIPLY(a,c,m)
#         f = MuLTIPLY(b,d,m)
#         g = MuLTIPLY(b,c,m)
#         h = MuLTIPLY(a,d,m)
#         return power(2,power(2,m))*e+power(2,m)*(g+h)+f