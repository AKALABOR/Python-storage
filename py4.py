import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("240x320")
        self.root.resizable(False, False)
        self.expression = ""

        self.entry = tk.Entry(root, font=('Arial', 14), bd=5, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=4, ipady=10, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.on_button_click(x)
            tk.Button(root, text=text, width=3, height=1, font=('Arial', 12), command=action)\
                .grid(row=row, column=col, padx=5, pady=5)

        tk.Button(root, text='C', width=16, height=1, font=('Arial', 12), command=self.clear)\
            .grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            try:
                if any(c not in "0123456789+-*/.()" for c in self.expression):
                    raise ValueError("Некоректний символ у виразі.")
                result = eval(self.expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.expression = str(result)
            except ZeroDivisionError:
                messagebox.showerror("Помилка", "Ділення на нуль!")
                self.clear()
            except Exception as e:
                messagebox.showerror("Помилка", f"Некоректний вираз!\n{e}")
                self.clear()
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
