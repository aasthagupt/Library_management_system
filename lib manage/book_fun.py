import json
from book import Book 

def print_options():
    print("press the button for the action")
    print("1-create a new book")
    print("2-save book")
    print("3-load books from the disk")
    print("4-issue book")
    print("5- return a book")
    print("6-update a book")
    print("show all books")
    print("8-show book")

def input_book_info():
    id=input("ID:")
    name=input("Name:")
    description=input("description: ")
    isbn=input("ISBN:")
    page_count=int(input("page count: "))
    issued=input("issued :y/Y for true, anything else for false")
    author=input("author name:")
    year=int(input("Year"))
    return {
        'id':id,'name':name,'description':description,'isbn':isbn,'page_count':page_count,
        'issued':issued,'author':author,'year':year}
    

def create_book():
    print("please enter your book information")
    book_input=input_book_info()
    book=Book(book_input['id'],book_input['name'],book_input['description'],book_input['page_count'],book_input['issued'],book_input['author'],book_input['year'])
    print(book.to_dict())
    return book

def save_book(books):
    json_books=[]   
    for book in books:
        json_books.append(book.to_dict())
    try:
        file=open("book.dat","w")
        file.write(json.dumps(json_books,indent=4))#converts into string
    except:
        print("we had an error in saving books")

def load_books():
    try:
        file=open("books.dat",'r')
        loaded_books=json.loads(file.read())
        books=[]
        for book in loaded_books:
            new_obj=Book(book['id'],book['name'],book['description'],book['page_count'],book['issued'],book['author'],book['year'])
            books.append(new_obj)
    except:
        print("the file doesn't exist")


