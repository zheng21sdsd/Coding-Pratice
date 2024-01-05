class Solution:
    def handle_str(self, s):
        import re
        lower_str = s.lower()
        lower_str = re.sub('[^a-zA-Z0-9]', '', lower_str)
        return lower_str

    def isPalindrome(self, s: str) -> bool:

        lower_str = self.handle_str(s)
        if lower_str == lower_str[::-1]:
            return True
        else:
            return False


s = "A man, a plan, a canal: Panama"


print(Solution().isPalindrome(s))
print(s)


# def isPalindrome(self, s: str) -> bool:
        #     s = self.handle_str(s)
        #     print(s)
        #     a = reversed(list(s))
        #     # print(list(a))
        #     # print(list(s))
        #
        #     if list(a) == list(s):
        #         print('是回文')
        #         return True
        #     elif list(a) != list(s):
        #         print(list(a))
        #         print(list(s))
        #         print('不是回文')
        #         return False
        #     else:
        #         print('xsd')