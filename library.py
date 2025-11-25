# library.py
# Handles: Books, Members, Borrow, Return, File Save/Load, Analytics
# JSON + CSV VERSION

import json
import csv
import os
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

        self.load_data()  # load JSON + CSV

    # ---------------------------------------------------------
    # SAVE DATA (JSON + CSV)
    # ---------------------------------------------------------
    def save_data(self):
        try:
            # ---- SAVE BOOKS JSON ----
            with open("books.json", "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)

            # ---- SAVE MEMBERS JSON ----
            with open("members.json", "w") as f:
                json.dump([m.to_dict() for m in self.members], f, indent=4)

            # ---- SAVE BOOKS CSV ----
            with open("books.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["title", "author", "isbn", "available"])
                for b in self.books:
                    writer.writerow([b.title, b.author, b.isbn, b.available])

            # ---- SAVE MEMBERS CSV ----
            with open("members.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "member_id", "borrowed_books"])
                for m in self.members:
                    writer.writerow([m.name, m.member_id, ",".join(m.borrowed_books)])

        except Exception as e:
            print("❌ Error saving data:", e)

    # ---------------------------------------------------------
    # LOAD DATA (JSON + CSV)
    # ---------------------------------------------------------
    def load_data(self):
        try:
            # ---- LOAD BOOKS JSON ----
            if os.path.exists("books.json"):
                with open("books.json", "r") as f:
                    data = json.load(f)
                    self.books = [Book.from_dict(b) for b in data]

            # ---- LOAD MEMBERS JSON ----
            if os.path.exists("members.json"):
                with open("members.json", "r") as f:
                    data = json.load(f)
                    self.members = [Member.from_dict(m) for m in data]

        except Exception:
            print("⚠ Warning: JSON data corrupted. Skipping JSON load.")

        # CSV load will NOT override JSON; only loads if JSON missing
        try:
            # ---- LOAD BOOKS CSV ----
            if not self.books and os.path.exists("books.csv"):
                with open("books.csv", "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        self.books.append(
                            Book(row["title"], row["author"], row["isbn"], row["available"] == "True")
                        )

            # ---- LOAD MEMBERS CSV ----
            if not self.members and os.path.exists("members.csv"):
                with open("members.csv", "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        m = Member(row["name"], row["member_id"])
                        m.borrowed_books = row["borrowed_books"].split(",") if row["borrowed_books"] else []
                        self.members.append(m)

        except Exception:
            print("⚠ Warning: CSV data corrupted. Skipping CSV load.")

    # ---------------------------------------------------------
    # ADD BOOK + MEMBER
    # ---------------------------------------------------------
    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()

    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
        self.save_data()

    # ---------------------------------------------------------
    # FINDERS
    # ---------------------------------------------------------
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    # ---------------------------------------------------------
    # BORROW / RETURN
    # ---------------------------------------------------------
    def lend_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return False

        if member.borrow_book(book):
            self.save_data()
            return True
        return False

    def take_return(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return False

        if member.return_book(book):
            self.save_data()
            return True
        return False

    # ---------------------------------------------------------
    # ANALYTICS
    # ---------------------------------------------------------
    def analytics(self):
        borrowed_books = [b for b in self.books if not b.available]

        return f"""
Library Report
-------------------------
Total Members: {len(self.members)}
Books Currently Borrowed: {len(borrowed_books)}
Available Books: {len(self.books) - len(borrowed_books)}
"""
