
import requests
from collections import defaultdict

URL = "http://localhost:4004/odata/v4/catalog/Reviews"

reviews = [
    {"rating": 5, "comment": "Excellent book", "book_ID": 1},
    {"rating": 4, "comment": "Very interesting", "book_ID": 1},
    {"rating": 3, "comment": "Good book", "book_ID": 2}
]

ratings_by_book = defaultdict(list)

for review in reviews:
    try:
        response = requests.post(URL, json=review)

        if response.status_code in (200, 201):
            print(
                f"Review added for Book {review['book_ID']}: "
                f"{review['rating']}/5"
            )
            ratings_by_book[review["book_ID"]].append(
                review["rating"]
            )
        else:
            print("Failed:", response.status_code, response.text)

    except requests.RequestException as error:
        print("Connection error:", error)

print("\nAverage rating per book:")

for book_id, ratings in ratings_by_book.items():
    average = sum(ratings) / len(ratings)
    print(f"Book ID {book_id}: {average:.2f}/5")
