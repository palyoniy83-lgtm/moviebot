import requests
from config import UCOZ_TOKEN


API_URL = "https://5star.at.ua/uapi/publ"


def test_ucoz():

    print("===== TEST UCOZ API =====")


    headers = {

        "Authorization": f"Bearer {UCOZ_TOKEN}",

        "Accept": "application/json"

    }


    response = requests.get(

        API_URL,

        headers=headers

    )


    print("STATUS:")

    print(response.status_code)


    print()

    print("RESPONSE:")

    print(response.text)



if __name__ == "__main__":

    test_ucoz()
