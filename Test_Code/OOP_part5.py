# static methods - if u are making basic functions which aren't specific to instances (more for good organisation)

class Math:
  
  @staticmethod   # static methods do stuff but don't change anything
  def add5(x):
    return x+5
  
  @staticmethod
  def pr(text):
    print(text)
  
print(Math.add5(5))
Math.pr("u suck")