#ques-1 Create a list with user defined inputs.
list=[]
list.append("shirt")
list.append("pant")
list.append("jeans")
list.append("skirt")
print(list)


#ques-2 Add the following list to above created list:
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
clothes_list=["shirt","pant","jeans","skirt"]
print(clothes_list)
web_list=["google","apple","facebook","microsoft","tesla"]
list = clothes_list + web_list
print(list)

or

clothes_list=["shirt","pant","jeans","skirt"]
web_list=["google","apple","facebook","microsoft","tesla"]
clothes_list.extend(web_list)
print(clothes_list)

or
list=[]
list.insert(0,"shirt")
list.insert(1,"pant")
list.insert(2,"jeans")
list.insert(3,"skirt")
list.append("google")
list.append("apple")
list.append("facebook")
list.append("microsoft")
list.append("tesla")
print(list)


#ques-3 Count the number of time an object occurs in a list. 
list=[]
list.append("ankita")
list.append("ankita")
list.append("shokeen")
print(list.count("ankita"))

or

clothes_list=["shirt","skirt","jeans","skirt"]
print(clothes_list.count("skirt"))


#ques-4 Create a list with numbers and sort it in ascending order. 
li=[2,5,3,1,8]
li.sort()
print(li)


#ques-5 Given are two one-dimensional arrays A and B which are sorted in ascending order.
#Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List] 
listA = [2,3,1,5,6]
listB = [4,8,9,10,7]
listC = listA + listB
listC.sort()
print(listC)


#ques-6 Implement a stack and queue using lists.
stack = ["apple","orange","pineapple"]
print(stack)
print(stack.pop(1))
print(stack)


from collections import deque
queue = deque(["red","green","pink"])
print(queue)
print(queue.popleft())
print(queue)


OPTIONAL QUESTION
#ques- Count even and odd numbers in that list.
numbers = [2, 3, 5, 7, 10, 12, 13]
even = 0
odd = 0
for x in numbers:
        if not x % 2:
    	     even+=1
        else:
    	     odd+=1
print("Number of even numbers:",even)
print("Number of odd numbers:",odd)






