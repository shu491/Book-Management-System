from os import system, name

file_name = 'books_23099740.txt'
books_data = []  # set books_data as an empty list

ASCII_ART = '''
                                                      ______ ______
                                                    _/      Y      \\_
                                                   //  Mala | tang  \\\\
                                                  //  Book  | System \\\\
                                                 //________.|.________\\\\
                                                `----------`-'----------'
'''


def clear():
    # Check if the name of the operating system is 'nt' for Windows
    if name == 'nt':
        # use system command 'cls' to clear the console screen
        _ = system('cls')
    else:
        # if not Windows, use system command 'clear' to clear the terminal screen
        _ = system('clear')


def read_books_from_file(file_name):  # define a function to read book information from a file
    with open(file_name, 'r') as file:  # read the txt file as a string
        for line in file:  # iterate through each line in the file
            book_info = line.strip().split(',')  # Split each line from the file into a list
            if len(book_info) == 8:  # check if the length of book_info is 8
                books_data.append({  # append book_info to books_data
                    'ISBN': book_info[0],
                    'Author': book_info[1],
                    'Title': book_info[2],
                    'Publisher': book_info[3],
                    'Genre': book_info[4],
                    'Year Published': book_info[5],
                    'Date Purchased': book_info[6],
                    'Status': book_info[7]})
            else:
                print('There is an issue with data format in line')


def add_book():
    from datetime import datetime
    # collect information for a book
    try:
        # exception handling for ISBN
        while True:
            try:
                #  input data
                isbn = input("Enter ISBN of the book:")
                # input must not be empty
                if not isbn:
                    raise ValueError("ISBN cannot be empty :)")
                # input must be 10-13 digits long
                elif not (10 <= len(isbn) <= 13 and isbn.isdigit()):
                    raise ValueError("ISBN should contain 10-13 numeric digits.")
                break
            except ValueError as e:
                print(f"{e}\nPlease enter a valid input.")

        # exception handling for author input
        while True:
            try:
                author = input("Enter author of the book:")
                if not author.strip():  # Check if the name is empty or contains only whitespace
                    raise ValueError("Author cannot be empty :)")
                # Allows space within the name
                elif not author.replace(" ", "").isalpha():
                    raise ValueError("Enter only alphabets.")
                break
            except ValueError as e:
                print(f"{e}\nPlease enter a valid input.")

        # exception handling for title input
        while True:
            try:
                title = input("Enter title of the book:")
                if not title:
                    raise ValueError("Title cannot be empty :)")
                break
            except ValueError as e:
                print(f"{e}\nPlease enter a valid input.")

        # exception handling for publisher
        while True:
            try:
                publisher = input("Enter name of publisher of the book:")
                if not publisher:
                    raise ValueError("Name of publisher cannot be empty :)")
                break
            except ValueError as e:
                print(f"{e}\nPlease enter a valid input.")

        # exception handling for genre
        while True:
            try:
                genre = input("Enter genre of the book:")
                if not genre:
                    raise ValueError("Genre cannot be empty :)")
                # Only alphabets are allowed
                elif genre.isdigit():
                    raise ValueError("Enter only alphabets.")
                break
            except ValueError as e:
                print(f"{e}\nPlease enter a valid input.")

        # exception handling for year published
        while True:
            try:
                year = input("Enter the Year Published of the book: ")
                if not year:
                    raise ValueError("Year published cannot be empty:) ")
                elif not year.isdigit():
                    raise ValueError('Year published must contain only numeric digits')
                year_input = int(year)
                # only 4 digits allowed, and can only enter years until 2023
                if not (1000 <= year_input <= 2023):
                    raise ValueError(
                        "Year published must contain only 4 digits and must be published before 2024.")
                break
            except ValueError as e:
                print(f"{e}\nPlease enter a valid input.")

        # exception handling for date purchased
        while True:
            try:
                date = input(
                    "Enter the Date Purchased(DD-MM-YYYY): ")
                if not date:
                    raise ValueError("Date Purchased cannot be empty :)")

                date_purchased = datetime.strptime(date, "%d-%m-%Y")
                year_purchased = date_purchased.year

                # Checks if date purchased is after year published
                if year_input > year_purchased:
                    raise ValueError("Date purchased cannot be earlier than year published")

                if not (1000 <= year_purchased <= 2023):
                    raise ValueError(
                        "Year published must not be in future.")

                # ensures input is between 8-10 digits(including -)
                elif not 8 <= len(date) <= 10:
                    raise ValueError("Invalid input length")
                break
            except ValueError as e:
                if "does not match format '%d-%m-%Y'" in str(e):
                    print("Incorrect format. Please enter the date in DD-MM-YYYY format.")

                elif "unconverted data remains" in str(e):  # to solve the output of unconverted data
                    print("Please enter a valid date in DD-MM-YYYY format.")

                else:
                    print(f"{e}\nPlease enter a valid input.")
        # exception handling for status input
        while True:
            status = input("Enter the Status of the book: ").strip().lower()
            if status == 'read' or status == 'to-read':
                break
            else:
                print('Please enter only "read" or "to-read".')
    except ValueError as e:
        print(f"{e}Please enter a valid input.")

    books_data.append(
        {'ISBN': isbn, 'Author': author, 'Title': title, 'Publisher': publisher, 'Genre': genre,
         'Year Published': year, 'Date Purchased': date, 'Status': status})
    print("Books added successfully!")


