class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for n in strs:
            res += str(len(n))
            res += "#"
            res += n
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            start = i
            while s[i] != '#': 
                i += 1
            length = int(s[start:i])

            i = i+1

            res.append(s[i: i+length])

            i += length

        
        return res
            

