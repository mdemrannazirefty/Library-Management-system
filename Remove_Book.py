def remove_book(library):
    if not library:
        print("No books available to remove.")
        return library
    
    removebook = int(input("Enter Book ID: "))
    for book in library:
        if str(book["Isbn"]) == str(removebook):
            library.remove(book)
            print("Book has been removed.")
            print()
            return library
        
    
    print("Book not found in the library.")
    print()
    return library
        
