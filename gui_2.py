#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

from tkinter import *

root = Tk()
root.geometry("100x100")
root = Frame()
root.pack()

d = {'Double click on names':'on names',
   'John':8588033135,
   'Tom': 999008892,
   'Kim': 9212864711,
   'Shrey':8368750600,
   'Roy' :9999992222,
   'Stify':8989453718,
   'Tuffy': 7654567823,
   'Ron' : 7612309351}
l1L = Label(root, text="Name")
l1L.pack()
l2L = Label(root, text="Phone Number")
l2L.pack()


def fun(event):
    label = list.get(ACTIVE)
    print(label)
    phone = d.get(label)
    l1L.config(text=label)
    l2L.config(text=phone)


list = Listbox(root)
sb = Scrollbar(root)
sb.config(command=list.yview)
list.config(yscrollcommand=sb.set)
sb.pack(side=RIGHT, fill=Y)
list.pack(side=LEFT, expand=YES, fill=BOTH)

list.bind('<Double-1>', fun)

for k, v in d.items():
    list.insert('end', k)
root.mainloop()


***************************************************************************************************************************************************************************************************


#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.

from tkinter import *

root = Tk()
dictt = {}
root.geometry("250x300")
keyL = Label(root, text="key")
keyL.pack()
e1E = Entry(root)
e1E.pack()
valueL = Label(root, text="value")
valueL.pack()
valueE = Entry(root)
valueE.pack()
l1L = Label(root)
l1L.pack()
l2L = Label(root)
l2L.pack()

def show():
    l1L.configure(text=e1E.get())
    l2L.configure(text=valueE.get())

def get():
    root = Tk()
    root.geometry("250x300")
    k = e1E.get()
    v = valueE.get()
    lab = Label(root)
    lab.pack()
    dictt.update({k: v})
    lab.configure(text=dictt)
    buttonB = Button(root, text="exit", font="Times 18", command=root.destroy)
    buttonB.pack(side=BOTTOM)
    r.mainloop()

dB = Button(root, text="dictionary", command=show, font="none 15")
dB.pack()
addB = Button(root, text="add", command=get, font="none 15")
addB.pack()
exitB = Button(root, text="exit", font="none 15", command=root.destroy)
exitB.pack(side=BOTTOM)
root.mainloop()


*******************************************************************************************************************************************************************************


#Extra Ques(Horizontal bar)

from tkinter import *
root = Tk()
root.title('macbook')
root.geometry('100x100')

sb = Scrollbar(root,orient=HORIZONTAL)
sb.pack(side=BOTTOM,fill=X)


l1L = Listbox(root, xscrollcommand = sb.set )
s=''
for ele in range(100):
    s=s+'hi'+str(ele)+''

l1L.insert(END,s)

l1L.pack( side = LEFT, fill = BOTH )
sb.config( command = l1L.xview )

root.mainloop()
