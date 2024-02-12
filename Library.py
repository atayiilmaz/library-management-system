import sys

class Library:
    def __init__(self):
        self.f = open("book.txt", "a+")
    
    def __del__(self):
        self.f.close()

    def listBooks(self):
        self.f.seek(0)
        data = self.f.read().splitlines()
        for book in data:
            bookName, author, *_ = book.split(',')
            print("Book:", bookName.strip(), "\tAuthor:", author.strip())

    def addBook(self):
        bookName = input("Enter book name: ")
        author = input("Enter author: ")
        releaseDate = input("Enter realease date: ")
        noOfPages = input("Enter page number: ")
        newBook = bookName + "," + author + "," + releaseDate + "," + noOfPages + "\n"
        self.f.write(newBook)
        print("Book added successfully!\n")

    def removeBook(self):
        getBookname = input("Enter the book name that you want to delete: ")
        self.f.seek(0)
        data = self.f.read().splitlines()
        for book in data:
            bookName, author, *_ = book.split(',')
            if bookName.strip() == getBookname:
                data.remove(book)
                self.f = open("book.txt", "w")
                for book in data:
                    self.f.write(book + "\n")
                print("Book removed successfully!\n")
        
while True:
    print("***MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4)Quit")
    option = input("\n Please select an option(1-4): ")
    lib = Library()

    if option == "1":
        lib.listBooks()
        del lib
    elif option == "2":
        lib.addBook()
        del lib
    elif option == "3":
        lib.removeBook()
        del lib
    elif option == "4":
        sys.exit()
    else:
        print("Wrong option")