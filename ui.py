from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        true = PhotoImage(file ="./images/true.png")
        false = PhotoImage(file="./images/false.png")

        #score label
        self.score_label = Label(text=f"score: 0", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300,height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",20,"italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(image=true, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    #def get_next_question(self):

