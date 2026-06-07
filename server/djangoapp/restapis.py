import os
import requests
from dotenv import load_dotenv


load_dotenv()

backend_url = os.getenv("backend_url", "http://localhost:3030")


def get_request(endpoint, **kwargs):
    params = ""

    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from {} ".format(request_url))

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("Network exception occurred")
        print(e)
        return None