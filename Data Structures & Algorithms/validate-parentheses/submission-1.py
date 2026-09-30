class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        

        for i in s:
            if not st and (i == ")" or  i == "}" or  i == "]"):
                return False

            if i == "(" or i == "{" or i == "[":
                st.append(i)
            elif i == ")" and st[-1] == "(":
                st.pop()
            elif i == "]" and st[-1] == "[":
                st.pop()
            elif i == "}" and st[-1] == "{":
                st.pop()
            else:
                return False
        
        if st:
            return False
        
        return True
                
        