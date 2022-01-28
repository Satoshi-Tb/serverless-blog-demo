from flask import request
from flask_blog import app


@app.route("/")
def show_entries():
    return "全ての記事を表示"


@app.route("/entries", methods=["POST"])
def add_entry():
    return "新しく記事が作成されました"


@app.route("/entries/new", methods=["GET"])
def new_entry():
    return "記事の入力フォームを表示"


@app.route("/entries/<int:article_id>", methods=["GET"])
def show_entry(article_id):
    return f"記事{article_id}を表示"


@app.route("/entries/<int:article_id>/edit", methods=["GET"])
def edit_entry(article_id):
    return f"記事{article_id}の編集画面を表示"


@app.route("/entries/<int:article_id>/update", methods=["POST"])
def update_entry(article_id):
    return f"記事{article_id}を更新しました"


@app.route("/entries/<int:article_id>/delete", methods=["POST"])
def delete_entry(article_id):
    return f"記事{article_id}を削除しました"
