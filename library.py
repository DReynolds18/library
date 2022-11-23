# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:56:54 2022

@author: dreynolds18

Set up a Class Object that keeps track of you books:

book title,

book author,

book length

genre (can be added)

how many books in each genre

book set 
"""

class Book:
    
    def __init__ (self, name):
        self._name = name
        
    def printName (self):
        print(self._name)
        
    def getDictionary(self, dictName):
        self._dict = dictName
        
    def printAllBooks(self):
        keys = self._dict.keys()
        for key in keys:
            x = self._dict[key]
            print(key, x)
        
    def add_book(self, title, author, pages, genre, series):
        self._dict[title] = [author, pages, genre, series]
        
    def print_bookInfo(self, title):
        if title in self._dict.keys():
            print(self._dict[title])
        else:
            print("No book in library")
    
    def howManyGenre(self, genre):
        tempValue = 0
        keys = self._dict.keys()
        
        for key in keys:
            x = self._dict[key]
            if x[2] == genre:
                tempValue += 1
            
        return tempValue
            
#####################################################################     
  
if __name__ == '__main__':
    
    #sets up dictionary called library
    library = {'Harry Potter and the Sorcerers Stone': ['J.K. Rowling', '320', 'Fantasy', 'Harry Potter'],}
    
    #sets up the name of the iteration
    dylanBooks = Book('Dylans Books')
    
    #prints the name of the iteration
    print("Name of iteration:")
    dylanBooks.printName()
    
    #sets up the name of the dictionary
    dylanBooks.getDictionary(library)
    
    #Prints all the books before adding the new books
    print("Library with one book:")
    dylanBooks.printAllBooks()
    
    #adds new books to dictionary
    dylanBooks.add_book('Harry Potter and the Chamber of Secrets', 'J.K. Rowling', '341', 'Fantasy', 'Harry Potter')
    
    #Prints only the info for both books and shows that if user types a book that isnt it will print a error
    print("Info of both books:")
    dylanBooks.print_bookInfo('Harry Potter and the Sorcerers Stone')
    dylanBooks.print_bookInfo('Harry Potter and the Chamber of Secrets')
    dylanBooks.print_bookInfo('Ultimate Cheat Code Guide 2018')
    
    #caculates and prints the number of fantasy books in the library
    numOfFantasyFiction = dylanBooks.howManyGenre("Fantasy")
    print(f'The number of Fantasy Books is {numOfFantasyFiction}')
    
    #shows the newest dictionary with both books
    print("Library with two books:")
    dylanBooks.printAllBooks()