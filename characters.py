import random

Neptune = {"name": "Neptune", "base": "Planeptune", "race": "Goddess","height": "146", "weapon": "Swords"}
Noire = {"name": "Noire", "base": "Lastation", "race": "Goddess","height": "158", "weapon": "Swords"}
Blanc = {"name": "Blanc", "base": "Lowee", "race": "Goddess","height": "144", "weapon": "Hammers"}
Vert = {"name": "Vert", "base": "Leanbox", "race": "Goddess","height": "163", "weapon": "Spears"}
Nepgear = {"name": "Nepgear", "base": "Planeptune", "race": "Goddess","height": "153", "weapon": "Swords"}
Uni = {"name": "Uni", "base": "Lastation", "race": "Goddess","height": "149", "weapon": "Rifles"}
Rom = {"name": "Rom", "base": "Lowee", "race": "Goddess","height": "132", "weapon": "Maces"}
Ram = {"name": "Ram", "base": "Lowee", "race": "Goddess","height": "132", "weapon": "Staffs"}
Compa = {"name": "Compa", "base": "Planeptune", "race": "Human","height": "152", "weapon": "Syringes"}
If = {"name": "IF", "base": "Planeptune", "race": "Human","height": "149", "weapon": "Qatars"}

all_characters = [Neptune, Noire, Blanc, Vert, Nepgear, Uni, Rom, Ram, Compa, If]
shuffled_characters = all_characters

def character_shuffle(): # Shuffles the shuffled_characters list in a random order
    random.shuffle(shuffled_characters)

def select_character(): # selects and removes the first entry in the shuffled_characters list.
    character_shuffle()
    selected = shuffled_characters.pop(0)
    return selected
