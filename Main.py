
from library import Library
import uuid

# --------------------------------------------------------
# DISPLAY MENU
# --------------------------------------------------------
def display_menu():
    print("\n=============================================")
    print("    WELCOME TO KRMU INVENTORY SYSTEM MENU")
    print("=============================================")
    print("1. Add New Book")
    print("2. Register New Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Library Report")
    print("6. Save All Data (JSON + CSV)")
    print("8. View All Books")
    print("9. View All Members")
    print("10. Exit")
    print("---------------------------------------------")

# --------------------------------------------------------
# ADD BOOK
# --------------------------------------------------------
def add_book_menu(library):
    print("\n--- Add New Book ---")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    isbn = input("Enter Book ISBN: ")
    library.add_book(title, author, isbn)
    print("✔ Book Added Successfully!")

# --------------------------------------------------------
# REGISTER MEMBER
# --------------------------------------------------------
def register_member_menu(library):
    print("\n--- Register New Member ---")
    name = input("Enter Member Name: ")
    member_id = str(uuid.uuid4())[:8]   # auto ID
    library.register_member(name, member_id)
    print(f"✔ Member Registered! Member ID = {member_id}")

# --------------------------------------------------------
# BORROW BOOK
# --------------------------------------------------------
def borrow_book_menu(library):
    print("\n--- Borrow Book ---")
    member_id = input("Enter Member ID: ")
    isbn = input("Enter Book ISBN: ")
    if library.lend_book(member_id, isbn):
        print("✔ Book Borrowed!")
    else:
        print("❌ Borrow Failed (Invalid ID or Book not available).")

# --------------------------------------------------------
# RETURN BOOK
# --------------------------------------------------------
def return_book_menu(library):
    print("\n--- Return Book ---")
    member_id = input("Enter Member ID: ")
    isbn = input("Enter Book ISBN: ")
    if library.take_return(member_id, isbn):
        print("✔ Book Returned!")
    else:
        print("❌ Return Failed.")

# --------------------------------------------------------
# VIEW ALL BOOKS
# --------------------------------------------------------
def view_all_books(library):
    print("\n--- All Books ---")
    if not library.books:
        print("No books available.")
        return

    for b in library.books:
        print(f"{b.title} | {b.author} | ISBN:{b.isbn} | Available:{b.available}")

# --------------------------------------------------------
# VIEW ALL MEMBERS
# --------------------------------------------------------
def view_all_members(library):
    print("\n--- All Members ---")
    if not library.members:
        print("No members registered.")
        return

    for m in library.members:
        print(f"{m.name} | ID:{m.member_id} | Borrowed:{m.borrowed_books}")

# --------------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------------
def main():
    print("=" * 50)
    print("        WELCOME TO KRM LIBRARY SYSTEM")
    print("=" * 50)

    library = Library()   # load JSON + CSV automatically
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            add_book_menu(library)

        elif choice == '2':
            register_member_menu(library)

        elif choice == '3':
            borrow_book_menu(library)

        elif choice == '4':
            return_book_menu(library)

        elif choice == '5':
            print(library.analytics())

        elif choice == '6':
            library.save_data()
            print("💾 Data Saved Successfully (JSON + CSV)!")

        elif choice == '7':
            library.load_data()
            print("📂 Data Loaded Successfully (JSON + CSV)!")

        elif choice == '8':
            view_all_books(library)

        elif choice == '9':
            view_all_members(library)

        elif choice == '10':
            print("\nThank you for using the Library System. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 10.")

# --------------------------------------------------------
if __name__ == "__main__":
    main()
