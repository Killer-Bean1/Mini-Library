import json
import os

BOOK_FILE = "books.json"
MEMBER_FILE = "members.json"


# -------------------- DATA HANDLING --------------------

def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return {}


def save_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


# -------------------- BOOK FUNCTIONS --------------------

def add_book(books):
    isbn = input("Enter ISBN: ")
    if isbn in books:
        print("Book already exists.")
        return

    title = input("Enter title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    total_copies = int(input("Enter total copies: "))

    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }

    save_data(BOOK_FILE, books)
    print("Book added successfully.")


def search_book(books):
    keyword = input("Enter title or author to search: ").lower()
    found = False

    for isbn, info in books.items():
        if keyword in info["title"].lower() or keyword in info["author"].lower():
            print(f"ISBN: {isbn}")
            for key, value in info.items():
                print(f"  {key.title()}: {value}")
            print("-----------------------------")
            found = True

    if not found:
        print("No matching books found.")


def update_book(books):
    isbn = input("Enter ISBN of book to update: ")
    if isbn not in books:
        print("Book not found.")
        return

    print("Leave field empty if you do not want to change it.")

    new_title = input("New title: ")
    new_author = input("New author: ")
    new_genre = input("New genre: ")
    new_copies_input = input("New total copies: ")

    book = books[isbn]

    if new_title:
        book["title"] = new_title
    if new_author:
        book["author"] = new_author
    if new_genre:
        book["genre"] = new_genre

    if new_copies_input:
        new_total = int(new_copies_input)
        difference = new_total - book["total_copies"]
        book["total_copies"] = new_total
        book["available_copies"] += difference
        if book["available_copies"] < 0:
            book["available_copies"] = 0

    save_data(BOOK_FILE, books)
    print("Book updated successfully.")


def delete_book(books):
    isbn = input("Enter ISBN of book to delete: ")
    if isbn in books:
        del books[isbn]
        save_data(BOOK_FILE, books)
        print("Book deleted successfully.")
    else:
        print("Book not found.")


# -------------------- MEMBER FUNCTIONS --------------------

def add_member(members):
    member_id = input("Enter Member ID: ")
    if member_id in members:
        print("Member already exists.")
        return

    name = input("Enter member name: ")
    email = input("Enter email: ")

    members[member_id] = {
        "name": name,
        "email": email,
        "borrowed_books": []
    }

    save_data(MEMBER_FILE, members)
    print("Member added successfully.")


# -------------------- BORROW / RETURN --------------------

def borrow_book(books, members):
    member_id = input("Enter Member ID: ")
    if member_id not in members:
        print("Member not found.")
        return

    isbn = input("Enter ISBN of book to borrow: ")
    if isbn not in books:
        print("Book not found.")
        return

    if books[isbn]["available_copies"] > 0:
        books[isbn]["available_copies"] -= 1
        members[member_id]["borrowed_books"].append(isbn)

        save_data(BOOK_FILE, books)
        save_data(MEMBER_FILE, members)

        print("Book borrowed successfully.")
    else:
        print("No copies available.")


def return_book(books, members):
    member_id = input("Enter Member ID: ")
    if member_id not in members:
        print("Member not found.")
        return

    isbn = input("Enter ISBN of book to return: ")
    if isbn not in members[member_id]["borrowed_books"]:
        print("This book was not borrowed by this member.")
        return

    members[member_id]["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1

    save_data(BOOK_FILE, books)
    save_data(MEMBER_FILE, members)

    print("Book returned successfully.")


# -------------------- MAIN MENU --------------------

def main():
    books = load_data(BOOK_FILE)
    members = load_data(MEMBER_FILE)

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            add_member(members)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            update_book(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "6":
            borrow_book(books, members)
        elif choice == "7":
            return_book(books, members)
        elif choice == "8":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
