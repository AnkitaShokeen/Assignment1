from tkinter import *

#def Add_notes():
#    mL=Label(root, text='Have a nice day:)', font = 'Times 25 bold ',bg='green')
#    mL.pack()

#def List_notes():
# mL=Label(root, text='Have a nice day:)', font = 'Times 25 bold ',bg='green')
#    mL.pack()

#def Search_notes():
# mL=Label(root, text='Have a nice day:)', font = 'Times 25 bold ',bg='green')
#    mL.pack()


root = Tk()
root.title('Note Taking App')
root.geometry('550x500')


AddB  =  Button(root,text='Add New Note>>',width=20,bg='red',highlightbackground ='purple')#,command=Add_notes)
AddB.grid(row=0,column=0,padx=20,pady=17,sticky=W,ipady=2)

ListB  =  Button(root,text='List All Notes',width=20,bg='red',highlightbackground ='purple')#,command=List_notes)
ListB.grid(row=0,column=0,pady=17,padx=250,sticky=W,columnspan=5,ipady=2)

l1L= Label(root,text="Search Notes",font = 'Times 15 bold')
l1L.grid(row=1,column=0,padx=20,pady=5,sticky=W)

search_text=StringVar()
entry1=Entry(root,textvariable=search_text,width=40)
entry1.grid(row=2, column=0,sticky=W,padx=20,ipady=2)

SearchB  =  Button(root,text='Search',width=10,bg='red',highlightbackground ='green')#,command=Search_notes)
SearchB.grid(row=2,column=0,sticky=W,padx=400)

l2L= Label(root,text="--Notes--",font = 'Times 15 bold')
l2L.grid(row=3,column=0,pady=6,sticky=W,padx=200)

List_Box=Listbox(root,height = 15, width = 55)
List_Box.grid(row = 4, column = 0,sticky=W,padx=5)

sb=Scrollbar(root)
sb.grid(row = 4, column = 4, rowspan = 6)

List_Box.configure(yscrollcommand = sb.set)
sb.configure(command = List_Box.yview)


root.mainloop()

