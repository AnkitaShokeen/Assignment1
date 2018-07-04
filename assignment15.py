#Q.1- Extract the user id, domain name and suffix from the following email addresses. 
'''emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
   desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]'''

import re

emails = ["zuck26@facebook.com","page33@google.com","jeff42@amazon.com"]

desired_output = []
for ele in emails:
    s = (re.split('[@.]',ele))
    desired_output.append(s)

print(desired_output)


#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."

import re

sen = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."

words = re.findall("[bB]\w+", sen)

print(words)


#Q.3- Split the following irregular sentence into words 
'''sentence = "A, very very; irregular_sentence"
   desired_output = "A very very irregular sentence'''


import re
sen = "A, very very; irregular_sentence"
desired_output = re.sub('[_\W+]',' ',sen)

print(desired_output)


#OPTIONAL QUESTION

#Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' 
#desired_output = 'Good advice What I would do differently if I was learning to code today'

import re

x = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

print(' '.join(re.sub("(@[\w]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|RT|cc"," ",x).split()))

