class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for t in tokens:
            match t:
                case '+':
                    n = numStack.pop()
                    numStack[-1] += n
                case '-':
                    n = numStack.pop()
                    numStack[-1] -= n
                case '*':
                    n = numStack.pop()
                    numStack[-1] *= n
                case '/':
                    n = numStack.pop()
                    numStack[-1] = int(numStack[-1] / n)
                case _:
                    numStack.append(int(t))
            print(numStack)
        return numStack.pop()
        