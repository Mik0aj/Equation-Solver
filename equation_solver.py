import tkinter as tk
import random

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Equation Solver")
        
        self.equation_label = tk.Label(master, text="")
        self.equation_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.feedback_label = tk.Label(master, text="", fg="blue")
        self.feedback_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.answer_entry = tk.Entry(master, width=20, borderwidth=5)
        self.answer_entry.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.buttons = [
            ('1', '1', 'a'), ('2', '2', 's'), ('3', '3', 'd'),
            ('4', '4', 'f'), ('5', '5', 'g'), ('6', '6', 'h'),
            ('7', '7', 'j'), ('8', '8', 'k'), ('9', '9', 'l'),
            ('0', '0', ';'), ('-', '-', 't'), ('=', '=', 'y')
        ]

        self.create_buttons()

        self.generate_equation()

        # Bind keyboard events
        self.master.bind('<KeyPress>', self.key_pressed)
        
    def create_buttons(self):
        row, col = 3, 0
        for label, action, key in self.buttons:
            if action == '=':
                btn = tk.Button(self.master, text=label, padx=40, pady=20, command=self.check_answer)
            elif action == '-':
                btn = tk.Button(self.master, text=label, padx=40, pady=20, command=self.add_minus)
            else:
                btn = tk.Button(self.master, text=label, padx=40, pady=20, command=lambda num=action: self.add_to_entry(num))
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 3:
                col = 0
                row += 1
                
    def add_to_entry(self, num):
        current = self.answer_entry.get()
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.insert(0, current + str(num))

    def add_minus(self):
        current = self.answer_entry.get()
        if current and current[0] != '-':
            self.answer_entry.insert(0, '-')
        elif current and current[0] == '-':
            self.answer_entry.delete(0)
        else:
            self.answer_entry.insert(0, '-')

    def generate_equation(self):
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        operator = random.choice(['+', '-', '*'])
        self.equation = f"{num1} {operator} {num2}"
        self.equation_label.config(text=self.equation)
        self.correct_answer = eval(self.equation)
        self.feedback_label.config(text="")

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = int(user_answer)
            if user_answer == self.correct_answer:
                result_text = "Correct!"
                self.feedback_label.config(text=result_text, fg="green")
            else:
                result_text = f"Incorrect. Correct answer is {self.correct_answer}."
                self.feedback_label.config(text=result_text, fg="red")
        except ValueError:
            result_text = "Invalid input. Please enter a number."
            self.feedback_label.config(text=result_text, fg="red")
            
        self.answer_entry.delete(0, tk.END)
        self.master.after(2000, self.generate_equation)  # Wait for 2 seconds and generate a new equation

    def key_pressed(self, event):
        key = event.char
        for label, action, key_binding in self.buttons:
            if key == key_binding:
                if action.isdigit() or action == '-':
                    self.add_to_entry(action)
                elif action == '=':
                    self.check_answer()

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
