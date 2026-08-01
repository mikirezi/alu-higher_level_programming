#!/usr/bin/python3
"""Script that searches for a user via search_user and prints result."""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(
        "http://0.0.0.0:5000/search_user", data={'q': letter})
    try:
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
