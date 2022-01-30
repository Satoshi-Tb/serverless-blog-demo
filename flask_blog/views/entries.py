import flask
from flask import request, redirect, url_for, render_template, flash, session, Markup
from flask_blog import app
from datetime import datetime
from flask_blog.models.entries import Entry


# 改行コードを<br>に置換し、その他のhtml特殊文字をエスケープしたい
@app.template_filter("cr")
def cr(arg):
    return Markup(arg.replace("\r\n", "<br>"))


@app.route("/")
def show_entries():

    entries = Entry.scan()
    entries = sorted(entries, key=lambda x: x.article_id, reverse=True)

    user = {
        "is_authenticated": True
    }
    return render_template("entries/index.html", entries=entries, current_user=user)


@app.route("/entries", methods=["POST"])
def add_entry():
    entry = Entry(
        article_id=int(datetime.now().timestamp()),
        title=request.form["title"],
        text=request.form["text"],
    )
    entry.save()

    return redirect(url_for("show_entries"))


@app.route("/entries/new", methods=["GET"])
def new_entry():
    user = {
        "is_authenticated": True
    }

    return render_template("entries/new.html", current_user=user)


@app.route("/entries/<int:article_id>", methods=["GET"])
def show_entry(article_id):
    entry = Entry.get(article_id)
    user = {
        "is_authenticated": True
    }

    return render_template("entries/show.html", entry=entry, current_user=user)


@app.route("/entries/<int:article_id>/edit", methods=["GET"])
def edit_entry(article_id):
    entry = Entry.get(article_id)
    user = {
        "is_authenticated": True
    }

    return render_template("entries/edit.html", entry=entry, current_user=user)


@app.route("/entries/<int:article_id>/update", methods=["POST"])
def update_entry(article_id):
    entry = Entry.get(article_id)

    entry.update(actions=[
        Entry.title.set(request.form["title"]),
        Entry.text.set(request.form["text"]),
    ])

    return redirect(url_for("show_entries"))


@app.route("/entries/<int:article_id>/delete", methods=["POST"])
def delete_entry(article_id):
    entry = Entry.get(article_id)
    entry.delete()

    return redirect(url_for("show_entries"))
