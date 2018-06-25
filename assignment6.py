#Q.1- Take 10 integers from user and print it on screen.

list=[]
for x in range(10):
  x=int(input(""))
  list.append(x)
print(list)


#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.

iter = 6
while iter>0:
    print("positive elements")


#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

square = [1,3,7,12]
sq=[]
for x in square:
    sq.append(x**2)
print(square)
print(sq)

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately

a=[0.2,1,"anki","shokeen",0.02,11]
x=[]
y=[]
z=[]
for ele in a:
    if(type(ele)==int):
        x.append(ele)
    elif(type(ele)==str):
        y.append(ele)
    elif(type(ele)==float):
        z.append(ele)
print(x)
print(y)
print(z)


#Q.5- Using range(1,101), make a list containing even and odd numbers.

x=[]
y=[]
for ele in range(1,101):
    if(ele%2==0):
        x.append(ele)
    else:
        y.append(ele)
print("List of even numbers :",x)
print("List of odd numbers :",y)


#Q.6- Print the following patterns: 
*
**
***
****

i = 1
while i<=4:
  print ("*"*i)
  i = i+1


#Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop.

x={'beautiful':'pretty','one':1,'three':3,'five':5}
for a,b in x.items():
    print(a,b)


#Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

list1=[]
s=int(input("Enter the size of list :"))
for x in range(s):
    y=int(input("Enter value :"))
    list1.append(y)
d=int(input("Enter the element to be deleted :"))
for x in list1:
    if x==d:
        list1.remove(x)
    else:
        print("Element not in the list")
        print("The list is: ",list1)

    
