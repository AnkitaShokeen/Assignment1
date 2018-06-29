
#Q1. Name and handle the exception occured in the following program:
a=3
 if a<4:
    a=a/(a-3)
     print(a)

Ans-This is ZeroDivisionError which occurs when number divided by zero. This exception can be handled as:
try:
    a = 3
    if a < 4:
        a = a / (a - 3)
        print(a)

except ZeroDivisionError as e:
    print ("their is an error")
    print(e)


#Q2. Name and handle the exception occurred in the following program:
l=[1,2,3]
print(l[3])

Ans-This is IndexError which occurs when the index is out of range.This exception can be handled as:
try:
  l=[1,2,3]
  print(l[3])

except IndexError as e:
  print("their is an error")
  print(e)


#Q3. What will be the output of the following code:
 Program to depict Raising Exception
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or n

Ans-  An exception
Traceback (most recent call last):
  File "as.py", line 2, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there


#Q4. What will be the output of the following code:
# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

Ans: -5.0
     a/b result in 0


#Q5. Write a program to show and handle following exceptions:
1. Import Error
Ans- try:
  from time import d
  print(d)
except ImportError as e:
  print("their is an error")
  print(e)

2. Value Error
Ans-while True:
    try:
        x=int(input("please enter a number"))
        break
    except ValueError:
        print("oops! that was not a valid number")

3. Index Error
Ans-  try:
  l=[1,2,3]
  print(l[3])



#Q6. Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
#The code must keep taking input till the user enters the appropriate age number(less than 18). 

except IndexError as e:
  print("their is an error")
  print(e)

class Er(Exception):
    def __init__(self):
        super(Exception, self).__init__(self)

    def AgeTooSmallError(self, msg):
        print(msg)

a = True
while a:
    try:
        age = int(input("Enter your age"))
        if age < 18:
            raise Er()

    except Er as e:
        e.AgeTooSmallError("Age is less than 18")

    else:
        a = False





  

  
