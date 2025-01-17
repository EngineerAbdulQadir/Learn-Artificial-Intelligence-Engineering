class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False  # Book is not issued by default

    def issue(self):
        if not self.is_issued:
            self.is_issued = True
            print(f"The book '{self.title}' has been issued.")
        else:
            print(f"The book '{self.title}' is already issued.")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not issued.")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Issued: {self.is_issued}"


class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.books_issued = []  # List to store books issued by this member

    def issue_book(self, book: Book):
        if len(self.books_issued) < self.max_books_allowed():
            self.books_issued.append(book)
            book.issue()
        else:
            print(f"{self.name} cannot issue more than {self.max_books_allowed()} books.")

    def return_book(self, book: Book):
        if book in self.books_issued:
            self.books_issued.remove(book)
            book.return_book()
        else:
            print(f"{self.name} has not issued the book '{book.title}'.")

    def max_books_allowed(self):
        """To be overridden by subclasses (Student/Teacher)."""
        return 0

    def __str__(self):
        return f"Member Name: {self.name}, Member ID: {self.member_id}"


class Student(Member):
    def __init__(self, name: str, member_id: str):
        super().__init__(name, member_id)

    def max_books_allowed(self):
        return 3  # A student can issue up to 3 books

    def __str__(self):
        return f"Student Name: {self.name}, Student ID: {self.member_id}"


class Teacher(Member):
    def __init__(self, name: str, member_id: str):
        super().__init__(name, member_id)

    def max_books_allowed(self):
        return 5  # A teacher can issue up to 5 books

    def __str__(self):
        return f"Teacher Name: {self.name}, Teacher ID: {self.member_id}"


class Library:
    def __init__(self):
        # Use dictionaries for quick lookups
        self.books = {}    # key: ISBN,    value: Book object
        self.members = {}  # key: Member ID, value: Member object

    def add_book(self, book: Book):
        if book.isbn in self.books:
            print(f"Book with ISBN {book.isbn} already exists in the library.")
        else:
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn: str):
        if isbn in self.books:
            removed_book = self.books.pop(isbn)
            print(f"Book '{removed_book.title}' removed from the library.")
        else:
            print("No book found with ISBN:", isbn)

    def register_member(self, member: Member):
        if member.member_id in self.members:
            print(f"Member with ID {member.member_id} already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Member '{member.name}' registered in the library.")

    def get_book(self, isbn: str):
        return self.books.get(isbn, None)

    def get_member(self, member_id: str):
        return self.members.get(member_id, None)

    def list_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("===== All Books in Library =====")
            for book in self.books.values():
                print(book)

    def list_all_members(self):
        if not self.members:
            print("No members registered in the library.")
        else:
            print("===== All Registered Members =====")
            for member in self.members.values():
                print(member)


def main():
    library = Library()

    while True:
        print("\n======== Education Trust Nasra School - Library Management System ========")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Register a Student")
        print("4. Register a Teacher")
        print("5. Issue a book")
        print("6. Return a book")
        print("7. Show book details")
        print("8. Show member details")
        print("9. List all books")
        print("10. List all members")
        print("11. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Add a book
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)

        elif choice == "2":
            # Remove a book
            isbn = input("Enter ISBN of book to remove: ")
            library.remove_book(isbn)

        elif choice == "3":
            # Register a Student
            name = input("Enter student name: ")
            member_id = input("Enter student ID: ")
            new_student = Student(name, member_id)
            library.register_member(new_student)

        elif choice == "4":
            # Register a Teacher
            name = input("Enter teacher name: ")
            member_id = input("Enter teacher ID: ")
            new_teacher = Teacher(name, member_id)
            library.register_member(new_teacher)

        elif choice == "5":
            # Issue a book
            member_id = input("Enter Member ID: ")
            isbn = input("Enter ISBN of the book: ")

            member = library.get_member(member_id)
            book = library.get_book(isbn)

            if not member:
                print(f"No member found with ID: {member_id}")
                continue
            if not book:
                print(f"No book found with ISBN: {isbn}")
                continue

            member.issue_book(book)

        elif choice == "6":
            # Return a book
            member_id = input("Enter Member ID: ")
            isbn = input("Enter ISBN of the book: ")

            member = library.get_member(member_id)
            book = library.get_book(isbn)

            if not member:
                print(f"No member found with ID: {member_id}")
                continue
            if not book:
                print(f"No book found with ISBN: {isbn}")
                continue

            member.return_book(book)

        elif choice == "7":
            # Show book details
            isbn = input("Enter ISBN of the book: ")
            book = library.get_book(isbn)
            if book:
                print("=== Book Details ===")
                print(book)
            else:
                print("No book found with that ISBN.")

        elif choice == "8":
            # Show member details
            member_id = input("Enter Member ID: ")
            member = library.get_member(member_id)
            if member:
                print("=== Member Details ===")
                print(member)
                print("Books currently issued:")
                for b in member.books_issued:
                    print(f"  - {b.title} (ISBN: {b.isbn})")
            else:
                print("No member found with that ID.")

        elif choice == "9":
            # List all books
            library.list_all_books()

        elif choice == "10":
            # List all members
            library.list_all_members()

        elif choice == "11":
            print("Exiting the Education Trust Nasra School - Library Management System")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the main program if the script is executed
if __name__ == "__main__":
    main()