class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        print(bin(result))

        for i in range(0,32):
            if (n & (1 << i)):
                result |=  1 << (31-i)
        
        return result
        