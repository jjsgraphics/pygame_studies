# OOP

class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade
    
class Course:
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students
    self.students = []

  def add_student(self, student):
    if len(self.students) >= self.max_students:
      print("max students reached")
      return False
    self.students.append(student)
    return True

  def get_average_grade(self):
    value = 0
    for student in self.students:
      value += student.get_grade()
    avg_grade = value / len(self.students)
    return avg_grade

s1 = Student("adam", 19, 95)
s2 = Student("bill", 19, 75)
s3 = Student("clove", 18, 65)

science = Course("Science", 2)
science.add_student(s1)
science.add_student(s2)
science.add_student(s3)
print(science.get_average_grade())


    