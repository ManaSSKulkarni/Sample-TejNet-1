import pdb
import requests
from bs4 import BeautifulSoup

pdb.set_trace()


def divide(a, b):
    pdb.set_trace()
    result = a / b
    return result


def scraping(url):
    response = requests.get(url)
    pdb.set_trace()

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
    else:
        print("Error: Failed to fetch data from the website")


def main():
    x = 10
    y = 10
    pdb.set_trace()
    try:
        result = divide(x, y)
        print("Result=", result)
    except Exception as e:
        pdb.post_mortem()

    scraping("https://example.com")


if __name__ == "__main__":
    main()
