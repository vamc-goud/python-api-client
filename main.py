from api_client import get_posts

posts = get_posts()

for post in posts[:5]:

    print("Title:", post["title"])
    print("User ID:", post["userId"])
    print("----------------")