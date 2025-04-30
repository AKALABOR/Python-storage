import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        celsius = float(entry.get())
        fahrenheit = celsius * 9/5 + 32
        result_label.config(text=f"Температура у Фаренгейтах: {fahrenheit:.2f}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректне число")

root = tk.Tk()
root.title("Конвертер температури")

entry_label = tk.Label(root, text="Введіть температуру в Цельсіях:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()
convert_button = tk.Button(root, text="Конвертувати", command=convert_temperature)
convert_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
