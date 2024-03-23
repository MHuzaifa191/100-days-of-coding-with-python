from tkinter import *
from PIL import ImageTk, Image
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, question_bank) -> None:
        self.quiz = QuizBrain(question_bank)
        self.score = 0
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.configure(bg=THEME_COLOR)

        self.question_frame = Frame(self.window, bg="white", padx=20, pady=20)
        self.question_frame.pack(pady=50)

        self.question_label = Label(self.question_frame, text="", bg="white", fg="black", padx=20, pady=20)
        self.question_label.pack()

        self.true_image = ImageTk.PhotoImage(Image.open("Images\\true.png"))
        self.false_image = ImageTk.PhotoImage(Image.open("Images\\false.png"))

        self.true_button = Button(self.window, image=self.true_image, padx=20, pady=20, command=self.true_pressed)
        self.true_button.pack(side="left", padx=20)

        self.false_button = Button(self.window, image=self.false_image, padx=20, pady=20, command=self.false_pressed)
        self.false_button.pack(side="right", padx=20)

        self.score_label = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.place(x=10, y=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question = self.quiz.next_question()
        if question == '-1':
            self.show_result()
        else:
            self.question_label.config(text=question)

    def true_pressed(self):
        if self.quiz.check_answer("True"):
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.get_next_question()

    def false_pressed(self):
        if self.quiz.check_answer("False"):
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.get_next_question()

    def show_result(self):
        result_window = Toplevel(self.window)
        result_window.title("Quiz Result")
        result_window.configure(bg=THEME_COLOR)

        total_questions = self.quiz.question_number - 1
        result_label = Label(result_window, text=f"Quiz over!", bg=THEME_COLOR, fg="white")
        result_label = Label(result_window, text=f"Your score: {self.score}/{total_questions}", bg=THEME_COLOR, fg="white")
        result_label.pack(pady=50)

# Usage
# quiz_ui = QuizUI(question_bank)
