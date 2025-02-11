
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
    return False


#------------------------------------------------------------------------------------


# todo delete book -> Mahmoud
# Input: book isbn
# Output: return true if book updated successfully, false if not
def delete_book(isbn):
    return False


#------------------------------------------------------------------------------------


# todo save to file -> Mahmoud
#Input: none
#Output: return true if saved successfully, false if not
def save_to_file():
    return False


#------------------------------------------------------------------------------------


# todo load from file -> Mahmoud
#Input: none
#Output: return true if loaded successfully, false if not
def load_from_file():
    return False