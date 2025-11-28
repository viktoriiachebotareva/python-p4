import tkinter as tk
from tkinter import ttk, messagebox, filedialog

root = tk.Tk()
root.title("Чеботарева Виктория Евгеньевна")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(pady=20, expand=True, fill=tk.BOTH)

# Вкладка 1: Калькулятор
calc_frame = ttk.Frame(notebook)
notebook.add(calc_frame, text="Калькулятор")

tk.Label(calc_frame, text="Число 1:").grid(row=0, column=0, padx=20, pady=10)
num1_entry = tk.Entry(calc_frame, width=15)
num1_entry.grid(row=0, column=1, padx=20, pady=10)

tk.Label(calc_frame, text="Число 2:").grid(row=1, column=0, padx=20, pady=10)
num2_entry = tk.Entry(calc_frame, width=15)
num2_entry.grid(row=1, column=1, padx=20, pady=10)

operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar()
operation_var.set(operations[0])
operation_menu = tk.OptionMenu(calc_frame, operation_var, *operations)
operation_menu.grid(row=2, column=0, columnspan=2, pady=10)

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        op = operation_var.get()
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                raise ValueError("Деление на ноль!")
                
        result_label.config(text=f"Результат: {result}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

tk.Button(calc_frame, text="Рассчитать", command=calculate).grid(row=3, column=0, columnspan=2, pady=20)
result_label = tk.Label(calc_frame, text="Результат: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Вкладка 2: Чекбоксы
checkbox_frame = ttk.Frame(notebook)
notebook.add(checkbox_frame, text="Чекбоксы")

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

tk.Checkbutton(checkbox_frame, text="Первый", variable=var1).pack(pady=10)
tk.Checkbutton(checkbox_frame, text="Второй", variable=var2).pack(pady=10)
tk.Checkbutton(checkbox_frame, text="Третий", variable=var3).pack(pady=10)

def show_selection():
    selected = []
    if var1.get():
        selected.append("Первый")
    if var2.get():
        selected.append("Второй")
    if var3.get():
        selected.append("Третий")
        
    if selected:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected)}")
    else:
        messagebox.showinfo("Выбор", "Ничего не выбрано")

tk.Button(checkbox_frame, text="Проверить выбор", command=show_selection).pack(pady=20)

# Вкладка 3: Работа с текстом
text_frame = ttk.Frame(notebook)
notebook.add(text_frame, text="Работа с текстом")

text_area = tk.Text(text_frame, width=60, height=15)
text_area.pack(pady=20)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)

def open_file():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(1.0, file.read())
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при открытии файла: {str(e)}")

def save_file():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Текстовые файлы", "*.txt")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_area.get(1.0, tk.END))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при сохранении файла: {str(e)}")

file_menu.add_command(label="Открыть файл", command=open_file)
file_menu.add_command(label="Сохранить файл", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

root.mainloop()
