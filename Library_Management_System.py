## Library Management System CLI
from Add_Book import add_book
from Remove_Book import remove_book
from Save_Books import Save_Books
from Update_Book import update_book
from Search_Book import search_book
from Load_Books import load_books
from View_All_Books import view_all_books

print("***** Welcome To Libary Management System *****")

library=load_books()

while True:
    print("@ Select any Option")
    print("1.Add Book")
    print("2.Remove Book")
    print("3.Search Book")
    print("4.Update Book")
    print("5.View All Books")
    print("6.Exit")

    option = int(input("- Enter your Option: "))
    
    if option==1:
        library=add_book(library)
    elif option==2:
        library=remove_book(library)
    elif option==3:
        library=search_book(library)
    elif option==4:
        library= update_book(library)
    elif option==5:
        view_all_books(library)
    elif option==6:
        Save_Books(library) 
        print("Thanks for using Library Management System")
        print()
        break
    else:
        print("Invalid Option")
