from collections import deque


class History(deque):
    """
    Browser history stack.
    """
    def empty(self) -> bool:
        """
        Check if the History stack is empty.
        :return: True if empty, else False
        """
        return len(self) == 0

    def push(self, page: str):
        """
        Push a page onto the stack.

        :param page: Page to push onto the stack
        """
        self.append(page)

    def peek(self):
        """
        Show the element at the top of the stack.

        NOTE: This is different from pop(), which returns the element and removes it from the stack.
        :return: Element at the top of the stack
        """
        return self[len(self) - 1]
