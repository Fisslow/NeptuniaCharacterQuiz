from characters import all_characters
import random

question_asked = []

def select_character():
    return all_characters[random.randrange(0,3)]

def create_question(char):
    current_character = char
    question_subject = random.randrange(1,4)
    if question_subject in question_asked:
        if len(question_asked) == 3:
            return "All question asked"
        else:
            question_subject = random.randrange(1,4)
    if question_subject == 1: # Creates a question on characters Base location
        question_asked.append(1)
        return f"This character is located in {current_character["base"]}"

    if question_subject == 2: #Creates a question on characters race
        question_asked.append(2)
        return f"This character is a {current_character["race"]}"

    if question_subject == 3: # Creates a question on characters height
        question_asked.append(3)
        return f"This character is {current_character["height"]} centimetres tall"
