import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

from tkinter import *
from tkinter import ttk


def selected(event):

    mylabel = Label(my_frame1,text=repr(countries[handList.get(handList.curselection())])).pack()

countries = {
        "1": 'Antigua and Barbuda', 
        "2": 'Bahamas',
        "3": 'Barbados',
        "4": ['Belize', 'Canada'],
        "5": ['Costa Rica ', 'Cuba', 'Dominica', 'Dominican Republic'],
        "6": ['El Salvador ','Grenada', 'Guatemala ', 'Haiti', 'Honduras'], 
        "7": ['Jamaica', 'Mexico','Nicaragua', 'Saint Kitts and Nevis'],
        "8": ['Panama ', 'Saint Lucia','Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States of America']
}

root = Tk()
root.geometry("1500x750")
# e = tk.Entry(root,width=35,borderwidth=5)
#e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook,width=500,height=500,bg="blue")
my_frame2 = Frame(my_notebook,width=500,height=500,bg="red")

my_frame1.pack(fill="both",expand=1)
my_frame2.pack(fill="both",expand=1)

my_notebook.add(my_frame1,text = "All Cards")
my_notebook.add(my_frame2,text = "Deck Build+Test")

handList = Listbox(my_frame1,listvariable=Variable(value=list(countries.keys())),selectmode=SINGLE)
handList.bind("<<ListboxSelect>>",selected) # this is called "binding"
handList.pack()


root.mainloop()