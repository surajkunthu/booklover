import pandas as pd

class BookLover:
    """
    Class for storing Books read and their ratings
    """
   
    def __init__(self, name, emails, fav_genre):
        self.name = str(name)
        self.emails = str(emails)
        self.fav_genre = str(fav_genre)
        self.num_books = 0
        self.book_list = pd.DataFrame({"book_name": [], "book_rating": []})   

    def add_book(self, book_name, rating):
        if (book_name in list(self.book_list["book_name"])):
            print("Book is already in the list!")
        else:
            new_book = pd.DataFrame({
                "book_name": [book_name],
                "book_rating": [int(rating)]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            self.num_books += 1
            
    def has_read(self, book_name):
        if (book_name in list(self.book_list["book_name"])):
            return True
        else:
            return False

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list["book_rating"] > 3.0]