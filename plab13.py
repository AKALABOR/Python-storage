import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

with open("phones.json", "r", encoding="utf-8") as file:
    data = json.load(file)

phones = data["data"] if "data" in data else data

def search_phones(query):
    return [p for p in phones if query.lower() in p["title"].lower()]

def sort_phones(key):
    return sorted(phones, key=lambda p: p.get(key) or 0, reverse=True)

def show_details(phone):
    top = tk.Toplevel(root)
    top.title(phone["title"])
    details = f"Назва: {phone['title']}\n"
    details += f"Ціна: {phone.get('price', 'Немає')}\n"
    details += f"Рейтинг: {phone.get('rating', 'Немає')}\n"
    details += f"Відгуки: {phone.get('comments_amount', 'Немає')}\n"
    tk.Label(top, text=details, justify="left", padx=10, pady=10).pack()

def update_list(phones_list):
    listbox.delete(0, tk.END)
    for phone in phones_list:
        listbox.insert(tk.END, phone["title"])

def on_search():
    query = search_var.get()
    filtered = search_phones(query)
    update_list(filtered)

def on_sort_price():
    sorted_phones = sort_phones("price")
    update_list(sorted_phones)

def on_sort_rating():
    sorted_phones = sort_phones("rating")
    update_list(sorted_phones)

def on_sort_reviews():
    sorted_phones = sort_phones("comments_amount")
    update_list(sorted_phones)

def on_select(event):
    index = listbox.curselection()
    if index:
        title = listbox.get(index)
        phone = next((p for p in phones if p["title"] == title), None)
        if phone:
            show_details(phone)

root = tk.Tk()
root.title("Телефони Rozetka")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

search_var = tk.StringVar()
tk.Entry(frame, textvariable=search_var).pack(side=tk.LEFT)
tk.Button(frame, text="Пошук", command=on_search).pack(side=tk.LEFT)

tk.Button(frame, text="Сортувати за ціною", command=on_sort_price).pack(side=tk.LEFT)
tk.Button(frame, text="Сортувати за рейтингом", command=on_sort_rating).pack(side=tk.LEFT)
tk.Button(frame, text="Сортувати за відгуками", command=on_sort_reviews).pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=60)
listbox.pack(padx=10, pady=10)
listbox.bind("<<ListboxSelect>>", on_select)

update_list(phones)

root.mainloop()
