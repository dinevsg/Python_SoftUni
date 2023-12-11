from project.user import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {Steven King: [IT, Shades]}
        self.rented_books = {}     # {Tingo: {Konan: 1, Crabi: 2}}

    def get_book(self, author, book_name, days_to_return, user):

        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for data in self.rented_books.values():
            if book_name in data:
                return f"The book '{book_name}' is already rented and will be available in {data[book_name]} days!"

    def return_book(self, author, book_name, user):
        # if book_name in user.books: to try !
        if book_name not in self.rented_books[user.username]:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]


