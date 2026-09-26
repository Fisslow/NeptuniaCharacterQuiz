from characters import all_characters
import random

def create_question():
    current_character = all_characters[random.randrange(0,3)]
    question_subject = random.randrange(1,3)
    if question_subject == 1: # Creates a question on characters Base location
        return f"This character is located in {current_character["base"]}", current_character

    if question_subject == 2: #Creates a question on characters race
        return f"This character is a {current_character["race"]}", current_character

    if question_subject == 3: # Creates a question on characters height
        return f"This character is {current_character["height"]} centimetres tall", current_character
