import requests
import json


def retrieve_data_from_api(url, name):
    return requests.get(url + name)


def main():
    name = input("What is your name? ")

    country = retrieve_data_from_api("https://api.nationalize.io?name=", name)
    gender = retrieve_data_from_api("https://api.genderize.io?name=", name)

    gender_text = json.loads(gender.text)
    country_code = json.loads(country.text)["country"][0]["country_id"]


    print(country_code)
    print(gender_text["gender"])

    # Find country from name from the highest percent
    # Find country code/ID
    # Use other api to find information about country


if __name__ == "__main__":
    main()
