from questions import create_question
from questions import select_character

def main():
    answer = select_character()
    end_quiz = False
    while end_quiz == False:
        question = create_question(answer)
        correct_answer = answer["name"].lower()
        print(question)
        player_answer = input("Enter answer: ")
        if player_answer.lower() == correct_answer:
            print("Correct")
            end_quiz = True
        else: print("Incorrect - try again")
main()
