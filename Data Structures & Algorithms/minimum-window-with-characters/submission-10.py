class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_len = len(t)
        s_len = len(s)

        if s_len<t_len:
            return ""

        t_rep = defaultdict(int)
        for c in t:
            t_rep[c] += 1

        t_unique_chars = len(t_rep)

        sub_rep = defaultdict(int)
        included = 0

        res = s
        is_present = False

        r = 0
        for l in range(s_len):
            # print("==>", s[l:r+1], included)
            # print(sub_rep, t_rep)
            while r<s_len and included!=t_unique_chars:
                sub_rep[s[r]] += 1
                if sub_rep[s[r]] == t_rep[s[r]]:
                    included += 1
                r+=1

            if included==t_unique_chars and len(res)>r-l-1:
                is_present = True
                res = s[l:r]

            sub_rep[s[l]] -= 1
            if sub_rep[s[l]] < t_rep[s[l]]:
                included -= 1

        return res if is_present else ""
