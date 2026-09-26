from questions import create_question

def main():
    end_quiz = False
    while end_quiz == False:
        question, answer = create_question()
        correct_answer = answer["name"].lower()
        print(question)
        player_answer = input("Enter answer: ")
        if player_answer.lower() == correct_answer:
            print("Correct")
            end_quiz = True
        else: print("Incorrect - try again")
main()
