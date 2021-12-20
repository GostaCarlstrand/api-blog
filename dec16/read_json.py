import json


def main():
    with open("data_test.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    data["members"][0]["age"] += 1

    with open("data_test.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