def add_continue():
    while True:
        choice_to_continue = input("Do you want to continue? (yes/no): ").lower()
        if choice_to_continue == 'no':
            clear()
            print("Exiting Add Book Records system. Thank you.")
            break
        elif choice_to_continue == 'yes':
            add_book()
        elif choice_to_continue != 'yes':
            print("Invalid input! Please enter 'yes' or 'no'")


def delete_book():
    try:
        while True:
            try:
                delete = input("Enter ISBN, author, or title to delete('cancel' to quit): ").lower()
                if delete == 'cancel':
                    print("Exiting...")
                    main()
                elif not delete:
                    raise ValueError("Books to be deleted cannot be empty!")
            except ValueError as e:
                print(f'{e}\nPlease enter a valid input.')
            # Continues if input is valid
            matching_books = []
            for book in books_data:
                # Check if the search criteria matches the ISBN, author, or title of any book
                isbn_match = delete == book['ISBN'].lower()
                author_match = delete == book['Author'].lower()
                title_match = delete == book['Title'].lower()

                if isbn_match or author_match or title_match:
                    matching_books.append(book)
                    print(matching_books)
            if matching_books:
                for book in matching_books:
                    # Display matching books and ask for confirmation to delete
                    print("\nMatching Book(s) to Delete:")
                    print(f"{'ISBN':<15}: {book['ISBN']}")
                    print(f"{'Author':<15}: {book['Author']}")
                    print(f"{'Title':<15}: {book['Title']}")
                    print(f"{'Publisher':<15}: {book['Publisher']}")
                    print(f"{'Genre':<15}: {book['Genre']}")
                    print(f"{'Year Published':<15}: {book['Year Published']}")
                    print(f"{'Date Purchased':<15}: {book['Date Purchased']}")
                    print(f"{'Status':<15}: {book['Status']}")

                while True:
                    confirm_delete = input("Do you want to delete the above book(s)? (yes/no): ").lower()

                    if confirm_delete == 'yes':
                        # Remove matching books from the 'books' list
                        for book in matching_books:
                            books_data.remove(book)
                        print("Book(s) deleted successfully!")
                        return
                    elif confirm_delete == 'no':
                        # Cancel deletion
                        print("Deletion cancelled.")
                        return
                    else:
                        print("Please enter 'yes' or 'no.")

            elif delete:
                print("No matching books found.")

    except ValueError as e:
        print(f"Error. {e}")


def delete_continue():
    while True:
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice == 'yes':
            clear()
            delete_book()  # Continue the outer loop
        elif choice == 'no':
            clear()
            print("Exiting Delete System. Thank you")
            break  # stops execution of the search function, terminate the program
        else:
            print("Invalid input! Please enter 'yes' or 'no'")


