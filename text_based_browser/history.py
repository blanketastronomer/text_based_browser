from collections import deque


class History(deque):
    def empty(self) -> bool:
        return len(self) == 0
