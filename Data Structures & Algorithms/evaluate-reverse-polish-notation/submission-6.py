
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        helper_arr = []
        for token in tokens:
            if token == "+":
                x = helper_arr.pop()
                y = helper_arr.pop()
                helper_arr.append(y + x)
            elif token == "-":
                x = helper_arr.pop()
                y = helper_arr.pop()
                helper_arr.append(y - x)
            elif token == "*":
                x = helper_arr.pop()
                y = helper_arr.pop()
                helper_arr.append(y * x)
            elif token == "/":
                x = helper_arr.pop()
                y = helper_arr.pop()
                # Truncate toward zero
                helper_arr.append(int(y / x))
            else:
                helper_arr.append(int(token))

        return helper_arr[-1]


        