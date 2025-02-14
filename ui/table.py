from tkinter import ttk

def table(root, *fields):

    table = ttk.Treeview(
        root,
        columns=fields,
        show="headings"
    )

    for field in fields:
        table.heading(field, text=field)
        table.column(field, width=120, anchor="center")

    table.pack(pady=10, fill="both", expand=True)

    return table