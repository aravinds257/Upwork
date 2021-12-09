class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary


John = Employee("John", 5000.50)
Maria = Employee("Maria", 4090.50)

print(John < Maria)
print(Maria < John)

class Student():
    university="ABC university"
    def __init__(self, name,  sid):
        self.name=name
        self.sid=sid

    def displayName(self):
        print(self.name)


    def displayGrade(self):
        pass



class Grade(Student):
    def __init__(self, name, studentId, courseGrade):
        self.name = name
        self.studentId = studentId
        self.courseGrade = courseGrade

    def displayGrade(self):
        grade = self.courseGrade
        if(grade <= 59.44 ):
            return 'F'
        elif(grade <=69.44 ):
            return 'D'
        elif(grade <= 79.44):
            return 'C'
        elif(grade <= 89.44):
            return 'B'
        elif(grade > 89.44 ):
            return 'A'

s1 = Grade("Tom", "s1",75.3 )
print(s1.displayGrade())

