import tkinter as tk
from tkinter import ttk

def select_menu(root, options: list[str]):

    selected_value = tk.StringVar()

    dropdown = ttk.Combobox(root, textvariable=selected_value, values=options, state="readonly")
    dropdown.pack(pady=20)

    return selected_value
    