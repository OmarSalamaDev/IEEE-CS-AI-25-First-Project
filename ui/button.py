import tkinter as tk


def button(root, text, command):
    button = tk.Button(root, text=text, command=command)
    button.pack(pady=10)
    return button