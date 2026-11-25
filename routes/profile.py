from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from models.profile import Profile
from utils.auth_utils import login_required

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        age = request.form.get("age")
        occupation = request.form.get("occupation")
        monthly_income = request.form.get("monthly_income")
        city = request.form.get("city")
        marital_status = request.form.get("marital_status")
        dependents = request.form.get("dependents")

        if not age or not occupation or not monthly_income or not city:
            flash("Please fill all required fields.", "danger")
            return redirect(url_for("profile.profile"))

        try:
            existing = Profile.query.filter_by(user_id=session["user_id"]).first()

            if existing:
                existing.age = int(age)
                existing.occupation = occupation
                existing.monthly_income = float(monthly_income)
                existing.city = city
                existing.marital_status = marital_status
                existing.dependents = int(dependents) if dependents else 0
            else:
                new_profile = Profile(
                    user_id=session["user_id"],
                    age=int(age),
                    occupation=occupation,
                    monthly_income=float(monthly_income),
                    city=city,
                    marital_status=marital_status,
                    dependents=int(dependents) if dependents else 0,
                )
                db.session.add(new_profile)

            db.session.commit()

            flash("Profile saved!", "success")
            return redirect(url_for("dashboard.dashboard"))

        except Exception as e:
            db.session.rollback()
            print("Profile Save Error:", e)
            flash("Something went wrong saving your profile.", "danger")
            return redirect(url_for("profile.profile"))

    return render_template("profile.html")
