from questions import create_question
from questions import select_character

def main():
    answer = select_character()
    end_quiz = False
    end_score = 3
    player_score = 0
    while end_quiz == False:
        if player_score == end_score: # ends quiz on 3 correct answers
            end_quiz = True
        else:
            question = create_question(answer)
            correct_answer = answer["name"].lower()
            print(question)
            player_answer = input("Enter answer: ")

            if player_answer.lower() == correct_answer: # when a answer is correct it adds to player_score, resets the questions asked and selects a new character
                print("Correct")
                player_score += 1
                answer = select_character()
            else: print("Incorrect - try again")

main()



# next have it so the same character can not come up again
