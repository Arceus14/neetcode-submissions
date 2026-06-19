import re
class Solution:
    def isPalindrome(self, st: str) -> bool:
        # lst = list(st.replace(' ', ''))
        # for each in lst:
        #     if not each.isalnum():
        #         lst.remove(each)
        
        s = re.sub(r'[^\w]', '', st)
        l = len(s)
        if not l%2 == 0:
            fh = s[:l//2]
            sh = s[l//2 + 1:]
        else:
            fh = s[: l//2]
            sh = s[l//2 :]
        if fh.lower() == sh.lower()[::-1]:
            return True
        else:
            return False
