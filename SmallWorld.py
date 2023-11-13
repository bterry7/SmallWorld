import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

import requests
from tkinter import *
from tkinter import ttk

from MonsterAPI.py import *

# Given a monster, determine applicable matches
monsters = monster_api()

def smallWorld(monsters,curMon):
    i = 0
    n = 0
    matches = []    
    maxcounter = len(monsters)
    while (i < maxcounter):
        # print(curMon)
        test = []
        while(n<5):
            # print(n)
            # print(stats[i][n+1])
            if monsters[i][n+1] == curMon[n+1]:
                test.append(1)
            else:
                test.append(0)
            n+=1
        n = 0
        if sum(test) == 1:
            matches.append(i)
        i+=1
    return matches

handMonSelected = []
# Methods for widget buttons
def cardSelect(event,listOpt,keys):
    state = [1, 0, 0]
    print(state)
    handMonSelected = repr(handMon[handList.get(handList.curselection())])
    drawGenFrame(state)

def resetHand():
    state = [0, 0, 0]
    drawGenFrame(state)
def resetBridge():
    state = [0, 0, 0]
    drawGenFrame(state)
def resetDeck():
    state = [0, 0, 0]
    drawGenFrame(state)

def resetAll():
    state = [0, 0, 0]
    drawGenFrame(state)


def drawGenFrame(state):

    global handList
    global bridgeList
    global deckList
    
    # Column Labels
    handLabel = Label(general,text="Monster in Hand").grid(row=0,column=0)
    handLabel = Label(general,text="Bridge").grid(row=0,column=1)
    handLabel = Label(general,text="Added Monster").grid(row=0,column=2)

    # Reset List Buttons
    handButton = Button(general, text="Reset Monster In Hand", command=resetHand).grid(row=3,column=0)
    bridgeButton = Button(general, text="Reset Bridge Monster", command=resetBridge).grid(row=3,column=1)
    endButton = Button(general, text="Reset Added Monster", command=resetDeck).grid(row=3,column=2)

    # Reset All
    resetButton = Button(general, text="Reset All Lists", command=resetAll).grid(row=4,column=0,columnspan=3)

    print(state)
    match state:
        case [0, 0, 0]: # Base State

            # Lists
            handList = Listbox(general,listvariable=Variable(value=list(handMon.keys())),selectmode=SINGLE,exportselection=FALSE)
            bridgeList = Listbox(general,listvariable=Variable(value=list(bridgeMon.keys())),selectmode=SINGLE,exportselection=FALSE)
            deckList = Listbox(general,listvariable=Variable(value=list(deckMon.keys())),selectmode=SINGLE,exportselection=FALSE)
            handList.bind("<<ListboxSelect>>",lambda event: cardSelect(event,1)) # this is called "binding"
            bridgeList.bind("<<ListboxSelect>>",lambda event: cardSelect(event,2)) # this is called "binding"
            deckList.bind("<<ListboxSelect>>",lambda event: cardSelect(event,3)) # this is called "binding"
            handList.grid(row = 1,column=0)
            bridgeList.grid(row = 1,column=1)
            deckList.grid(row = 1,column=2)

            # List Status Labels
            handLabel = Label(general,text="Monster in Hand Status: Open").grid(row=2,column=0)
            handLabel = Label(general,text="Bridge Monster Status: Open").grid(row=2,column=1)
            handLabel = Label(general,text="Deck Monster Status: Open").grid(row=2,column=2)

        case [1, 0, 0]: # Base State

            # Lists

            # Display states if applicable:
            handLabel = Label(general,text="Attribute, Type, Level, Atk, Def").grid(row=5,column=0,columnspan=3)

            statsLabel = Label(general,text=handMonSelected).grid(row=6,column=0)
            #statsLabel = Label(general,text=repr(bridgeMon[bridgeList.get(bridgeList.curselection())])).grid(row=6,column=1)
            #statsLabel = Label(general,text=repr(deckMon[deckList.get(deckList.curselection())])).grid(row=6,column=2)
            

        case _: # Default to a reset

            # Lists
            handList = Listbox(general,listvariable=Variable(value=list(handMon.keys())),selectmode=SINGLE,exportselection=FALSE)
            bridgeList = Listbox(general,listvariable=Variable(value=list(bridgeMon.keys())),selectmode=SINGLE,exportselection=FALSE)
            deckList = Listbox(general,listvariable=Variable(value=list(deckMon.keys())),selectmode=SINGLE,exportselection=FALSE)
            handList.bind("<<ListboxSelect>>",lambda event: cardSelect(event,1)) # this is called "binding"
            bridgeList.bind("<<ListboxSelect>>",lambda event: cardSelect(event,2)) # this is called "binding"
            deckList.bind("<<ListboxSelect>>",lambda event: cardSelect(event,3)) # this is called "binding"
            handList.grid(row = 1,column=0)
            bridgeList.grid(row = 1,column=1)
            deckList.grid(row = 1,column=2)

            # List Status Labels
            handLabel = Label(general,text="Monster in Hand Status: Open").grid(row=2,column=0)
            handLabel = Label(general,text="Bridge Monster Status: Open").grid(row=2,column=1)
            handLabel = Label(general,text="Deck Monster Status: Open").grid(row=2,column=2)

            # Display states if applicable:
            handLabel = Label(general,text="Attribute, Type, Level, Atk, Def").grid(row=5,column=0,columnspan=3)
               
            statsLabel = Label(general,text=repr(handMon[handList.get(handList.curselection())])).grid(row=6,column=0)
            statsLabel = Label(general,text=repr(bridgeMon[bridgeList.get(bridgeList.curselection())])).grid(row=6,column=1)
            statsLabel = Label(general,text=repr(deckMon[deckList.get(deckList.curselection())])).grid(row=6,column=2)
        
# Create Widget

       
root = Tk()
totHeight = 750
totWidth = 1500
root.geometry("1500x750")
root.title("Small World")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

general = Frame(my_notebook,width=totWidth,height=totHeight)
deck = Frame(my_notebook,width=totWidth,height=totHeight)

general.pack(fill="both",expand=1)
deck.pack(fill="both",expand=1)

my_notebook.add(general,text = "All Cards")
my_notebook.add(deck,text = "Deck Build+Test")

handMon = monsters
bridgeMon = monsters
deckMon = monsters

drawGenFrame([0,0,0])
root.mainloop()