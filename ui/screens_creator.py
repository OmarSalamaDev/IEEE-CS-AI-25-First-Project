import tkinter as tk
from tkinter import ttk
from ui.text_field import text_field
from ui.button import button
from ui.table import table
from ui.select_menu import select_menu
from repositry import *


def create_main_screen(root):

    main_menu = tk.Frame(root, bg="#eeeeee", padx=10, pady=10)
    tk.Label(main_menu, text="Welcome to the Library Management System!").pack(pady=10)

    return main_menu


def create_add_book_screen(root):
    
    add_book_screen = tk.Frame(root, bg="#eeeeee", padx=10, pady=10)
    tk.Label(add_book_screen, text="Enter book details to add a new book to the library.").pack(pady=10)

    
    error_msg = tk.StringVar()
    error_msg.set("")
    success_msg = tk.StringVar()
    success_msg.set("")


    def add(title, author, price, description, category, publisher):
        if title == "enter title..." or author == "enter author..." or price == "enter price..." or description == "enter description..." or category == "enter category..." or publisher == "enter publisher...":
            error_msg.set("Please fill in all fields.")
            success_msg.set("")
            return
        
        state = add_book(title, author, price, description, category, publisher)

        if not state:
            error_msg.set("An error occurred, please try again.")
            success_msg.set("")
            return

        save = save_to_file()

        if not save:
            error_msg.set("Could not save to file.")
            success_msg.set("")
            return
        
        error_msg.set("")
        success_msg.set("Book added successfully.")


    title = text_field(add_book_screen, "enter title...")
    author = text_field(add_book_screen, "enter author...")
    price = text_field(add_book_screen, "enter price...")
    description = text_field(add_book_screen, "enter description...")
    category = text_field(add_book_screen, "enter category...")
    publisher = text_field(add_book_screen, "enter publisher...")
    
    button(add_book_screen, "Add book", lambda: add(title.get(), author.get(), price.get(), description.get(), category.get(), publisher.get()))

    error_label = tk.Label(add_book_screen, textvariable=error_msg, fg="red").pack(pady=2)
    success_label = tk.Label(add_book_screen, textvariable=success_msg, fg="green").pack(pady=2)

    return add_book_screen


def create_view_books_screen(root):
      
    view_books_screen = tk.Frame(root, bg="#eeeeee", padx=10, pady=10)
    tk.Label(view_books_screen, text="Enter book details to add a new book to the library.").pack(pady=10)

    error_msg = tk.StringVar()
    error_msg.set("")

    isLoaded = load_from_file()
    booksList = view_books()

    if not isLoaded:
        error_msg.set("Couldn't load the file.")
    
    if booksList == [] :
        error_msg.set("No books found.")

    books_table = table(view_books_screen, "Title", "Author", "Price", "Description", "Category", "publisher")
    
    for row in books_table.get_children():
        books_table.delete(row)

    for book in booksList:
        books_table.insert("", "end", values=[book.title, book.author, book.price, book.description, book.category, book.publisher])

    tk.Label(view_books_screen, textvariable=error_msg, fg="red").pack(pady=2)

    return view_books_screen


def create_search_book_screen(root):
    
    load_from_file()

    search_book_screen = tk.Frame(root, bg="#eeeeee", padx=10, pady=10)
    tk.Label(search_book_screen, text="Search for a book in the library.").pack(pady=10)

    error_msg = tk.StringVar()
    books_table = table(search_book_screen, "Title", "Author", "Price", "Description", "Category", "Publisher")

    def getBook(text):
        print(text)
        if text == "" or text == "Search by title...":
            error_msg.set("Please enter a search term.")
            return
        else:
            error_msg.set("")

        for row in books_table.get_children():
            books_table.delete(row)

        books = search_book_by_title(text)
        if books == []:
            error_msg.set("No books found.")
            return
        for book in books:
            books_table.insert("", "end", values=[
                book.title, book.author, book.price, book.description, book.category, book.publisher
            ])

    search = text_field(search_book_screen, "Search by title...")
    button(search_book_screen, "Search", lambda: getBook(search.get()))

    tk.Label(search_book_screen, textvariable=error_msg, fg="red").pack(pady=2)

    return search_book_screen


def create_edit_book_screen(root):

    load_from_file()

    edit_book_screen = tk.Frame(root, bg="#eeeeee", padx=10, pady=10)
    tk.Label(edit_book_screen, text="Search for a book in the library.").pack(pady=10)

    error_msg = tk.StringVar()
    error_msg.set("")
    success_msg = tk.StringVar()
    success_msg.set("")
    
    books = view_books()
    if books == []:
        error_msg.set("No books found.")
        return edit_book_screen
    
    books_list = [book.title for book in books]
    selected_book = select_menu(edit_book_screen, books_list)

    def del_Book():
        if selected_book.get() == "":
            error_msg.set("Please select a book to delete.")
            success_msg.set("")
            return edit_book_screen
        
        if delete_book(books[books_list.index(selected_book.get())].isbn):
            error_msg.set("")
            success_msg.set("Book deleted successfully.")
            selected_book.set("")
        else:
            error_msg.set("An error occurred, please try again.")
            success_msg.set("")


    button(edit_book_screen, "Delete", lambda: del_Book())

    tk.Label(edit_book_screen, textvariable=error_msg, fg="red").pack(pady=2)
    tk.Label(edit_book_screen, textvariable=success_msg, fg="green").pack(pady=2)

    return edit_book_screen


def create_delete_book_screen(root):

    load_from_file()

    edit_book_screen = tk.Frame(root, bg="#eeeeee", padx=10, pady=10)
    tk.Label(edit_book_screen, text="Search for a book in the library.").pack(pady=10)

    error_msg = tk.StringVar()
    error_msg.set("")
    success_msg = tk.StringVar()
    success_msg.set("")
    
    books = view_books()
    if books == []:
        error_msg.set("No books found.")
        return edit_book_screen
    
    books_list = [book.title for book in books]
    selected_book = select_menu(edit_book_screen, books_list)

    def del_Book():
        if selected_book.get() == "":
            error_msg.set("Please select a book to delete.")
            success_msg.set("")
            return edit_book_screen
        
        if delete_book(books[books_list.index(selected_book.get())].isbn):
            error_msg.set("")
            success_msg.set("Book deleted successfully.")
            selected_book.set("")
        else:
            error_msg.set("An error occurred, please try again.")
            success_msg.set("")


    button(edit_book_screen, "Delete", lambda: del_Book())

    tk.Label(edit_book_screen, textvariable=error_msg, fg="red").pack(pady=2)
    tk.Label(edit_book_screen, textvariable=success_msg, fg="green").pack(pady=2)

    return edit_book_screen