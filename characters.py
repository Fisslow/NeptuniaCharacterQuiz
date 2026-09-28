import random

Neptune = {"name": "Neptune", "base": "Planeptune", "race": "Goddess","height": "146"}
Noire = {"name": "Noire", "base": "Lastation", "race": "Goddess","height": "158"}
Blanc = {"name": "Blanc", "base": "Lowee", "race": "Goddess","height": "144"}
Vert = {"name": "Vert", "base": "Leanbox", "race": "Goddess","height": "163"}

all_characters = [Neptune, Noire, Blanc, Vert]
shuffled_characters = all_characters

def character_shuffle():
    random.shuffle(shuffled_characters)

def select_character():
    character_shuffle()
    selected = shuffled_characters.pop(0)
    return selected
