from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
#Functions I might need: print(), 'for' loop,
#Only print availiable, title, author, and ID
#Input: ID or Availibility
#Output: Avaliable books
#According to level 5, books are dictionaries for the first 4 levels

def check_if_available():
    for books in library_books: #Checks for each book
        
        title = books["title"]
        author = books["author"]
        id = books["id"]
        available = books["available"]
        if available == True: #Only true gets printed
            print(F"{title} by {author}, {id}, Available") #Available doesn't need to be printed because all of them are available
        else: # All False gets ignored
            pass


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
#IF ElIF and .lower functions for sorting
#Same function for lvl1's avalibility with lvl 2's author and genre
#input() so user can search up author.

def search_by_author(): #Level two is basically copy and paste from level 1, just with a few changes.
    user_search = input("What author would you like to search for? ")
    low_user_search = user_search.lower() #makes user's input all lowercase
    for books in library_books: #Checks for each book
        
        title = books["title"]
        author = books["author"]
        lower_author = author.lower() #makes author input all lower. If only user was lower, only the
        id = books["id"]
        available = books["available"]
        if low_user_search == lower_author: #Checks for matches
            print(f"{title} by {author}, {id}, {available}") 
        else: # All non-author gets ignored
            pass

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
#datetime will be needed
#Else, error message

def checkout():
    user_checkout = input("Input the ID of the book if you want to check it out: ") #Asks user to input book to checkout
    upper_user_checkout = user_checkout.upper() #To make it case insensitive
    for books in library_books: #checks for each book
        available = books["available"] #different variables used here because the others were not needed
        id = books["id"]
        upper_id = id.upper()
        due_date = books ["due_date"]
        if upper_user_checkout == upper_id:
            if available == True:
                print("You have successfully checked out this book for")
                due_date = timedelta(0,0,0,0,0,0,2) # The last number is ammount of weeks
                available = False # Removes avalibility
                print(due_date)
            else:
                print("This book is unavailable")

        else:
            pass

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
#Use lvl 3's function but reverse
#Only halfway done

def return_book():
    user_return = input("Input the ID of the book if you want to return out: ") #Asks user to input book to return
    upper_user_return = user_return.upper() #To make it case insensitive
    for books in library_books: #checks for each book
        available = books["available"] #different variables used here because the others were not needed
        id = books["id"]
        upper_id = id.upper()
        due_date = books ["due_date"]
        if upper_user_return == upper_id: # b7 works as B7
            if available == False:
                print("You have successfully returned this book.")
                due_date = None
                available = True
            else:
                print("This book is already returned")

        else:
            pass

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# Will need: 'while' loop and input()


# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    #check_if_available()
    #search_by_author()
    #checkout()
    #return_book() I didn't finish level 4
    pass