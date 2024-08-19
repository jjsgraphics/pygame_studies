# 

class Dog:

  #def __init__(self):   # runs whenever a dog instance is created 
  #  pass
  
  def __init__(self, name, age):   # whenever a dog instance is created 
    self.name = name
    self.age = age

  def add_one(self, x):   # we have to always use self when creating methods as the class will always invisibly get passed first 
    return x + 1

  def bark(self):
    print("bark")

  def get_name(self):
    return self.name
  
  def get_age(self):
    return self.age
  
  def set_age(self, age):
    self.age = age

d = Dog("Tim", 1) # creates d as an instance of the class dog
d2 = Dog("Bill", 2)

print(type(d)) # outputs: <class '__main__.Dog'>     because it is an object of the class dog defined in the main module

d.bark()
print(d.add_one(5))
print(d.get_name())
print(d2.get_age())
d2.set_age(67)
print(d2.get_age())