import unittest
from booklover.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    global test_object 
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object.add_book("War of the Worlds", 4)
         
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object.add_book("War of the Worlds", 4)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object.has_read("War of the Worlds")
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        self.assertFalse(test_object.has_read("Tom Sawyer"))

    def test_5_num_books_read(self): 
        expected = 5
        # add some books to the list, and test num_books matches expected.
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)
        self.assertEqual(test_object.num_books, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object.add_book("The Hobbit", 2)
        test_object.add_book("Lord of the Rings", 7)
        test_object.add_book("The Count of Monte Cristo", 8)
        test_object.add_book("Harry Potter 1-7", 8)
        test_object.add_book("The Fountainhead", 1)
        test_object.fav_books()

if __name__ == '__main__':
    unittest.main(verbosity=3)