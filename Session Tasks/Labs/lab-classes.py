class Student:
    
    def __init__(self, name: str, age: int, classroom: str) -> None:
        self.name = name
        self.age = age
        self.classroom = classroom
        
    def calculateAverageScore(self, score1: float, score2: float, score3: float) -> float:
        average = (score1 + score2 + score3) / 3
        return round(average, 2)
        
student_1 = Student(name="Alice", age=20, classroom="Chemistry")
student_2 = Student(name="Bob", age=22, classroom="Drama")
student_3 = Student(name="Charlie", age=20, classroom="Computer Science")

avg_score = student_3.calculateAverageScore(85.5, 90.0, 55.0)

print(f"{student_3.name} is {student_3.age} years old. And is scoring {avg_score} on average")