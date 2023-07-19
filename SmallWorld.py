import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

import requests
from tkinter import *
from tkinter import ttk

# Get all Cards
response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
data = response.json()['data'] # list of dictionaries, each dict is a card
monsters = {}

exclude = {"Spell Card", "Trap Card","Fusion Monster","Link Monster","Pendulum Effect Fusion Monster","Synchro Monster","Synchro Pendulum Effect Monster","Synchro Tuner Monster","XYZ Monster","XYZ Pendulum Effect Monster","Skill Card","Token"}
# {} is a set (cannot change items, but can add or remove)

# Get all Monsters and break into 
monsters["Please Pick A Monster"] = [""]
for i in data:
    if not i['type'] in exclude:
        toappend = [i['attribute'],i['race'],i['level'],i['atk'], i['def']]
        monsters[i['name']] = toappend



# Given a monster, determine applicable matches

def smallWorld(monsters,curMon):
    i = 0
    n = 0
    matches = []    
    maxcounter = len(monsters)
    curMon = stats[2] # this to be replaced with user feedback
    while (i < maxcounter):
        # print(curMon)
        test = []
        while(n<5):
            # print(n)
            # print(stats[i][n+1])
            if stats[i][n+1] == curMon[n+1]:
                test.append(1)
            else:
                test.append(0)
            n+=1
        n = 0
        if sum(test) == 1:
            matches.append(i)
        i+=1
    return matches

handMonSelected []
# Methods for widget buttons
def selectedHand(event):
    print(state)
    state = [1, 0, 0]
    handMonSelected = repr(handMon[handList.get(handList.curselection())])
    drawGenFrame(state)

def selectedBridge(event):
    state = [0, 0, 0]
    drawGenFrame(state)

def selectedDeck(event):
    state = [0, 0, 0]
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

state = [0,0,0]

def drawGenFrame(state):
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
            handList.bind("<<ListboxSelected>>",selectedHand) # this is called "binding"
            bridgeList.bind("<<ListboxSelected>>",selectedBridge) # this is called "binding"
            deckList.bind("<<ListboxSelected>>",selectedDeck) # this is called "binding"
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
            handList.bind("<<handSelect>>",selectedHand) # this is called "binding"
            bridgeList.bind("<<bridgeSelect>>",selectedBridge) # this is called "binding"
            deckList.bind("<<deckSelect>>",selectedDeck) # this is called "binding"
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
        
mylabel = Label(my_frame1,text=repr(countries[handList.get(handList.curselection())])).pack()
          Label(general,text=repr(handMon[handList.get(handList.curselection())])).grid(row=6,column=0)

# Create Widget

        '''
        case [1, 0, 0]: # First Card only selected: show bridge options 
            
        case [0, 0, 1]: # Last Card Only selected: show bridge options

        case [0, 1, 0]: # Bridge Only selected: show first and last options
            
        case [1, 1, 0]: # First Card and Bridge selected: show last card options
            
        case [0, 1, 1]: # Last Card and Bridge selected: show first card options
            
        case [1, 0, 1]: # First and Last Card selected: show bridge options
                   
                   
                   handList = ttk.Combobox(general,value=list(handMon.keys()))
            bridgeList = ttk.Combobox(general,value=list(bridgeMon.keys()))
            deckList = ttk.Combobox(general,value=list(deckMon.keys()))
            handList.current(0)
            handList.bind("<<ComboboxSelected>>",selectedHand) # this is called "binding"
            bridgeList.current(0)
            bridgeList.bind("<<ComboboxSelected>>",selectedBridge) # this is called "binding"
            deckList.current(0)
            deckList.bind("<<ComboboxSelected>>",selectedDeck) # this is called "binding"
            handList.grid(row = 1,column=0)
            bridgeList.grid(row = 1,column=1)
            deckList.grid(row = 1,column=2)
        
         
           '''

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

drawGenFrame(state)
root.mainloop()
