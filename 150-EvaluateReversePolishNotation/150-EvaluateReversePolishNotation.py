# Last updated: 8/15/2026, 3:05:48 PM
class Solution:
    def evalRPN(self,tokens,):
        stack=[]
        for token in tokens:
            if token not in ["+","-","*","/"]:
                stack.append(int(token))
            else:
                b=stack.pop()
                a=stack.pop()
                if token == "+":
                    result = a+b
                elif token == "-":
                    result = a-b
                elif token == "*":
                    result = a*b
                elif token == "/":
                    result = a/b
                stack.append(int(result))
        return stack[0]
        