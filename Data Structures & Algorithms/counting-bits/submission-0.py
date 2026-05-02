class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            val = i
            count = 0
            while val:
                count += val&1
                val >>= 1
            result.append(count)
        return result


        