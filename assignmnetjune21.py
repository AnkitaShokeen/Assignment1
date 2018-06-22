QUESTION:1 What is Time Tuple

Ans: We represent time in a way that’s easy for us to understand. However, Python stores it in tuples. These python tuples are made of nine numbers.

Index	Field	Domain of Values
0	Year (4 digits)	Ex.- 1995
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60/61 are leap seconds)
6	Day of Week	0 to 6 (Monday to Sunday)
7	Day of Year	1 to 366 (Julian day)
8	DST	-1,0,1
Leap seconds are added to make up to Earth’s slowing rotation. When DST is 0, it isn’t applied. When it’s 1, it is applied. However, when it is -1, it is up to the library to determine that.
This tuple has an equivalent struct_time structure.


QUESTION:2 WAP To Get Formatted Time
import datetime
x=datetime.datetime.now()
print(x)


QUESTION:3 Extract Month from the Time.
import datetime
x=datetime.datetime.now()
print(x.strftime("%B"))


QUESTION:4 Extract Day from the Time.
import datetime
x=datetime.datetime.now()
print(x.strftime("%A"))


QUESTION:5 Extract date (ex : 11 in 11/01/2021) from the time.
import datetime
x=datetime.datetime.now()
print(x.strftime("%d"))


QUESTION:6 WAP Time Using Local Time
import time
localtime = time.localtime(time.time())
print("local current time:", localtime)


QUESTION:7 Find the Factorial of a Number
import math
x=int(input("factorial of"))
print("factorial is",math.factorial(x))

QUESTION:8 Find the GCD of a number input by user using math package functions.
import math
a=10
b=5
print(math.gcd(a,b))

QUESTION:9 Use OS package and do the following tasks:
1. Get current working directory.
2. Get the user environment.
import os
print(os.getcwd())
import os
print(os.environ)
