class Person:
    def __init__(self, name, age,department):
        self.name = name
        self.age = age
        self.department = department

    def get_name(self):
        return self.name


class Student(Person):

    def __init__(self, name="", age=0, department="", id=0, GPA=0.0):
        Person.__init__(self, name=name,age=age,department=department)
        self.id = id
        self.GPA = GPA
        self.advisor = Professor()

    def reg_advisor(self, prof):
        self.advisor = prof

    def print_student_info(self):
        print("제 이름은 {}, 나이는 {}, 학과는 {}, 지도교수님은 {} 입니다".format(self.get_name(), self.age, self.department, self.advisor.get_name()))

class Professor(Person):
    def __init__(self, name="", age=0, department="", position="", laboratory=""):
        Person.__init__(self, name=name, age=age, department=department)
        self.position = position
        self.laboratory = laboratory
        self.myStd = []

    def reg_student(self, std):
        self.myStd.append(std)

    def print_professor_info(self):
        print("제 이름은 {}, 나이는 {}, 학과는 {}, 지도학생은 {}입니다".format(self.get_name(), self.age, self.department, [self.myStd[i].get_name() for i in range(len(self.myStd))]))

# # test case
# stu1 = Student('Kim', 30, 'Computer', 20001234, 4.5)
# stu2 = Student('Lee', 22, 'Computer', 20103333, 0.5)
# prof1 = Professor('Koo', 50, 'Computer', 'Full', 'RR')
#
# stu1.reg_advisor(prof1)
# stu2.reg_advisor(prof1)
# prof1.reg_student(stu1)
# prof1.reg_student(stu2)
#
# stu1.print_student_info()
# stu2.print_student_info()
# prof1.print_professor_info()