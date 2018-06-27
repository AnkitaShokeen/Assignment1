#Q1.Create a threading process such that it sleeps for 5 seconds and then prints out a message.

import time
import threading

def anki():
   print("Sleeps for 5 Seconds")
   time.sleep(5)
   print("Hello Ankita :) ")

threading.Thread(target=anki).start()


#Q2.Make a thread that prints numbers from 1-10, waits for 1 sec in between. 

import time
import threading

def anki():
   for x in range(1,11):
      print(x)
      time.sleep(1)

threading.Thread(target=anki).start()


#Q3.Make a list that has 5 elements.
#Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec 

import time
import threading

list=[1,2,3,4,5]

def anki():
   delay=2
   for x in list:
      print(x)
      time.sleep(delay)
      delay+=2

threading.Thread(target=anki).start()


#Q4.Call factorial function using thread.


import time
import threading
def fact(n,d):
    f=1
    for i in range(2,n+1):
       f*=i
    time.sleep(d)
    print("Factorial of %d is :%d "%(n,f))

n=int(input("Enter number: "))
threading.Thread(target=fact,args=(n,2)).start()

