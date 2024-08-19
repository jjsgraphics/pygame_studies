# class attributes and methods

class Person:
  number_of_ppl = 0
  GRAVITY = -9.8 # put attributes like this inside classes so u can export the whole class without depending on outer code

  def __init__(self, name):
    self.name = name
    Person.number_of_ppl += 1

  @classmethod                        # a function which is used for data stored in the class (e.g n.o. ppl or GRAVITY ) rather than class instances
  def number_of_people(cls):          # for class methods always use cls as the first argument instead of self
    return cls.number_of_people()     
  
  @classmethod
  def add_person(cls):
    cls.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")


# Shows that if an instance of a class doesn't have the attribute, it checks the class for it
print(p1.number_of_ppl)
Person.number_of_ppl = 8
print(p1.number_of_ppl)
print(Person.number_of_ppl)
p1.number_of_ppl = 4
print(p1.number_of_ppl)
print(Person.number_of_ppl)