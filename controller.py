import tkinter as tk
from ui.button import *
from ui.screens_creator import *


# window setup
root = tk.Tk()
root.title("Library Management System")
root.geometry("1000x500")
root.resizable(False, False)
root.configure(background="#eeeeee")


# set window icon
icon = tk.PhotoImage(file="book_icon.png")
root.iconphoto(False, icon)


screens = {
        "main": create_main_screen(root),
        "add_book": create_add_book_screen(root),
        "view_books": create_view_books_screen(root),
        "search_book": create_search_book_screen(root),
        "delete_book": create_delete_book_screen(root),
        "edit_book": create_edit_book_screen(root),
}


# Initially show only the main screen
current_screen = tk.StringVar()
current_screen.set("main")
screens[current_screen.get()].pack(fill="both", expand=True, padx=20, pady=20)

# def on_change(var, index, mode):
#     global screens
#     for screen in screens:
#         screens[screen].pack_forget()
#     screens = {
#         "main": create_main_screen(root),
#         "add_book": create_add_book_screen(root),
#         "view_books": create_view_books_screen(root),
#         "search_book": create_search_book_screen(root),
# }


# current_screen.trace_add("write", on_change)


# Navigation Functions
def show_screen(screen):
    global current_screen
    screens[current_screen.get()].pack_forget()  # Hide current screen
    screens[screen].pack(fill="both", expand=True)  # Show new screen
    current_screen.set(screen)  # Update current screen


# Back button for secondary screens
button(screens["add_book"], "Back to Main Menu", lambda: show_screen("main")).pack(pady=10)
button(screens["view_books"], "Back to Main Menu", lambda: show_screen("main")).pack(pady=10)
button(screens["search_book"], "Back to Main Menu", lambda: show_screen("main")).pack(pady=10)
button(screens["delete_book"], "Back to Main Menu", lambda: show_screen("main")).pack(pady=10)
button(screens["edit_book"], "Back to Main Menu", lambda: show_screen("main")).pack(pady=10)


# Navigation buttons on the main screen
button(screens["main"], "Add Book", lambda: show_screen("add_book")).pack(pady=10)
button(screens["main"], "View Books", lambda: show_screen("view_books")).pack(pady=10)
button(screens["main"], "Search Book", lambda: show_screen("search_book")).pack(pady=10)
button(screens["main"], "Delete a Book", lambda: show_screen("delete_book")).pack(pady=10)
button(screens["main"], "Edit a Book", lambda: show_screen("edit_book")).pack(pady=10)



# run the app
root.mainloop()