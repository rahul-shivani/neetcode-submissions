class MinStack:

    def __init__(self):
        self._min = []
        self._list = []

    def push(self, val: int) -> None:
        self._list.append(val)
        min_val = val
        if self._min:
            min_val = min(self._min[-1], val)         
        self._min.append(min_val)

    def pop(self) -> None:
        self._list.pop()
        self._min.pop()

    def top(self) -> int:
        return self._list[-1]

    def getMin(self) -> int:
        return self._min[-1]
