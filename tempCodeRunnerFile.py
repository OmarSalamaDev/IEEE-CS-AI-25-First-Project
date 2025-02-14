# window setup
root = tk.Tk()
root.title("Library Management System")
root.geometry("1000x500")
root.resizable(False, False)
root.configure(background="#eeeeee")


# set window icon
icon = tk.PhotoImage(file="book_icon.png")
root.iconphoto(False, icon)


# create screens (Frames)
main_screen = create_main_screen(root)
add_book_screen = create_add_book_screen(root)
view_books_screen = create_view_books_screen(root)
search_book_screen = create_search_book_screen(root)


# initially show the main menu screen
current_screen = main_screen
current_screen.pack(fill="both", expand=True, padx=20, pady=20)


# function to switch screens
def switch_screen(new_screen):
    global current_screen
    current_screen.pack_forget()
    new_screen.pack(fill="both", expand=True)
    current_screen = new_screen


# Navigation Functions
def to_add_book_screen():
    switch_screen(add_book_screen)

def to_view_books_screen():
    switch_screen(view_books_screen)

def to_search_book_screen():
    switch_screen(search_book_screen)

def to_main_screen():
    switch_screen(main_screen)


# navigation buttons
btn1 = button(main_screen, "Add Book", to_add_book_screen)
btn2 = button(main_screen, "View Books", to_view_books_screen)
btn3 = button(main_screen, "Search Book", to_search_book_screen)
btn4 = button(add_book_screen , "Back to action selection", to_main_screen)
btn5 = button(search_book_screen , "Back to action selection", to_main_screen)
btn6 = button(view_books_screen , "Back to action selection", to_main_screen)

# run the app
root.mainloop()
