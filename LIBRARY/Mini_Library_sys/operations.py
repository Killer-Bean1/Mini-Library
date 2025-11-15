class Book:
    def __init__(self, isbn, title, author, genre, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies <= 0:
            return "No copies available."
        self.available_copies -= 1
        return "Book borrowed successfully."

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return "Book returned successfully."
        return "All copies are already returned."


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, isbn):
        if len(self.borrowed_books) >= 3:
            return "Borrow limit reached (3 books)."
        self.borrowed_books.append(isbn)
        return "Book added to borrowed list."

    def return_book(self, isbn):
        if isbn not in self.borrowed_books:
            return "Book not borrowed by this member."
        self.borrowed_books.remove(isbn)
        return "Book removed from borrowed list."


class Library:  
    VALID_GENRES = ("Fiction", "Non-Fiction", "Sci-Fi")

    def __init__(self):
        self.books = {}       # {isbn: Book}
        self.members = {}     # {member_id: Member}

    # --- BOOK METHODS ---
    def add_book(self, isbn, title, author, genre, total_copies):
        if isbn in self.books:
            return "Book already exists."
        if genre not in Library.VALID_GENRES:
            return "Invalid genre."
        self.books[isbn] = Book(isbn, title, author, genre, total_copies)
        return "Book added successfully."

    def search_books(self, keyword):
        results = []
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append((book.isbn, book.title, book.author))
        return results

    def update_book(self, isbn, title=None, author=None, total_copies=None):
        if isbn not in self.books:
            return "Book not found."
        book = self.books[isbn]
        if title:
            book.title = title
        if author:
            book.author = author
        if total_copies is not None:
            diff = total_copies - book.total_copies
            book.total_copies = total_copies
            book.available_copies += diff
        return "Book updated successfully."

    def delete_book(self, isbn):
        if isbn not in self.books:
            return "Book not found."
        for member in self.members.values():
            if isbn in member.borrowed_books:
                return "Cannot delete. Book is borrowed."
        del self.books[isbn]
        return "Book deleted successfully."

    # --- MEMBER METHODS ---
    def add_member(self, member_id, name, email):
        if member_id in self.members:
            return "Member already exists."
        self.members[member_id] = Member(member_id, name, email)
        return "Member added successfully."

    def update_member(self, member_id, name=None, email=None):
        if member_id not in self.members:
            return "Member not found."
        member = self.members[member_id]
        if name:
            member.name = name
        if email:
            member.email = email
        return "Member updated successfully."

    def delete_member(self, member_id):
        if member_id not in self.members:
            return "Member not found."
        member = self.members[member_id]
        if member.borrowed_books:
            return "Cannot delete. Member has borrowed books."
        del self.members[member_id]
        return "Member deleted successfully."

    # --- BORROW & RETURN ---
    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            return "Member not found."
        if isbn not in self.books:
            return "Book not found."

        member = self.members[member_id]
        book = self.books[isbn]

        if len(member.borrowed_books) >= 3:
            return "Borrow limit reached (3 books)."
        if book.available_copies <= 0:
            return "No copies available."

        member.borrow_book(isbn)
        result = book.borrow()
        if result == "Book borrowed successfully.":  # Check if borrow was successful
            return "Book borrowed successfully."
        return result

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            return "Member not found."
        if isbn not in self.books:
            return "Book not found."

        member = self.members[member_id]
        book = self.books[isbn]

        if isbn not in member.borrowed_books:
            return "Book not borrowed by this member."

        member.return_book(isbn)
        book.return_book()
        return "Book returned successfully."


# Demo code (optional)
if __name__ == "__main__":
    from operations import Library  # This will work now
    print("\n--- DEMO: Library Management System ---")

    # Add books
    library = Library()
    print(library.add_book("001", "Python 101", "John Doe", "Fiction", 2))
    print(library.add_book("002", "AI Basics", "Jane Smith", "Non-Fiction", 1))

    # Add members
    print(library.add_member(1, "Alice", "alice@example.com"))
    print(library.add_member(2, "Bob", "bob@example.com"))

    # Search
    print("\nSearch results for 'Python':", library.search_books("Python"))

    # Borrow/Return
    print(library.borrow_book(1, "001"))
    print(library.borrow_book(2, "001"))
    print(library.borrow_book(2, "001"))  

    print(library.return_book(1, "001"))
    print(library.borrow_book(2, "001"))  

    # Delete
    print(library.delete_book("002"))
    print(library.delete_member(2))