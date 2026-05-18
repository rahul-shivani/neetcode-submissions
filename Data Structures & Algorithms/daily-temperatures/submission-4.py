class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        result = [0]*len(temperatures)
        for idx in range(len(temperatures)):
            # print(tempStack)
            t = temperatures[idx]
            while tempStack and t > tempStack[-1][0]:
                result[tempStack[-1][1]] = idx - tempStack[-1][1]
                tempStack.pop()
            tempStack.append((t, idx))
        return result


        
        