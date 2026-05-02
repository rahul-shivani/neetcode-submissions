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
                    numStack[-1] /= n
                    if numStack[-1]<0:
                        numStack[-1] = math.ceil(numStack[-1])
                    else:
                        numStack[-1] = math.floor(numStack[-1])
                case _:
                    numStack.append(int(t))
            print(numStack)
        return numStack.pop()
        