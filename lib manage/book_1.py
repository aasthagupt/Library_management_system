import book_fun
import os
book_fun.print_options()
option = input()
books=[]
while option!='X' and option !='x':
    if option =='1':
        books.append(book_fun.create_book())
        book_fun.create_book()
        input("command executed... press any button to continue")
    elif option=='2':
        book_fun.save_book(books)
    elif option=='3':
        books=book_fun.load_books()
    elif option=='4':
        book_fun.find_book(books,"12")
    elif option=='5':
        book_fun.issue_book(books)
    elif option=='6':
        book_fun.return_book(books)
    else:
        print("the given command doesn't exsits")
    input("press enter to continuee....")
    os.system("cls")
    book_fun.print_options()
    option=input()
