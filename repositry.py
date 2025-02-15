from Book import Book
import os


# List to store books added
library: list[Book] = []


# Generate ISBN (formatted as 10-digit number)
def generate_isbn(index):
    return str(index + 1).zfill(10)


# Input: book details 
# Output: return true if book added successfully, false if not
def add_book(title, author, price, description, category, publisher):
    isbn = generate_isbn(len(library))  # Auto-generate ISBN
    book = Book(title, author, isbn, price, description, category, publisher)

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


# Input: none
# Output: return a list of all books
def view_books():
    return library


#------------------------------------------------------------------------------------


# Input: book title
# Output: return the book if found, otherwise return an empty list
def search_book_by_title(title):
    if not title.strip():
        return []
    title = title.lower()
    return [book for book in library if title == book.title.lower()]



#------------------------------------------------------------------------------------


# Input: book isbn
# Output: return the book if found, otherwise return an empty list
def search_book_by_isbn(isbn):
    found_books = [book for book in library if book.isbn == isbn]
    return found_books


#------------------------------------------------------------------------------------


# Input: book isbn
# Output: return true if book updated successfully, false if not
def update_book(isbn):
    for book in library:
        if book["Book ISBN"] == isbn:
            updates = update_helper_function(book)
            for key, value in updates.items():
                book[key] = value
            print("Book updated succefully.")
            # print book details after update
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


# Input: book isbn
# Output: return true if book updated successfully, false if not
def delete_book(isbn):
    book = search_book_by_isbn(isbn)
    if book == []:
        return False
    
    library.remove(book[0])
    save_to_file()
    return True


#------------------------------------------------------------------------------------


#Input: none
#Output: return true if saved successfully, false if not
def save_to_file():
    try:
        with open("db.txt", "w") as file:
            for book in library:
                file.write(",".join([
                                    book.title, 
                                    book.author, 
                                    str(book.price),
                                    book.description, 
                                    book.isbn, 
                                    book.category,
                                    book.publisher
                                ])
                                + "\n"
                )
        print("Library saved successfully.")
        return True
    except Exception as error:
        print(f"Error saving library: {error}")
        return False


#------------------------------------------------------------------------------------


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
                if len(data) == 7:
                    book = Book(
                                data[0], 
                                data[1],
                                int(data[2]),
                                data[3],
                                data[4],
                                data[5],
                                data[6]
                    )
                    library.append(book)
        print("Library loaded successfully.")
        return True
    except Exception as e:
        print(f"Error loading library: {e}")
        return False