# Inheritance 

class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(f"I am {self.name} and I am {self.age} years old")

  def speak(self):
    print("idk what i am")

class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age) # sets up the sub class using the init from the parent class
    self.color = color

  def speak(self):
    print("meow")

  def get_color(self):
    return self.color

class Dog(Pet):
  def speak(self):
    print("woof")

p = Pet("Tim", 19)
p.show()
c = Cat("JeRRY", 10, "red")
c.show()
c.speak()
p.speak()
print(c.get_color())