from collections import deque

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()

# Read input
s = input()
obj = Solution()

for ch in s:
    obj.pushCharacter(ch)
    obj.enqueueCharacter(ch)

is_palindrome = True
for _ in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        is_palindrome = False
        break

print(f"The word, {s}, is a palindrome." if is_palindrome else f"The word, {s}, is not a palindrome.")