def update_book():  # updating book information
    print("\nUpdate/Edit Book Record(s)")
    while True:
        # Ask user to input ISBN/Author/Title
        keywords = input("Enter ISBN/Author/Title of a book: ").lower()
        matching_found = False

        for book in books_data:  # to check whether the matching record have found
            if keywords.lower().replace(" ", "") in [book['ISBN'].lower().replace(" ", ""),
                                                     book['Author'].lower().replace(" ", ""),
                                                     book['Title'].lower().replace(" ", "")]:
                matching_found = True

                # Print the current book information
                print("\nCurrent Book Information: ")
                print(f"{'ISBN':<15} : {book['ISBN']}")
                print(f"{'Author':<15} : {book['Author']}")
                print(f"{'Title':<15} : {book['Title']}")
                print(f"{'Publisher':<15} : {book['Publisher']}")
                print(f"{'Genre':<15} : {book['Genre']}")
                print(f"{'Year Published':<15} : {book['Year Published']}")
                print(f"{'Date Purchased':<15} : {book['Date Purchased']}")
                print(f"{'Status':<15} : {book['Status']}")

                while True:  # Confirmation by user to update/edit the information
                    confirm_updating = input("Do you want to update/edit this book? (yes/no): ").lower()
                    if confirm_updating == 'yes':
                        break
                    elif confirm_updating == 'no':
                        print("Updating/Editing book information cancelled.")
                        return
                    else:
                        print("Invalid input! Please enter 'yes' or 'no'.")

                while True:  # Selection for user to choose what they want to update/edit
                    print("\nSelect the information you want to update/edit: ")
                    print("1. ISBN")
                    print("2. Author")
                    print("3. Title")
                    print("4. Publisher")
                    print("5. Genre")
                    print("6. Year Published")
                    print("7. Date Purchased")
                    print("8. Status")

                    try:
                        updating_choice = int(input("Enter your choice(1-8): "))  # Ask user to input choice
                        if updating_choice == 1:
                            while True:
                                try:  # exception handling for ISBN
                                    book['ISBN'] = input("New ISBN (10-13 numeric digits): ").strip()
                                    if not book['ISBN']:  # Check whether the ISBN is empty
                                        raise ValueError("ISBN cannot be empty.")
                                    if not book['ISBN'].isdigit():
                                        raise ValueError('ISBN should contain only numeric digits!')
                                    if not (10 <= len(book['ISBN']) <= 13):
                                        # ISBN should be in 10-13 digits
                                        raise ValueError("ISBN should be contain 10-13 numeric digits!")
                                    break
                                except ValueError as e:
                                    print(f'{e}\nPlease enter a valid input.')
                        elif updating_choice == 2:
                            while True:
                                try:  # exception handling for Author
                                    book['Author'] = input("New Author: ").strip()
                                    if not book['Author']:  # Check whether the Author is empty
                                        raise ValueError("Author name cannot be empty!")
                                    if not book['Author'].replace(" ", "").isalpha():
                                        # Author should be in alphabets only
                                        raise ValueError("Please enter only alphabets!")
                                    break
                                except ValueError as e:
                                    print(e)
                        elif updating_choice == 3:
                            while True:
                                try:  # exception handling for Title
                                    book['Title'] = input("Title: ").strip()
                                    if not book['Title']:  # Check whether the Title is empty
                                        raise ValueError("Title cannot be empty!")
                                    break
                                except ValueError as e:
                                    print(f'{e}\nPlease enter a valid input!')
                        elif updating_choice == 4:
                            while True:
                                try:  # exception handling for Publisher
                                    book['Publisher'] = input("Publisher: ").strip()
                                    if not book['Publisher']:  # Check whether the Publisher is empty
                                        raise ValueError("Publisher cannot be empty!")
                                    break
                                except ValueError as e:
                                    print(f"{e}\nPlease enter a valid input!")
                        elif updating_choice == 5:
                            while True:
                                try:  # exception handling for Genre
                                    book['Genre'] = input("New Genre: ").strip()
                                    if not book['Genre']:  # Check whether the Genre is empty
                                        raise ValueError("Genre cannot be empty!")
                                    if not book['Genre'].replace(" ", "").isalpha():
                                        # Genre should be in alphabets only
                                        raise ValueError("Please enter only alphabets!")
                                    break
                                except ValueError as e:
                                    print(e)
                        elif updating_choice == 6:
                            while True:
                                try:  # exception handling for Year Published
                                    book['Year Published'] = input(
                                        "New Year Published (4 digits): ").strip()
                                    if not book['Year Published']:  # Check whether the year is empty
                                        raise ValueError("Year Published cannot be empty!")
                                    if not book['Year Published'].isdigit():
                                        raise (ValueError
                                               ('Year Published should contain only numeric digits.'))
                                    if not (1000 <= int(book['Year Published']) <= 2023):
                                        # Year Published should be in 4 digits and before 2024
                                        raise ValueError(
                                            "Year Published should be contain 4 digits "
                                            "and published before 2024!")
                                    break
                                except ValueError as e:
                                    print(f"{e}\nPlease enter a valid input!")
                        elif updating_choice == 7:
                            from datetime import datetime
                            while True:
                                try:  # exception handling for Date Purchased
                                    book['Date Purchased'] = input(
                                        "New Date Purchased (DD-MM-YYYY): ").strip()
                                    if not book['Date Purchased']:  # Check whether the date is empty
                                        raise ValueError("Date Purchased cannot be empty!")

                                    new_date = datetime.strptime(book['Date Purchased'], "%d-%m-%Y")
                                    if new_date.date() > datetime.now().date():
                                        # Date Purchased should be in right format
                                        raise ValueError(
                                            'Date Purchased cannot be in the future.')
                                    # update the book with new date purchased
                                    new_date_purchased = book['Date Purchased']
                                    # Check if the Date Purchased year is earlier than the Year Published
                                    year_published = int(book['Year Published'])
                                    date_purchased_year = int(new_date_purchased.split('-')[-1])
                                    if date_purchased_year < year_published:
                                        raise ValueError(
                                            "Date Purchased year cannot be earlier than Year Published!")
                                    break

                                except ValueError as e:
                                    if "does not match format" in str(e):
                                        print(
                                            "Incorrect date format. "
                                            "Please enter the date in DD-MM-YYYY format.")
                                    else:
                                        print(f"{e}\nPlease enter a valid date.")
                        elif updating_choice == 8:
                            while True:
                                try:  # exception handling for Status
                                    book['Status'] = input("New Status: ").strip().lower()
                                    if not book['Status']:
                                        raise (ValueError
                                               ('Status cannot be empty!\nPlease enter a valid input.'))
                                    # if statement, relational and logic operators was used
                                    if (book['Status'] != 'read'.lower()
                                            and book['Status'] != 'to-read'.lower()):
                                        raise ValueError('Please enter only "read" or "to-read"')

                                    break
                                except ValueError as e:
                                    print(e)
                            print("Information update successfully!")
                        else:
                            print("Invalid. Please enter a number between 1 and 8.")
                            continue

                        while True:  # Confirmation by user to continue updating/editing
                            continue_updating = input(
                                "\nDo you want to continue updating/editing THIS book (yes/no): ").lower()
                            if continue_updating == 'yes':
                                clear()
                                break
                            elif continue_updating == 'no':
                                print("Finishing update/editing book information.")
                                return
                            else:
                                print("Invalid input! Please enter 'yes' or 'no'.")

                    except ValueError:
                        print(f"\nInvalid input!!! Please enter choice from 1-8.")
        if not matching_found:
            print("No matching record found. Please enter again.")


