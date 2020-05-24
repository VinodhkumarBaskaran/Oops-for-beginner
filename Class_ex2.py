
class Student:

    def __init__(self,name,age,grade):

        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:

    def __init__ (self,course_name,max_strength):

        self.course_name = course_name
        self.max_strength = max_strength
        self.student_list = []

    def add_student(self,student):

        if len(self.student_list) < self.max_strength:
            if student.grade > 50:
                self.student_list.append(student)
                return True
        return False

    def get_mean_grade(self):
        value =0
        for student in self.student_list:
            value+=student.get_grade()

        return value / len(self.student_list)



s1 = Student('ram',20,15)
s2 = Student('shree',20,45)
s3 = Student('jiji',21,51)

course = Course('ML',2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.student_list)
print(course.get_mean_grade())
