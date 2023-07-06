import tkinter as tk

def add():
    print("add")

window = tk.Tk()
entry1 = tk.Entry(fg="red", bg="black", width=50)
entry2 = tk.Entry(fg="red", bg="black", width=50)
entry1.pack()
entry2.pack()
button = tk.Button(text="add", width=25, height=5, bg="blue"add())
button.pack()

window.mainloop()
