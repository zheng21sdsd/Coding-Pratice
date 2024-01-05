class Solution(object):

    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            if n == 0:
                return 1
            if n == 1:
                return x
            else:
                return x * self.myPow(x, n - 1)
        else:
            return 1 / x * self.myPow(x, n + 1)

print(Solution().myPow(x=2.00000, n=10))
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n > 0:
#             if n == 1:
#                 return x
#             y = n // 2
#             m = n % 2
#             return Solution().myPow(x, y) * Solution().myPow(x, y) if m == 0 else Solution().myPow(x,
#                                                                                                    y) * Solution().myPow(
#                 x, y) * Solution().myPow(x, m)
#         else:
#             if n == 1:
#                 return 1 / x
#             if n == 0:
#                 return 0
#
#             y = n // 2
#             m = n % 2
#             return Solution().(1 / x, y) * Solution().(1 / x, y) if m == 0 else Solution().(1 / x, y) * Solution().(
#                 1 / x, y) * Solution().(1 / x, m)
#
#
# print(Solution().myPow(x=2.00000, n=10))