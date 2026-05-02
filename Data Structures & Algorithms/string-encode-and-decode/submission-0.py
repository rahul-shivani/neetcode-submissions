class Solution:

    def encode(self, strs: List[str]) -> str:
        self.idx_to_word = {}
        encoded_str = ''

        for i in range(len(strs)):
            self.idx_to_word[i] = strs[i]
            encoded_str += str(i) + ' '
            i+=1
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        s = s.split(' ')[:-1]
        s = [self.idx_to_word[int(i)] for i in s]
        return s

