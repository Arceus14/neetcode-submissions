class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return 'empty'
        enc = '//'
        return enc.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == 'empty':
            return []
        enc = '//'
        return s.split(enc)