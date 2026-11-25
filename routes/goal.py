from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from models.goal import Goal
from utils.auth_utils import login_required
from datetime import datetime

goal_bp = Blueprint("goal", __name__)


@goal_bp.route("/goals", methods=["GET", "POST"])
@login_required
def goals():
    if request.method == "POST":
        name = request.form.get("name")
        target_amount = request.form.get("target_amount")
        target_date = request.form.get("target_date")
        priority = request.form.get("priority")

        if not name or not target_amount:
            flash("Please fill all required fields.", "danger")
            return redirect(url_for("goal.goals"))

        try:
            new_goal = Goal(
                user_id=session["user_id"],
                name=name,
                target_amount=float(target_amount),
                target_date=datetime.strptime(target_date, "%Y-%m-%d") if target_date else None,
                priority=priority,
            )
            db.session.add(new_goal)
            db.session.commit()

            flash("Goal added!", "success")
            return redirect(url_for("goal.goals"))

        except Exception as e:
            db.session.rollback()
            print("Goal Save Error:", e)
            flash("Something went wrong adding your goal.", "danger")
            return redirect(url_for("goal.goals"))

    user_goals = Goal.query.filter_by(user_id=session["user_id"]).all()
    return render_template("goal.html", goals=user_goals)
