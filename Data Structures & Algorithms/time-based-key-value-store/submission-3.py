class TimeMap:

    def __init__(self):
        self.kvt_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvt_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvt_map:
            return ""
        
        vt_list = self.kvt_map[key]

        l = 0 
        r = len(vt_list) - 1

        while l<=r:
            mid = l//2 + (r+1)//2
            if vt_list[mid][1] == timestamp:
                return vt_list[mid][0]
            elif vt_list[mid][1] < timestamp:
                if mid+1<=r and vt_list[mid+1][1] <= timestamp:
                    l = mid + 1
                else:
                    return vt_list[mid][0]
            else:
                r = mid - 1
        
        return ""

