class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '\\\\'
        elif len(strs) == 1 and '' in strs:
            return ""
        new_str = ';'.join(strs)
        lst = []
        l = len(new_str)
        for i in range(l):
            ltr = new_str[i]
            lst.append(ltr.lower() if ltr.isupper() else ltr.upper())
        return ''.join(lst)
    def decode(self, s: str) -> List[str]:
        if s == '\\\\':
            return []
        elif s == "":
            return [""]
        l = len(s)
        lst = []
        for ltr in s:
            lst.append(ltr.lower() if ltr.isupper() else ltr.upper())
        tmp = ''.join(lst)
        op_lst = tmp.split(';')

        return op_lst

            