from questions import create_question
from questions import create_subject
from characters import select_character
import tkinter as tk

# Set Variables for quiz
answer = select_character()
create_subject()
question = create_question(answer)
correct_answer = answer["name"].lower()
player_score = 0


def main():
    # Set screen
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Neptunia Character quiz")

    def quit():
        root.destroy()

    # Set Variables for Widgets
    question_var = tk.StringVar()
    question_var.set(question)
    input_var = tk.StringVar()
    answer_var = tk.StringVar()
    answer_var.set("")
    pervious_var1 = tk.StringVar()
    pervious_var1.set("")
    pervious_var2 = tk.StringVar()
    pervious_var2.set("")
    pervious_var3 = tk.StringVar()
    pervious_var3.set("")
    pervious_var4 = tk.StringVar()
    pervious_var4.set("")
    question_ammount_var = tk.StringVar()
    question_ammount_var.set("0 / 5")

    # submits entry to check answer
    def submit():
        global answer
        global question
        global correct_answer
        global player_score
        input = input_var.get()
        input_var.set("")
        pervious_question1 = pervious_var1.get()
        pervious_question2 = pervious_var2.get()
        pervious_question3 = pervious_var3.get()
        pervious_question4 = pervious_var4.get()


        if input.lower() == correct_answer:
            player_score += 1
            if player_score == 5:
                quit()
            answer_var.set("Correct")
            answer = select_character()
            correct_answer = answer["name"].lower()
            create_subject()
            question = create_question(answer)
            question_var.set(question)
            pervious_var1.set("")
            pervious_var2.set("")
            pervious_var3.set("")
            pervious_var4.set("")
            question_ammount_var.set(f"{player_score} / 5")

        else:
            answer_var.set("Incorrect")

            x = False
            while x != True:
                if pervious_question1 == "":
                    pervious_var1.set(f"{question}")
                    x = True
                    break
                if pervious_question2 == "":
                    pervious_var2.set(f"{question}")
                    x = True
                    break
                if pervious_question3 == "":
                    pervious_var3.set(f"{question}")
                    x = True
                    break
                if pervious_question4 == "":
                    pervious_var4.set(f"{question}")
                    x = True
                    break
                else:
                    break

            question = create_question(answer)
            question_var.set(question)





    # Set Widgets
    question_label = tk.Label(root, textvariable = question_var)
    input_entry = tk.Entry(root,textvariable = input_var)
    submit_button = tk.Button(root,text = 'Submit', command = submit)
    answer_label = tk.Label(root, textvariable = answer_var)
    pervious_question1 = tk.Label(root, textvariable = pervious_var1)
    pervious_question2 = tk.Label(root, textvariable = pervious_var2)
    pervious_question3 = tk.Label(root, textvariable = pervious_var3)
    pervious_question4 = tk.Label(root, textvariable = pervious_var4)
    question_ammount = tk.Label(root, textvariable = question_ammount_var)

    #  Create Widget in root
    question_label.pack()
    input_entry.pack()
    submit_button.pack()
    answer_label.pack()
    pervious_question1.pack()
    pervious_question2.pack()
    pervious_question3.pack()
    pervious_question4.pack()
    question_ammount.pack()

    root.mainloop()
main()

# Program now runs in Tkinter but question and character is not changing and need to re add player count
