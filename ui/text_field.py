import tkinter as tk

def text_field(root, placeholder):

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")


    entry = tk.Entry(root, width=30, fg="gray")
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
    entry.pack(pady=10)   

    return entry