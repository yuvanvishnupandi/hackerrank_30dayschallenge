class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError("n and p should be non-negative")
        return n ** p

calc = Calculator()
for _ in range(int(input())):
    n, p = map(int, input().split())
    try:
        print(calc.power(n, p))
    except Exception as e:
        print(e)
