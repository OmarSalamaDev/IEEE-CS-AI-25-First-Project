
from Book import Book

# List to store books added
library = []


# Generate ISBN (formatted as 10-digit number)
def generate_isbn(index):
    return str(index + 1).zfill(10)

# todo add_book() -> Ahmed
# Input: book details 
# Output: return true if book added successfully, false if not
def add_book(title, author, price, description, category):
    isbn = generate_isbn(len(library))  # Auto-generate ISBN
    book = Book(title, author, isbn, price, description, category)
    library.append(book)

    inserted = False # to check if there is an empty slot mid array
    for i in range(len(library)):
        if library[i] is None:  # Empty slot found
            library[i] = book
            inserted = True
            break
        
    # If no empty slots, append normally
    if not inserted:
        library.append(book)


    return True


#------------------------------------------------------------------------------------


# todo view books -> Ahmed
# Input: none
# Output: return a list of all books
def view_books():
    if not library:
        return False
    else:
        for book in library:
            print(book) 
        return True


#------------------------------------------------------------------------------------


# todo search book by title -> Ahmed
# Input: book title
# Output: return the book if found, otherwise return an empty list
def search_book_by_title(title):
    found_books = [book for book in library if book.get_title().lower() == title.lower()]
    return found_books 


#------------------------------------------------------------------------------------


# todo search book by isbn -> Ahmed
# Input: book isbn
# Output: return the book if found, otherwise return an empty list
def search_book_by_isbn(isbn):
    found_books = [book for book in library if book.get_isbn() == isbn]
    return found_books
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