import requests

def get_posts():

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url, timeout=10)

    if response.status_code == 200:

        return response.json()

    else:

        print("API request failed")
        return []