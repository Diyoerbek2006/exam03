from datetime import datetime

class Book:
    def __init__(self, id: int, title: str, author: str, pages: int):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("id musbat butun son bo'lishi kerak")
        if not title.strip():
            raise ValueError("title bo'sh bo'lishi mumkin emas")
        if not author.strip():
            raise ValueError("author bo'sh bo'lishi mumkin emas")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("pages 0 dan katta bo'lishi kerak")

        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False
        self.borrower = None
        self.borrow_history = []
        self.archived = False

    def borrow(self, user: str) -> None:
        if self.archived:
            raise RuntimeError("Kitob arxivlangan va olinmaydi")
        if self.is_borrowed:
            raise RuntimeError("Kitob allaqachon olingan")
        self.is_borrowed = True
        self.borrower = user
        self.borrow_history.append((user, datetime.now()))

    def return_book(self) -> None:
        if not self.is_borrowed:
            raise RuntimeError("Kitob olinmagan")
        self.is_borrowed = False
        self.borrower = None

    def change_title(self, new_title: str) -> None:
        if not new_title.strip():
            raise ValueError("Yangi nom bo'sh bo'lishi mumkin emas")
        if self.archived:
            raise RuntimeError("Arxivlangan kitob nomini o'zgartirib bo'lmaydi")
        self.title = new_title

    def archive(self) -> None:
        if self.is_borrowed:
            raise RuntimeError("Olingan kitobni arxivlab bo'lmaydi")
        self.archived = True

    def info(self) -> dict:
        if self.archived:
            status = "archived"
        elif self.is_borrowed:
            status = "borrowed"
        else:
            status = "available"

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "status": status,
            "borrower": self.borrower,
            "times_borrowed": len(self.borrow_history)
        }

    def __str__(self):
        return f"<Book {self.title}>"

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', borrowed={self.is_borrowed})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.id == other.id

    def __len__(self):
        return self.pages

    def __bool__(self):
        return not self.archived
