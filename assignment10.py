#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

NewCircle = Circle(9)
print(NewCircle.area())
print(NewCircle.perimeter())


#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
    
class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def display(self):
        print("The name of the student is %s"%(self.name))
    def display2(self):
        print("The Roll number is %d"%(self.roll_number))

ankita=Student("ankita" , 14)
print(ankita.name,ankita.roll_number)
ankita.display()
ankita.display2()


#Q.3- Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temperature():
    def __init__(self,c, f):
        self.celsius = c
        self.fahrenheit = f

    def convertFahrenheit(self):
        return(self.celsius*1.8+32)

    def convertCelsius(self):
        return(self.fahrenheit-32)*(5/9)

x = Temperature(18,54)
print("Fahrenheit from Celsius:", x.convertFahrenheit())
print("Celsius from Fahrenheit:", x.convertCelsius())
    
    

#**Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 
#1. Display-Display the details.
#2. Update- Update the movie details.
    
class MovieDetails:
    def __init__(self,mn,an,yor,r):
        self.moviename=mn
        self.artistsname=an
        self.yearofrelease=yor
        self.ratings=r
    def display(self):
        print("The name of the movie is %s the artistname is %s Release in %d with ratings of %d"%(self.moviename,self.artistsname,self.yearofrelease,self.ratings))
    def update(self,i):
        self.ratings+=i
Movie=MovieDetails("fast and furious","Paul Walker",2015,5)
Movie.display()
Movie.update(1)
Movie.display()


#Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
#1. Display expenditure and savings 
#2. Calculate total salary
#3. Display salary

class Expenditure:
    def __init__(self,e,s):
        self.expenditure=e
        self.savings=s
    def display(self):
        print("The expenditure is %d and the savings is %d"%(self.expenditure,self.savings))
    def totalsalary(self):
        total=self.expenditure + self.savings
        self.total=total
        print("the total salary is %d"%(self.total))
Salary=Expenditure(1000,3500)
Salary.display()
Salary.totalsalary()
