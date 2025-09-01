# This is a basic Book class with title and author attributes
class Book:
    def __init__(self, title, author):
        # Initialize the book's title and author
        self.title = title
        self.author = author
    
    def info(self):
        # Return a string describing the book
        return f"'{self.title}' by {self.author}"

# LibraryBook class inherits from Book and adds checkout status
class LibraryBook(Book):
    def __init__(self, title, author):
        # Initialize title and author using the base class constructor
        super().__init__(title, author)
        # Track whether the book is checked out; initially False
        self.checked_out = False
    
    def check_out(self):
        # If the book is not checked out, mark it as checked out
        if not self.checked_out:
            self.checked_out = True
            print(f"Checked out '{self.title}'")
        else:
            # Inform if the book is already checked out
            print(f"'{self.title}' is already checked out")
    
    def return_book(self):
        # If the book is checked out, mark it as returned (not checked out)
        if self.checked_out:
            self.checked_out = False
            print(f"Returned '{self.title}'")
        else:
            # Inform if the book wasn't checked out but a return was attempted
            print(f"'{self.title}' was not checked out")
    
    def info(self):
        # Get the basic book info from the parent class
        base_info = super().info()
        # Add the current status (checked out or available)
        status = "Checked out" if self.checked_out else "Available"
        # Return combined information string
        return f"{base_info} - Status: {status}"



# Example of usage of the classes

# Create a library book instance (inherits from Book)
library_book = LibraryBook("Computer Literacy Book", "Joseph Ajireloja")

# Print information about the library book (initially available)
print(library_book.info())

# Check out the library book (change its status)
library_book.check_out()

# Print updated info showing the book is checked out
print(library_book.info())

# Return the library book (change status back)
library_book.return_book()

# Print updated info showing the book is available again
print(library_book.info())