def update_to_file():  # exception handling
    try:  # Open the file for writing
        for book in books_data:  # Iterate over each book in the list
            # Write the book information to the file
            books_data.write(
                f"{book['ISBN']},{book['Author']},{book['Title']},{book['Publisher']},{book['Genre']},"
                f"{book['Year Published']},{book['Date Purchased']},{book['Status']}\n")
    except Exception as e:
        print(f"{e}")

    while True:  # Confirmation by user to update another book
        clear()
        choice_continue = input("\nDo you want to continue updating/editing ANOTHER book? (yes/no): ").lower()
        if choice_continue == 'yes':
            clear()
            update_book()  # Continue the outer loop
        elif choice_continue == 'no':
            clear()
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")


def display_book():  # Display current book information
    print("\nDisplay")
    print("CURRENT BOOK LIST:")
    headers = ['ISBN', 'Author', 'Title', 'Publisher', 'Genre', 'Year Published', 'Date Purchased',
               'Status']

    if books_data:
        column_length = {}  # Create an empty dictionary to store column lengths
        for header in headers:
            # Find the maximum length of each column
            maximum_length = max(len(str(header)),
                                 max(len(str(book.get(header, ''))) for book in books_data))
            column_length[header] = maximum_length + 1  # Assign the maximum length into the current column

        new_headers = []  # Create an empty list to store the header string
        for header in headers:
            # Format the header string
            new_header = "{:{}}".format(header, column_length[header])
            new_headers.append(new_header)

        header_separator1 = '| '.join(new_headers)  # Put the separator together with the new_headers
        print(header_separator1)
        separator_line = '=' * len(header_separator1)  # Create separator horizontal line
        print(separator_line)

        for book_info in books_data:
            formatting_result = []  # Create an empty list to stor formatting result

            for header in headers:
                # Format all current data
                result = "{:<{}}".format(str(book_info.get(header, '')), column_length[header])
                formatting_result.append(result)
            # Print the final result
            final_result = '| '.join(formatting_result)
            print(final_result)
    else:
        print("No books available!")


