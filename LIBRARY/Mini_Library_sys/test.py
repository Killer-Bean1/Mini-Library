from operations import Library
def run_tests():
    lib = Library()

    # 1. Add book
    assert lib.add_book("001", "Python 101", "John Doe", "Fiction", 2) == "Book added successfully."
    assert "001" in lib.books

    # 2. Add member
    assert lib.add_member(1, "Alice", "alice@example.com") == "Member added successfully."
    assert 1 in lib.members

    # 3. Borrow book
    assert lib.borrow_book(1, "001") == "Book borrowed successfully."
    assert lib.books["001"].available_copies == 1

    # 4. Borrow when no copies left
    lib.borrow_book(1, "001")
    assert lib.borrow_book(1, "001") == "No copies available."

    # 5. Return book
    assert lib.return_book(1, "001") == "Book returned successfully."
    assert lib.books["001"].available_copies == 1

    print("OOP tests passed!")


if __name__ == "__main__":
    run_tests()