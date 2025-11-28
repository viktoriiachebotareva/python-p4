from tkinter import *
from tkinter import messagebox
import requests
import json

def get_data():
    user = entry.get()
    if not user:
        messagebox.showwarning('Ошибка', 'Введите имя пользователя GitHub')
        return

    url = f"https://api.github.com/users/{user}"

    try:
        data = requests.get(url).json()
        
        result = {"company": data.get("company"), "created_at": data.get("created_at"), "email": data.get("email"), "id": data.get("id"), "name": data.get("name"), "url": data.get("url")}
        file = f"github_user_{user}.json"
        with open(file, "w") as f:
            json.dump(result, f, indent=2)
        
        text_output.delete(1.0, END)
        text_output.insert(END, json.dumps(result, indent=2))
        
        messagebox.showinfo('Успех', f'Данные сохранены в файл: {file}')
        
    except Exception as e:
        messagebox.showerror('Ошибка', f'Не удалось получить данные: {e}')

win = Tk()
win.title("Информация о пользователе GitHub")
win.geometry('600x500')

lbl = Label(win, text="Введите имя пользователя GitHub:", font=("Times New Roman", 12), bg='light blue', fg='dark blue')
lbl.grid(column=0, row=0, padx=10, pady=10)

entry = Entry(win, width=30, font=("Times New Roman", 12), bg='white', fg='black')
entry.grid(column=1, row=0, padx=10, pady=10)
entry.focus()

btn = Button(win, text="Получить данные", command=get_data, font=("Times New Roman", 12), bg='blue', fg='white')
btn.grid(column=2, row=0, padx=10, pady=10)

output_lbl = Label(win, text="Полученные данные:", font=("Times New Roman", 12), bg='light blue', fg='dark blue')
output_lbl.grid(column=0, row=1, padx=10, pady=10)

text_output = Text(win, width=70, height=20, font=("Times New Roman", 12), bg='white', fg='black')
text_output.grid(column=0, row=2, padx=10, pady=10, columnspan=3)

win.mainloop()
