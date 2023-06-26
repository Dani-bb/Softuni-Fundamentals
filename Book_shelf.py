shelf_with_books = input().split("&")

while True:
    command = input()
    if command == "Done":
        break
    command = command.split(" | ")
    if len(command) < 2:
        continue
    action = command[0]
    if action == "Add Book":
        book = command[1]
        if book in shelf_with_books:
            continue
        else:
            shelf_with_books.insert(0,book)
    if action == "Take Book":
        book = command[1]
        if book in shelf_with_books:
            shelf_with_books.remove(book)
        else:
            continue
    elif action == "Insert Book":
        book = command[1]
        if book  in shelf_with_books:
            continue
        else:
            shelf_with_books.append(book)
    elif action == "Check Book":
        index = int(command[1])
        if index < len(shelf_with_books):
            print(shelf_with_books[index])
    elif action == "Swap Books":
        book1 = command[1]
        book2 = command[2]
        if book1 in shelf_with_books and book2 in shelf_with_books:
            index1 = shelf_with_books.index(book1)
            index2 = shelf_with_books.index(book2)
            shelf_with_books[index1], shelf_with_books[index2] = shelf_with_books[index2], shelf_with_books[index1]

print(", ".join(shelf_with_books))
