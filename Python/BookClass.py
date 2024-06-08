class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages 
    def __str__(self):
        return(self.title + " by " + self.author + ", " + str(self.pages) + " pages ")
    
title = input()
author = input()
pages = int(input())
book_obj = Book(title, author, pages)
print(book_obj)