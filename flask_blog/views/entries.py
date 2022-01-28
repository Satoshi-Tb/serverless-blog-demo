from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from datetime import datetime


@app.route("/")
def show_entries():
    entries = [
        {
            "id": 1,
            "title": "はじめての投稿",
            "text": "はじめての内容",
            "created_at": datetime.now(),
        },
        {
            "id": 2,
            "title": "2つ目の投稿",
            "text": "２つ目の内容",
            "created_at": datetime.now(),
        },
    ]

    user = {
        "is_authenticated": True
    }

    return render_template("entries/index.html", entries=entries, current_user=user)


@app.route("/entries", methods=["POST"])
def add_entry():
    return "新しく記事が作成されました"


@app.route("/entries/new", methods=["GET"])
def new_entry():
    return "記事の入力フォームを表示"


@app.route("/entries/<int:article_id>", methods=["GET"])
def show_entry(article_id):
    entry = {
        "id": 1,
        "title": "はじめての投稿",
        "text": "はじめての内容",
        "created_at": datetime.now(),
    }

    user = {
        "is_authenticated": True
    }

    return render_template("entries/show.html", entry=entry, current_user=user)


@app.route("/entries/<int:article_id>/edit", methods=["GET"])
def edit_entry(article_id):
    return f"記事{article_id}の編集画面を表示"


@app.route("/entries/<int:article_id>/update", methods=["POST"])
def update_entry(article_id):
    return f"記事{article_id}を更新しました"


@app.route("/entries/<int:article_id>/delete", methods=["POST"])
def delete_entry(article_id):
    return f"記事{article_id}を削除しました"
