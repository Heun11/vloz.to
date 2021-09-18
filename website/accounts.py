from flask import Blueprint, render_template, request, flash, redirect, url_for
from .db_models import users
from . import db
from .fun import hash_pass
from flask_login import login_user, login_required, logout_user, current_user
import json

accounts = Blueprint('accounts', __name__)

@accounts.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        if request.form["ln"] == "" or request.form["pw"] == "" or request.form["em"] == "":
            return redirect(url_for("accounts.register"))
        else:
            user = request.form["ln"]
            email = request.form["em"]
            password = request.form["pw"]

            found_user = users.query.filter_by(email=email).first()

            if found_user:
                return redirect(url_for("accounts.login"))

            if current_user.is_authenticated:
                return redirect(url_for("accounts.user"))

            else:
                new_user = users(email=email, name=user, password=hash_pass(password), files=json.dumps({"files":[]}))

                db.session.add(new_user)
                db.session.commit()

                login_user(new_user, remember=True)
                return redirect(url_for("accounts.user"))
    else:
        return render_template("register.html")

@accounts.route("/login", methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("accounts.user"))

    if request.method == "POST":
        if request.form["em"] == "" or request.form["pw"] == "":
            return redirect(url_for("accounts.login"))
        else:
            email = request.form["em"]
            password = request.form["pw"]

            found_user = users.query.filter_by(email=email).first()
            if found_user:
                if hash_pass(password) == found_user.password:
                    user = found_user.name
                    login_user(found_user, remember=True)
                    return redirect(url_for("accounts.user"))
                else:
                    return redirect(url_for("accounts.login"))
            else:
                return redirect(url_for("accounts.register"))
    else:
        return render_template("login.html")


@accounts.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("accounts.login"))

@accounts.route("/user")
def user():
    if current_user.is_authenticated:
        return render_template("user.html", user=current_user.name, files=json.loads(current_user.files))
    else:
        return redirect(url_for("accounts.login"))

@accounts.route("/delete")
def delete():
    if current_user.is_authenticated:
        email = current_user.email
        user = users.query.filter_by(email=email).first()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("accounts.logout"))
    else:
        return redirect(url_for("accounts.login"))

@accounts.route("/view")
def view():
    return render_template("view.html", values=users.query.all())