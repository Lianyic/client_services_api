import os
import requests
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BOOKS_API_URL = os.getenv("BOOKS_API_URL")

if not BOOKS_API_URL:
    raise ValueError("⚠️ Error: BOOKS_API_URL is not set! Make sure to define it in .env or in your environment.")

@app.route("/", methods=["GET", "POST"])
def search_books():
    books = []
    error_message = None

    if request.method == "POST":
        genre_query = request.form.get("genre")
        author_query = request.form.get("author")
        title_query = request.form.get("title")

        params = {k: v for k, v in {"genre": genre_query, "author": author_query, "title": title_query}.items() if v}

        try:
            response = requests.get(BOOKS_API_URL, params=params)
            if response.ok:
                books = response.json()
            else:
                error_message = "Failed to fetch books from the server."
        except requests.exceptions.RequestException as e:
            error_message = f"Connection error: {str(e)}"

    return render_template("index.html", books=books, error_message=error_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

