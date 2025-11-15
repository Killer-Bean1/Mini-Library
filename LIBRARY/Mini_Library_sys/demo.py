import operations  

print("\n--- DEMO: Library Management System ---")

# Add books
library = operations.Library()
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