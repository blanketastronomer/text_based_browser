from collections import deque
from typing import Any


class History(deque):
    def empty(self) -> bool:
        return len(self) == 0

    def push(self, obj: Any):
        self.append(obj)

    def peek(self):
        return self[len(self) - 1]
