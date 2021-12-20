import json
import datetime
import uuid

import flask
from flask import Flask, Response

app = Flask(__name__)
BASE_URL = "/api/v1"


def check_valid_input(valid_keys, data):
    for key in data:
        if key not in valid_keys:
            return False
    return True


def read_all_posts():
    # Open blog_posts in read mode, store it in books_file
    with open("blog_file.json", "r") as blog_file:
        # Return list from json data
        return json.load(blog_file)


def save_data(data):
    with open("blog_file.json", "w") as blog_file:
        json.dump(data, blog_file, indent=2)


def find_post_recursive(post_id, posts, high_index, low_index, memory_index):
    middle_index = int((low_index+high_index)/2)  # In the middle
    if middle_index == memory_index:
        return None
    if posts[middle_index]["post_id"] == int(post_id):
        return posts[middle_index]
    if posts[high_index]["post_id"] == int(post_id):
        return posts[high_index]
    if posts[low_index]["post_id"] == int(post_id):
        return posts[low_index]
    elif posts[middle_index]["post_id"] < int(post_id):
        low_index = middle_index
        return find_post_recursive(post_id, posts, high_index, low_index, middle_index)
    else:
        high_index = middle_index
        return find_post_recursive(post_id, posts, high_index, low_index, middle_index)


@app.get(BASE_URL + "/posts/locate/<post_id>")
def find_post(post_id):
    posts = read_all_posts()
    if posts:   # If there are elements in the list
        post = find_post_recursive(post_id, posts, (len(posts)-1), 0, None)
        if post:    # If the return value is not None
            return Response(json.dumps(post), 200, content_type="application/json")
    return Response('{"status": "could not find post"}', 404, content_type="application/json")


@app.get(BASE_URL + "/posts")
def get_all_posts():
    posts = read_all_posts()
    if posts:
        return Response(json.dumps(posts),
                        200, content_type="application/json")
    return Response('{"status" : "not found"}', 404, content_type="application/json")


@app.get(BASE_URL + "/posts/headlines")
def get_all_headlines():
    posts = read_all_posts()
    if posts:
        list_with_headlines = []
        for post in posts:
            list_with_headlines.append(post["headline"])
        return Response(json.dumps(list_with_headlines), 200, content_type="application/json")
    return Response('{"status" : "not found"}', 404, content_type="application/json")


@app.post(BASE_URL + "/posts/post")
def add_post():
    data = flask.request.json
    unique_id = generate_unique_id()
    valid_keys = ["content", "user_id", "headline"]
    check_valid_input(valid_keys, data)
    # data["post_id"] = unique_id.time      ID is saved as key in dict
    data["review"] = []
    data["date"] = None
    data["post_id"] = unique_id.time
    posts = read_all_posts()
    posts.append(data)
    save_data(posts)
    return Response('{"status" : "created"}', 201, content_type="application/json")


@app.put(BASE_URL + "/posts/post/comment_author/<comment_id>")
def post_comment_to_author(comment_id):
    data = flask.request.json
    valid_keys = ["user_id", "comment", "recommended_content"]
    if not check_valid_input(valid_keys, data):
        return Response('{"status": "error", "reason": "Json format error not allowed"}'
                        , 400, content_type="application/json")
    posts = read_all_posts()
    unique_id = generate_unique_id()
    data["comment_id"] = unique_id.time
    for post in posts:
        if post["post_id"] == int(comment_id):
            post["review"].append(data)
            save_data(posts)
            return Response('{"status" : "created"}', 201, content_type="application/json")
    return Response('{"status" : "ERROR" ' + comment_id + 'is not valid}',
                          400, content_type="application/json")


def generate_unique_id():
    return uuid.uuid1()


if __name__ == "__main__":
    app.run(port=5001)
