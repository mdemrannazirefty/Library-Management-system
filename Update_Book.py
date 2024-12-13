def update_book(library):
    if library is None or not library: 
        print("The library is empty. No book to update.")
        return library

    updatebook = int(input("Enter Book ID to Update: "))
    
    for book in library:
        if book['Isbn'] == updatebook:  
            print("\nBook Found")
            print("Current Book Details:")
            print(f"Title: {book['Title']}")
            print(f"Author Name: {book['Author']}")
            print(f"ID NO: {book['Isbn']}")
            print(f"Published Year: {book['Year']}")
            print(f"Price: {book['Price']}")
            print(f"Quantity: {book['Quantity']}")
            
            book['Title'] = input("Enter New Title: ") or book['Title']
            book['Authorn'] = input("Enter New Author Name: ") or book['Author']
            book['Year'] = input("Enter New Published Year: ") or book['Year']
            book['Price'] = float(input("Enter New Price: ") or book['Price'])
            book['Quantity'] = int(input("Enter New Quantity: ") or book['Quantity'])

            print("Book Updated")
            print()
            return library

    print("Book Not Found")
    return library
