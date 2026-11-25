from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from models.user import User

auth = Blueprint("auth", __name__)


# -------------------- Home Page --------------------
@auth.route("/")
def home():
    return render_template("index.html")


# -------------------- Register --------------------
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        if not full_name or not email or not phone or not password:
            flash("Please fill all the fields.", "danger")
            return redirect(url_for("auth.register"))

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered.", "warning")
            return redirect(url_for("auth.register"))

        try:
            new_user = User(
                full_name=full_name,
                email=email,
                phone=phone,
                password=""
            )
            new_user.set_password(password)

            db.session.add(new_user)
            db.session.commit()

            flash("Registration Successful! Please log in.", "success")
            return redirect(url_for("auth.login"))

        except Exception as e:
            db.session.rollback()
            print("Database Error:", e)
            flash("Database Error!", "danger")
            return redirect(url_for("auth.register"))

    return render_template("register.html")


# -------------------- Login --------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Please fill all the fields.", "danger")
            return redirect(url_for("auth.login"))

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session["user_id"] = user.id
            session["user_name"] = user.full_name

            flash("Login successful!", "success")
            return redirect(url_for("dashboard.dashboard"))
        else:
            flash("Invalid email or password.", "danger")
            return redirect(url_for("auth.login"))

    return render_template("login.html")


# -------------------- Logout --------------------
@auth.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.home"))
