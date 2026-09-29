from characters import all_characters
import random

question_list = [] # list of questions to be asked

def create_subject():  # appends question_list with random numbers that are not repeating
    while len(question_list) < 4:
        num = random.randint(1, 4)
        if num not in question_list:
            question_list.append(num)

def create_question(char):
    current_character = char # sets characrer to access values

    if question_list == []: # is question_list is empty returns a statement
        return "All question asked"

    question_subject = question_list.pop(0) # picks the first value in the list and then removes it preventing the same question from being asked twice

    if question_subject == 1 and question_subject: # Creates a question on characters Base location
        return f"This character is located in {current_character["base"]}"

    if question_subject == 2 and question_subject: #Creates a question on characters race
        return f"This character is a {current_character["race"]}"

    if question_subject == 3 and question_subject: # Creates a question on characters height
        return f"This character is {current_character["height"]} centimetres tall"

    if question_subject == 4:
        return f"This character uses {current_character["weapon"]} in combat"
