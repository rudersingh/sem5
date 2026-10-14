
books = {}

n = int(input("Enter the number of books to add: "))

for i in range(n):
    title = input("Enter book title: ").strip().lower()
    copies = int(input("Enter number of copies: "))

    if copies < 0:
        print("Invalid number of copies!")
    else:
        books[title] = copies

while True:
    print("\n--- Library Menu ---")
    print("1. Issue a book")
    print("2. Return a book")
    print("3. Display all books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title to issue: ").strip().lower()

        if title not in books:
            print("Book is unavailable in the library.")
        elif books[title] > 0:
            books[title] -= 1
            print("Book issued successfully.")
        else:
            print("No copies available to issue.")

    elif choice == "2":
        title = input("Enter book title to return: ").strip().lower()

        if title not in books:
            print("Book is unavailable in the library.")
        elif books[title] == 0:
            print("No issued copy of this book to return.")
        else:
            books[title] += 1
            print("Book returned successfully.")

    elif choice == "3":
        print("\n--- All Books ---")
        if not books:
            print("Library is empty.")
        else:
            for title, copies in books.items():
                print(title.title(), ":", copies, "copies available")

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please try again.")
