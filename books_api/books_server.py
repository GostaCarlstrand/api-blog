from flask import Flask, Response
import json

app = Flask(__name__)

BASE_URL = "/api/v1"


def read_all_books():
    with open("books.json", "r") as books_file:
        return json.load(books_file)    # Returns a python dict


@app.get(BASE_URL + "/books")
def get_all_books():
    return Response(json.dumps(read_all_books()),
                    200, content_type="application/json")


@app.get(BASE_URL + "/books/<book_id>")
def get_book(book_id):
    books = read_all_books()
    for book in books:
        if book["id"] == int(book_id):
            return Response(json.dumps(book), 200, content_type="application/json")
    return Response('{"status : Error", "reason": "Book with id' + book_id + 'not found}',
                    404, content_type="application/json")


if __name__ == "__main__":
    app.run(port=4067)
