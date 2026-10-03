class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        m = 0 

        st = ""

        for i in s: 
            if i not in st:
                st += i
                m = max(m , len(st))
            else:
                x = st.find(i)
                st = st[x+1: len(st)]
                st += i
        

        return m