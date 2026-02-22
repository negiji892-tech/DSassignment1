"""
ETCCDS202 - Data Structures
Unit 1 Experiment 1: Stack ADT Implementation

Time Complexity:
Push: O(1)
Pop: O(1)
Peek: O(1)
"""

class Stack:
    def __init__(self):
        self.items = []

    # Push element
    def push(self, item):
        self.items.append(item)
        print(f"{item} pushed into stack.")

    # Pop element
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! No element to pop.")
            return None
        return self.items.pop()

    # Peek top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.items[-1]

    # Check empty
    def is_empty(self):
        return len(self.items) == 0

    # Size
    def size(self):
        return len(self.items)


# -------- Main Program --------
if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    print("Top element:", s.peek())
    print("Popped element:", s.pop())
    print("Stack size:", s.size())