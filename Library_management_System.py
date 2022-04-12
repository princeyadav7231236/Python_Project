class library:
    def __init__(self, library_name, *list_of_books):
        self.list_of_books = list_of_books
        self.library_name = library_name

    def display_books(self, comment):
        i = 0
        print(comment)
        for item in self.list_of_books:
            i += 1
            print(i, "-->   ", item)

    def lend_book(self, **kwargs):
        print("Here are the name of all the books and people who have lend the book")
        print("Enter the name of the book you want to Lend : ")
        key_1 = input()
        print("Enter your name here : ")
        value_1 = input()
        kwargs[key_1] = value_1

        while True:
            if key_1 in self.list_of_books:
                print("You can Lend this book")
                print("Details updated successfully ......")
                break
            elif key_1 not in self.list_of_books:
                print("This book is not in the Library")
                break
            else:
                print("This book is not in the Library")
                break

    def add_book(self, *name_of_book):
        print("Successfully added the book ")
        adding = self.list_of_books + name_of_book
        i = 0
        for item in adding:
            i += 1
            print(i, "-->   ", item)

    def return_book(self, **dictionary_of_returned_books):
        while True:
            print("Enter the name of the book you want to return : ")
            key_1 = input()
            print("Enter your name here : ")
            value_1 = input()
            dictionary_of_returned_books[key_1] = value_1
            print("Successfully added ......")
            print("If you want to see the dictionary the type 'print dictionary' : ")
            print("If you want to add more items to the dictionary then type 'add' else type 'exit' to exit : ")
            again = input()
            if again == "add":
                continue
            elif again == "print dictionary":
                print(dictionary_of_returned_books)
                break
            else:
                break


if __name__ == '__main__':
    print(
        "What do you want to do here ? \n Do you want to : \n 1)  Display the Library \n 2)  Lend a book from the Library \n 3)  Add a book in the Library \n 4) Return a book to the Library ")
    print("Type 'Display' to Display the Library .")
    print("Type 'Lend' to Lend a book from the Library .")
    print("Type 'Add' to Add a book in the Library")
    print("Type 'Return' to Return a book to the Library")
    print("Type 'Exit' to exit the Library. ")
    var_1 = input("So, what do you want to do ? \n Type here --> ")
    list_of_book = ["1", 2, 3, 4, 4545, 46]

    dictionary_of_lend_books = {"a": 1, "b": 2}
    dictionary_of_returned_book = {"Name": "Diwakar singh", "Class": "XII",
                                   "Profession": {"Profession": "Teacher", "profession": "Student"}}
    library_1 = library("Library_1", *list_of_book)
    comment_1 = "Displaying list of books"
    while True:

        if var_1 == "Display":
            library_1.display_books(comment_1)
            break

        elif var_1 == "Lend":
            library_1.lend_book(**dictionary_of_lend_books)
            break

        elif var_1 == "Add":
            list_of_name_of_book_to_be_added = [input("Enter the name of the book which you want to add : ")]

            library_1.add_book(*list_of_name_of_book_to_be_added)
            break

        elif var_1 == "Return":
            library_1.return_book(**dictionary_of_returned_book)
            break

        elif var_1 == "Exit" or var_1 == "exit":
            break

        else:
            print("You entered a wrong word !")
            break
