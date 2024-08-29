'''   
Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.
'''


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]  


def add_book(list): 
    try:     
        while True:  # loop to ask user if they want to add anything to library
            choice = input("Would you like to add a book to the library? (yes or no) ")  
            if choice.upper() == 'YES':  # if user enters yes 
                while True: # new loop to add books 
                    new_title = input("What is the title of the book you wish to add?")   # ask user to enter title of book to add 
                    new_author = input("Who is this book written by?")    # ask user to enter name of author of new book to add 
                    new_book = (new_title, new_author)  # create tuple with new title and author
                    if new_book in list: 
                        print(f"Sorry, looks like '{new_title}' by {new_author} is already in your library.")  # if given Title and Author are already in list, break loop 
                        break 
                    else:  # else if title and author are not in list 
                        library.append(new_book)  # add the tuple to our library list
                        print(f"'{new_title}' by {new_author} was added to your library!")   # let user know that it was added 
                        break   # break the loop, and ask user if they wish to add another book
            elif choice.upper() == 'NO':   # if they don't want to add a book 
                print("Very well! This is your current library: ") 
                for index, shelf in enumerate(library): # print out current library
                    print(f"'{shelf[0]}' by {shelf[1]}")
                break
            else:
                print("I'm sorry, but you'll need to enter either yes or no.")   # if neither yes or no is entered, tell user to enter yes or no until one is entered 
    except Exception as e: 
        print("Unexpected Error Occured.") 
        
        
add_book(library)
