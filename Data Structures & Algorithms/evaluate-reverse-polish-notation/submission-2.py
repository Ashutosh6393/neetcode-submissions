class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for n in tokens:
            if n == "+":
                first = st.pop()
                second = st.pop()
                result = int(first) + int(second)
                st.append(result)
            elif n == "-":
                first = st.pop()
                second = st.pop()
                result = int(second) - int(first)
                st.append(result)
            elif n == "*":
                first = st.pop()
                second = st.pop()
                result = int(first) * int(second)
                st.append(result)
            elif n == "/":
                first = st.pop()
                second = st.pop()
                result = int(second) / int(first)
                st.append(result)
            else: 
                st.append(n)

        return int(st[-1])
        