
class Difference:
    def __init__(self, elements):
        self.elements = elements
        self.maximumDifference = 0

    def computeDifference(self):
        max_element = max(self.elements)
        min_element = min(self.elements)
        self.maximumDifference = abs(max_element - min_element)

n = int(input())
elements = list(map(int, input().split()))
diff = Difference(elements)
diff.computeDifference()
print(diff.maximumDifference)
