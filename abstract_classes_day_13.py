class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print(f"Name: {self.lastName}, {self.firstName}")
        print(f"ID: {self.idNumber}")


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90:
            return 'O'
        elif avg >= 80:
            return 'E'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'P'
        elif avg >= 40:
            return 'D'
        else:
            return 'T'


firstName, lastName, idNumber = input().split()
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNumber, scores)
s.printPerson()
print(f"Grade: {s.calculate()}")
