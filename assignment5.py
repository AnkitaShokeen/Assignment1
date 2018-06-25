#Q.1- Take an input year from user and decide whether it is a leap year or not.

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
  print("The year is leap year")
else:
  print("Not a leap year")


#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle. 

x=int(input("Enter the length :"))
y=int(input("Enter the breadth :"))
if (x==y):
  print("This is a Square")
elif(x!=y):
  print("This is a Rectangle")

  
#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

x=int(input("Enter the age of first person :"))
y=int(input("Enter the age of second person :"))
z=int(input("Enter the age of third person :"))
if ((x>y) and (x>z)):
  print("First person is the oldest")
else:
  print("First person is youngest")
if((y>x) and (y>z)):
  print("Second person is oldest")
elif(y<x and y<z):
  print("Second person is youngest")
if((z>x) and (z>y)):
  print("Third person is oldest")
elif(z<x and z<y):
  print("Third person is youngest")


#Q.4- Write an if statement to lets competitor know which of these prises they won.

points=int(input("Enter points: "))
if(points>200):
   print("Points cannot be more than 200")

elif(points>=1 and points<=50):
   print("Sorry! No prize this time.")

elif(points>=51 and points<=150):
   print("Congratulations! You won a Wooden Dog!")

elif(points>=151 and points<=180):
   print("Congratulations! You won a Book!")

else:
   print("Congratulations! You won a Chocolates!")


#**Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

print ("Enter quantity")
quantity = int(input())
if (quantity*100 > 1000):
  print ("Cost is",((quantity*100)-(.1*quantity*100)))
else:
  print ("Cost is",quantity*100)
