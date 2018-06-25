#Q1.Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
   def animal_attribute(self,name,work):
       print(name," likes to ",work)

class Tiger(Animal):
   def tiger_attribute(self,name,work):
       self.animal_attribute(name,work)

T = Tiger()
T.tiger_attribute("Tiger","Roar")


#Q2.What will be output of following code.
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())


Output - 
A B
A B


#Q3.Create a class Cop. Initialize its name, age , work experience and designation.
#Define methods to add, display and update the following details. Create another class Mission which extends the class Cop.
#Define method add_mission _details.
#Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.

class Cop:
  name=""
  age=int()
  work=""
  experience=int()
  designation=""
  
  def add(self,n,a,w,e,d):
    self.name=n
    self.age=a
    self.work=w
    self.experince=e
    self.designation=d

  def display(self):
    print("Name: ",self.name)
    print("Age: ",self.age) 
    print("Work: ",self.work)
    print("Experince(in months): ",self.experince,"months")
    print("Designation: ",self.designation)
 

class Mission(Cop):
  def add_mission_details(self,m):
      print("Mission: ",m)

m1 = Mission()
m1.add("M.P. Grover",32,"Special Branch",30,"ASI")
m1.display()
m1.add_mission_details("Dealing with the terrorism")


#Q4. Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.

class Shape:
   length=int()
   breadth=int()
   def area(self,l,b):
       self.length=l
       self.breadth=b
       return self.length*self.breadth

class Rectangle(Shape):
   def display_area(self):
      l=int(input("Enter length of rectangle:"))
      b=int(input("Enter breadth of rectangle:"))
      print("Area of Rectangle: ",self.area(l,b))

r= Rectangle()
r.display_area()

class Square(Shape):
   def display_area(self):
      a=int(input("Enter side length of square:"))
      print("Area of Rectangle:",self.area(a,a))

s= Square()
s.display_area()
