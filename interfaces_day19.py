from abc import ABC, abstractmethod

class AdvancedArithmetic(ABC):
    @abstractmethod
    def divisorSum(self, n):
        pass

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum(i for i in range(1, n + 1) if n % i == 0)

n = int(input())
my_calculator = Calculator()
print("I implemented: AdvancedArithmetic")
print(my_calculator.divisorSum(n))
