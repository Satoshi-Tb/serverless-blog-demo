import flask
from flask import request, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user
from flask_blog import app
from flask_blog.models.users import User


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username != app.config["USERNAME"]:
            flash("ユーザー名が異なります")
        elif password != app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            login_user(User(username))
            flash("ログインしました")
            return redirect(url_for("show_entries"))

    return render_template("login.html")


@app.route("/logout")
def log_out():
    logout_user()
    flash("ログアウトしました")
    return redirect(url_for("login"))


@app.errorhandler(404)
def non_exist_route(error):
    return redirect(url_for("login"))
