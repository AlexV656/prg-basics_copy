# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade = 10

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.grade = 101

    student2.name = "Olivia"
    student2.age = 21
    student2.grade = 25

    student3.name = 'LIdia'
    student3.age = 100
    student3.grade = 10000
    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.grade}, grade')
    print(f'{student2.name}, {student2.age} years old, {student2.grade}, grade')
    print(f'{student3.name}, {student3.age} years old, {student3.grade} grade')

if __name__ == "__main__":
    main()