import flask
import json

app = flask.Flask(__name__)


def read_data():
    with open("data.json", "r") as json_file:
        return json.load(json_file)


@app.get("/persons")
def index_get():
    last_name = flask.request.args.get("last_name")
    persons = read_data()
    if last_name:
        persons = [person for person in persons if person["last_name"] == last_name]
    json_persons = json.dumps(persons)
    return flask.Response(json_persons, 200, content_type="application/json")


@app.get("/v2/users")
def index2_get():
    return index_get()


def save_data(data):
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)


@app.post("/persons")
def index_post():
    data = flask.request.json
    valid_keys = ["first_name", "last_name", "age"]
    for key in data:
        if key not in valid_keys:
            return flask.Response('{"status": "error", "reason": "Json format error' + key + '"not allowed"}'
                                  , 400, content_type="application/json")
    persons = read_data()
    persons.append(data)
    save_data(persons)
    return flask.Response('{"status" : "created"}', 201, content_type="application/json")


if __name__ == "__main__":
    app.run(port=4789)