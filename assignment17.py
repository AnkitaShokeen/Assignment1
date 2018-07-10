#Q1. Write a python program using tkinter interface to write Hello World and an exit button that closes the interface.

from tkinter import *

root = Tk()
root.title('Macbook')
root.geometry('600x600')

hwL = Label(root, text='Hello World', font = 'Times 25 bold underline',bg='lightgreen')
hwL.pack()

exitB  =  Button(root,text='exit',width=25,highlightbackground ='pink',command=root.destroy)
exitB.pack(side=BOTTOM)

root.mainloop()

*******************************************************************************************************************************************************************

#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.

from tkinter import *

def ShowMsg():
    mL=Label(root, text='Have a nice day:)', font = 'Times 25 bold ',bg='green')
    mL.pack()

root = Tk()
root.title('Macbook')
root.geometry('600x600')
#root.configure(background='blue')

hwL = Label(root, text='Hello World', font = 'Times 25 bold underline',bg='lightgreen')
hwL.pack()

buttonB  =  Button(root,text='Press for Msg',width=25,highlightbackground ='pink',command=ShowMsg)
buttonB.pack()
exitB  =  Button(root,text='exit',width=25,command=root.destroy)
exitB.pack(side=BOTTOM)

root.mainloop()

*******************************************************************************************************************************************************************

#Q3. Create a frame using tkinter with any label text and two buttons.
#One to exit and other to change the label to some other text.

from tkinter import *

def ShowMsg():
    l1_L.config( text="Label is Changed", bg='green') #update label using config

root=Tk()
root.title('Frames_')
root.configure(background='pink')
root.geometry('600x600')

frame_1=Frame(root, bg='black')
frame_1.pack(fill=X)

frame_2=Frame(root, bg='red')
frame_2.pack(fill=X,side=LEFT)

frame_3=Frame(root, bg='green')
frame_3.pack(fill=X,side=RIGHT)

l1_L= Label(frame_1,text="This is label 1",bg='red')
l1_L.pack()

buttonB  =  Button(frame_2,text='Press for Msg',width=25,highlightbackground ='orange',command=ShowMsg)
buttonB.pack()
exitB  =  Button(frame_3,text='exit',width=25,highlightbackground ='orange',command=root.destroy)
exitB.pack()

root.mainloop()

#OR

from tkinter import *

def ShowMsg():
    l1_L = Label(frame_1, text="label is changed", bg='green')
    l1_L.grid(row=0,column=0) #using grid by overwriting the new label on the same location but this will hide the previous label not change!

root=Tk()
root.title('Frames_')
root.configure(background='pink')
root.geometry('600x600')

frame_1=Frame(root, bg='black')
frame_1.pack(fill=X)

frame_2=Frame(root, bg='red')
frame_2.pack(fill=X,side=LEFT)

frame_3=Frame(root, bg='green')
frame_3.pack(fill=X,side=RIGHT)

l1_L= Label(frame_1,text="This is label 1",bg='red')
l1_L.grid(row=0,column=0)

buttonB  =  Button(frame_2,text='Press for Msg',width=25,highlightbackground ='orange',command=ShowMsg)
buttonB.pack()
exitB  =  Button(frame_3,text='exit',width=25,highlightbackground ='orange',command=root.destroy)
exitB.pack()

root.mainloop()

***********************************************************************************************************************************************************

#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.

from tkinter import *

def ShowMsg():
    data = userE.get()
    labeL=Label(root,text="Hello Miss " +data,font='Times 18 italic',bg='lightgreen')
    labeL.pack()
root = Tk()
root.title('Ankita_s_Macbook')
root.geometry('600x600')
root.configure(background='blue')

userL = Label(root, text='Please enter your Name : ')
userL.pack()

userE = Entry(root)
userE.pack()

buttonB  =  Button(root,text='Submit',width=25,highlightbackground ='pink',command=ShowMsg)
buttonB.pack()


root.mainloop()




