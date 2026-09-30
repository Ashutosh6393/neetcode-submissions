class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest = strs[0]
        id = 0
        for index, st in enumerate(strs):
            if len(st) < len(shortest):
                shortest = st
                id = index
        
        
        for st in strs:
            while not(st.startswith(shortest)):
                shortest = shortest[0:len(shortest)-1]
                
            else:
                continue

        return shortest








        