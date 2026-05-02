class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        unique = set(numbers)
        for i in range(len(numbers)):
            if target-numbers[i] in unique:
                for j in range(i+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        return [i+1, j+1]
