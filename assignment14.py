File saved as xyz.txt
'''“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. 
Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” 
That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. 
“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy. 
They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. 
That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird'''

#Q.1- Write a Python program to read last n lines of a file

def last_lines(name, lines):
    with open(name, 'r') as f:
        data = f.readlines()[-lines:]
        for line in data:
            print(line)

f = open("xyz.txt",'r')
length = len(f.readlines())
n = int(input("Enter number of lines you want to read but it should be less than %d \n"%(length)))
if n > length:
    print("The file does not contain %d lines"%(n))
else:
    last_lines("xyz.txt", n)
f.close()


#Q.2- Write a Python program to count the frequency of words in a file.
with open('xyz.txt' ,'r') as f:
    data = f.readlines()
    words = []
    for line in data:
        words += line.split()

    count_freq = {}
    for w in words:

        count_freq[w] = words.count(w)

    for k ,v in count_freq.items():
        print (k ,":" ,v)


#Q.3- Write a Python program to copy the contents of a file to another file
f1 = open('xyz.txt','r')
f2 = open('copy.txt','w')

l = f1.readlines()
f2.writelines(l)

f1.close()
f2.close()


#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

file1 = open('first.txt', 'r')
file2 = open('second.txt', 'r')
file3 = open('third.txt', 'w')

list1 = []
while 1:
    line1 = file1.readline()
    file3.write(line1)
    print(line1)
    line2 = file2.readline()
    file3.write(line2)
    print(line2)
    if not line1 and not line2:
        break
file1.close()
file2.close()
file3.close()


#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

with open('f1.txt','w') as f:
   for i in range(10):
      n=int(input("Enter number: "))
      f.write("%d "%(n))

with open('f1.txt','r') as f:
   data=f.readlines()

   for num in data:
      x=num.split()
   x.sort()

with open('f2.txt','w') as f:
   for i in x:
      f.write("%s "%(i))
