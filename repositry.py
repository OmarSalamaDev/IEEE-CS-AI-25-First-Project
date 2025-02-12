
from Book import Book

# List to store books added
library = []


#------------------------------------------------------------------------------------


# todo add_book() -> Ahmed
# Input: book details 
# Output: return true if book added successfully, false if not
def add_book(title, author, price, description, isbn, category):
    is_adding = True 

    # Loop in case of wanting to add multiple books at once
    while is_adding: 
        new_book = {
            "Book Title": Book.set_book(), 
            "Book Author": Book.set_author(),
            "Book Price" : Book.set_price(),
            "Book Description": Book.set_description(),
            "Book ISBN": Book.set_isbn(), 
            "Book Category": Book.set_category
        }
        library.append(new_book)

        if input("Do you wish to add another book? (Y/N): ").lower() == "n":
            is_adding = False

    return True


#------------------------------------------------------------------------------------


# todo view books -> Ahmed
# Input: none
# Output: return a list of all books
def view_books():
    # Check output format with respect to GUI
    pass
    


#------------------------------------------------------------------------------------


# todo search book by title -> Ahmed
# Input: book title
# Output: return the book if found, otherwise return an empty list
def search_book(title):
    found_book = [book for book in library if book["Book Title"].lower() ==title.lower()]
    
    if not found_book:
        print(f"No books found with title: {title}.")
    else:
        for book in found_book:
            print(f"{book['Book Title']} by {book['Book Author']} (ISBN: {book['Book ISBN']})")


#------------------------------------------------------------------------------------


# todo search book by isbn -> Ahmed
# Input: book isbn
# Output: return the book if found, otherwise return an empty list
def search_book(isbn):
    found_book = [book for book in library if book["Book ISBN"].lower() == isbn.lower()]
    
    if not found_book:
        print(f"No book ISBN matches {isbn}.")
    else:
        for book in found_book:
            print(f"{book['Book Title']} by {book['Book Author']} (ISBN: {book['Book ISBN']})")


#------------------------------------------------------------------------------------


# todo update book details -> Mahmoud
# Input: book isbn
# Output: return true if book updated successfully, false if not
def update_book(isbn):
    """ Update book details by ISBN. Returns True if successful, False otherwise """
    for book in library:
        if book["Book ISBN"] == isbn:
            updates = update_helper_function(book)
            for key, value in updates.items():
                book[key] = value
            print("Book updated succefully.")
            # print book details after update
            print_book_details(book)
            return True
    print(f"No book found with ISBN: {isbn}!")
    return False


def update_helper_function(book):
    """ Get updated book details from user input. Keeps existing values if input is empty """
    print("\nUpdating book details. Press Enter to keep existing values.\n")

    title = input(f"Enter the book title [{book['Book Title']}]: ") or book['Book Title']
    author = input(f"Enter the book author [{book['Book Author']}]: ") or book['Book Author']
    while True:
        price = input(f"Enter the book price [{book['Book Price']}]: ")
        if not price:
            price = book['Book Price']
            break
        try:
            price = int(price)
            if price > 0:
                break
            else:
                print("Invalid input! Price must be a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    desc = input(f"Enter the book description [{book['Book Description']}]: ") or book['Book Description']
    categ = input(f"Enter the book category [{book['Book Category']}]: ") or book['Book Category']

    return {"Book Title":title, 
            "Book Author": author,
            "Book Price": price,
            "Book Description": desc,
            "Book Category": categ}

#------------------------------------------------------------------------------------


# todo delete book -> Mahmoud
# Input: book isbn
# Output: return true if book updated successfully, false if not
def delete_book(isbn):
    """ Delete a book by ISBN. Returns True if deleted, False otherwise. """
    for i, book in enumerate(library):
        if book["Book ISBN"] == isbn:
            print("\nFound book to delete:\n")
            print_book_details(book)
            confirm = input(f"Are you sure you want to delete this book {book['Book Title']}? (Y/N)").lower()
            if confirm == 'y':
                del library[i]
                print("Book deleted successully.")
                return True
            else:
                print("Deletion canceled")
                return False
    print(f"No book found with ISBN: {isbn}!")
    return False

#------------------------------------------------------------------------------------


# helper function to print all details about specific book
def print_book_details(book):
    """ Print details of a specific book """
    print("\n📖 Book Details:")
    for key, val in book.items():
        print(f"  {key:<10}: {val:<10}")
    print()


    # """Print book details in a readable format"""
    # print("\n📖 Book Details:")
    # print(f"  Title:       {book['Book Title']}")
    # print(f"  Author:      {book['Book Author']}")
    # print(f"  Price:       ${book['Book Price']}")
    # print(f"  Description: {book['Book Description']}")
    # print(f"  ISBN:        {book['Book ISBN']}")
    # print(f"  Category:    {book['Book Category']}\n")

#------------------------------------------------------------------------------------



import os

# todo save to file -> Mahmoud
#Input: none
#Output: return true if saved successfully, false if not
def save_to_file(library):
    try:
        with open("db.txt", "w") as file:
            for book in library:
                file.write(",".join([
                                book["Book Title"], 
                                book["Book Author"], 
                                str(book["Book Price"]),
                                book["Book Description"], 
                                book["Book ISBN"], 
                                book["Book Category"]
                            ]) + "\n")
        print("Library saved successfully.")
        return True
    except Exception as error:
        print(f"Error saving library: {error}")
        return False


#------------------------------------------------------------------------------------


# todo load from file -> Mahmoud
#Input: none
#Output: return true if loaded successfully, false if not
def load_from_file():
    if not os.path.exists("db.txt"):
        print("No saved library file found.")
        return False
    library.clear()
    try:
        with open("db.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 6:
                    book = {
                                "Book Title":           data[0], 
                                "Book Author":          data[1],
                                "Book Price" :          int(data[2]),
                                "Book Description":     data[3],
                                "Book ISBN":            data[4],
                                "Book Category":        data[5]
                            }
                    library.append(book)
        print("Library loaded successfully.")
        return True
    except Exception as e:
        print(f"Error loading library: {e}")
        return False