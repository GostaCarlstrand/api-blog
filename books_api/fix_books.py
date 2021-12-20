import json
import datetime


def main():
    now = datetime.date.today()


    # 3 Open file in read mode, store in books_file
    with open("books.json", "r") as books_file:
        # From the json file books_file to a python list
        books = json.load(books_file)
        # Loop book in books
    for i, book in enumerate(books):
        # Delete the content of imageLink
        #del book["imageLink"]
        # Add a key : set value to i +1
        book["id"] = i + 1
        # Add a key : set value to an empty list
        book["reviews"] = []

        # Open books.json in write mode, store content in books_file
    with open("books.json", "w") as books_file:
        # Write to file using python object books, to books_file
        json.dump(books, books_file)


if __name__ == "__main__":
    main()
