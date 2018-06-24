#Q.1- Create a function to calculate the area of a circle by taking radius from user.

x = int(input("Enterthe radius"))
def rad(x):
    pi = 3.14
    area = pi * x * x
    return area

print("Radius of circle is", rad(x))


#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

def Perfect(n):
    sum = 1

    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i

        i += 1
        return (True if sum == n and n != 1 else False)

print("Below are all perfect numbers")
n = 2
for n in range(1000):
    if Perfect(n):
        print(n)


#Q.3- Print multiplication table of 12 using recursion.

def multiply(n, i=1):
    print(n*i)
    if(i == 11):
        return 1
    else:
        multiply(n, i+1)
n=12
multiply(n)


#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(x,y):
    if(y==1):
        return(x)
    if(y!=1):
        return(x*power(x,y-1))
x=int(input("Enter Number: "))
y=int(input("Enter Power: "))
print("Answer is :",power(x,y))


#Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary        

def factorial(n):
    if (n <= 1):
        return 1
    else:
        return (n * factorial(n - 1))

n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
