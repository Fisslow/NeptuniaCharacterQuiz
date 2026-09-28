from characters import all_characters
import random

question_list = [] # list of questions to be asked

def select_character(): # selects random character
    create_subject()
    return all_characters[random.randrange(0,4)]

def create_subject():  # appends question_list with random numbers that are not repeating
    while len(question_list) < 3:
        num = random.randint(1, 3)
        if num not in question_list:
            question_list.append(num)

def create_question(char):
    current_character = char # sets characrer to access values

    if question_list == []: # is question_list is empty returns a statement
        return "All question asked"

    question_subject = question_list.pop(0) # picks the first value in the list and then removes it preventing the same question from being asked twice

    if question_subject == 1 and question_subject: # Creates a question on characters Base location
        #question_asked.append(1)
        return f"This character is located in {current_character["base"]}"

    if question_subject == 2 and question_subject: #Creates a question on characters race
        #question_asked.append(2)
        return f"This character is a {current_character["race"]}"

    if question_subject == 3 and question_subject: # Creates a question on characters height
        #question_asked.append(3)
        return f"This character is {current_character["height"]} centimetres tall"
