#!/usr/bin/env python3

        
class Book:
    def __init__(self, title, page_count):
      
        self.title = title
        self._page_count = page_count
        self.current_page = 0

    @property
    def page_count(self):  
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
       
        self.current_page += 1
        print("Flipping the page...wow, you read fast!")
    
book = Book("Harry Potter", 315)

  