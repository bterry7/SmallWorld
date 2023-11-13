import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

import requests
from tkinter import *
from tkinter import ttk


def monster_api (monsters):

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

