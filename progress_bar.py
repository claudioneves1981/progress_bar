import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Progress Bar")
root.geometry("350x120")

progress = ttk.Progressbar(root, length=300,
mode="determinate", maximum=100)
progress.pack(pady=25)

def update():
    if progress["value"] < 100:
        progress["value"] += 2
        root.after(50, update)

ttk.Button(root, text="Start", command=update).pack()

root.mainloop()