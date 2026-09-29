from questions import create_question
from questions import create_subject
from characters import select_character
import tkinter as tk

def main():
    # Set screen
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Neptunia Character quiz")

    # Set Variables for quiz
    answer = select_character()
    create_subject()
    question = create_question(answer)
    correct_answer = answer["name"].lower()

    # Set Variables for Widgets
    question_var = tk.StringVar()
    question_var.set(question)
    input_var = tk.StringVar()
    answer_var = tk.StringVar()
    answer_var.set("")

    # submits entry to check answer
    def submit():
        input = input_var.get()
        input_var.set("")
        if input.lower() == correct_answer:
            answer_var.set("Correct")
            answer = select_character()
            create_subject()
        else:
            answer_var.set("Incorrect")

    # Set Widgets
    question_label = tk.Label(root, textvariable = question_var)
    input_entry = tk.Entry(root,textvariable = input_var)
    submit_button = tk.Button(root,text = 'Submit', command = submit)
    answer_label = tk.Label(root, textvariable = answer_var)

    #  Create Widget in root
    question_label.pack()
    input_entry.pack()
    submit_button.pack()
    answer_label.pack()

    root.mainloop()
main()

# Program now runs in Tkinter but question and character is not changing and need to re add player count
