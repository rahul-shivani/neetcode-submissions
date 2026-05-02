class TimeMap:

    def __init__(self):
        self._map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._map:
            self._map[key] = {
                "values": [value],
                "ts": [timestamp]
            }
        else:
            self._map[key]["values"].append(value)
            self._map[key]["ts"].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map:
            return ""

        _len = len(self._map[key]["ts"])

        l = 0
        r = _len-1

        while l<=r:
            m = (l+1)//2 + r//2
            if self._map[key]["ts"][m]==timestamp:
                return self._map[key]["values"][m]
            elif self._map[key]["ts"][m]>timestamp:
                r = m-1
            else:
                if m+1<_len and self._map[key]["ts"][m+1]<=timestamp:
                    l = m+1
                else:
                    return self._map[key]["values"][m]
        
        return ""