def display_continue():
    while True:
        choice_continue = input("\nDo you want to continue? (yes/no): ").lower()
        if choice_continue == 'yes':
            clear()
            display_book()  # Continue the outer loop
        elif choice_continue == 'no':
            clear()
            print("Exiting Display System.Thank you")
            break  # stops execution of the display function, terminate the program
        else:
            print("Invalid input! Please enter 'yes' or 'no'")


def search_book():
    clear()
    print(f"\nLet's search for your book!")
    search_criteria = input(
        "Enter ISBN, author, or title to search: ").lower()
    # Prompt user enter the search criteria(ISBN, Author, Title)
    matching_book = []  # create an empty list to store matching book
    for book in books_data:
        if search_criteria in [book['ISBN'].lower(), book['Author'].lower(), book
        ['Title'].lower()]:
            # check if the search criteria matches ISBN, Author or Title
            matching_book.append(book)  # append the book into matching book list if there is a match
    if matching_book:  # if there are any matching books
        print("\nMatching Book!")
        for book in matching_book:  # print matching book and its information
            print(f"\n{'ISBN':<15}: {book['ISBN']}")
            print(f"{'Author':<15}: {book['Author']}")
            print(f"{'Title':<15}: {book['Title']}")
            print(f"{'Publisher':<15}: {book['Publisher']}")
            print(f"{'Genre':<15}: {book['Genre']}")
            print(f"{'Year Published':<15}: {book['Year Published']}")
            print(f"{'Date Purchased':<15}: {book['Date Purchased']}")
            print(f"{'Status':<15}: {book['Status']}")

    else:  # if there are not any matching books
        print("No matching book found.")
        search_continue()


def search_continue():
    while True:
        choice_continue = input("Do you want to continue? (yes/no): ").lower()
        if choice_continue == 'yes':
            search_book()  # Continue the outer loop
        elif choice_continue == 'no':
            clear()
            print("Exiting Search System.Thank you")
            break  # stops execution of the search function, terminate the program
        else:
            print("Invalid input! Please enter 'yes' or 'no'")


def main():
    file_name = "books_23099740.txt"
    read_books_from_file(file_name)
    while True:
        clear()
        print(ASCII_ART)
        print("Welcome to Malatang Book Management System ૮₍˃ ⤙ ˂₎ა")
        print("1. Add Book Record(s)")
        print("2. Delete Book Record(s)")
        print("3. Update/Edit Book Record(s)")
        print("4. Display")
        print("5. Search for Book(s)")
        print("6. Exit")
        choice = input("Enter your choice (1-6) in order for us to assist you: ")

        if choice == '1':
            clear()
            add_book()
            add_continue()
        elif choice == '2':
            clear()
            delete_book()
            delete_continue()
        elif choice == '3':
            clear()
            update_book()
            update_to_file()
        elif choice == '4':
            display_book()
            display_continue()
        elif choice == '5':
            clear()
            search_book()
            search_continue()
        elif choice == '6':
            clear()
            print("Exiting Malatang Book Management System. Thank you for using!")
            file_name = "books_23099740.txt"
            # open file in write mode to save book data
            with open(file_name, 'w') as f:
                # iterate through each dictionary in books_data
                for idx in books_data:
                    # write each value from the dictionary, separated by commas to file
                    f.write(','.join(str(value) for value in idx.values()) + '\n')
            return books_data
        else:
            print("Invalid choice. Please enter a valid option.")
            input("\nPress Enter to continue...")


main()