class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for idx in range(len(digits)-1, -1, -1):
            digits[idx] = digits[idx]+carry
            carry = digits[idx]//10
            digits[idx] = digits[idx]%10
            if carry == 0:
                return digits

        return [carry]+digits


        