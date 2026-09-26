def main():
    end_quiz = False
    while end == False:
        answer = input("Enter answer: ")
        if answer.lower() == "test":
            print("Correct")
            end_quiz = True
        else: print("Incorrect - try again")
main()
