import os
import requests
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# 通过环境变量获取 `book-api` 地址（如果未设置，使用默认值）
BOOKS_API_URL = os.getenv("BOOKS_API_URL", "http://20.254.238.140:5000/books")

@app.route("/", methods=["GET", "POST"])
def search_books():
    books = []  # 存储搜索结果
    error_message = None

    if request.method == "POST":
        # 从前端获取查询参数
        genre_query = request.form.get("genre")
        author_query = request.form.get("author")
        title_query = request.form.get("title")

        # 仅保留有值的查询参数，传递给 `book-api`
        params = {k: v for k, v in {"genre": genre_query, "author": author_query, "title": title_query}.items() if v}

        try:
            response = requests.get(BOOKS_API_URL, params=params)
            if response.ok:
                books = response.json()  # 获取 `book-api` 返回的筛选数据
            else:
                error_message = "Failed to fetch books from the server."
        except requests.exceptions.RequestException as e:
            error_message = f"Connection error: {str(e)}"

    return render_template("index.html", books=books, error_message=error_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
