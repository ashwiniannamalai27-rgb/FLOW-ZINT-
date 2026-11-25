from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from models.reminder import Reminder
from utils.auth_utils import login_required

reminder_bp = Blueprint("reminder", __name__)


@reminder_bp.route("/reminders", methods=["GET", "POST"])
@login_required
def reminders():
    if request.method == "POST":
        bill_name = request.form.get("bill_name")
        due_date = request.form.get("due_date")

        if not bill_name:
            flash("Please enter a bill name.", "danger")
            return redirect(url_for("reminder.reminders"))

        new_reminder = Reminder(
            user_id=session["user_id"],
            bill_name=bill_name,
            due_date=due_date,
            status="Pending"
        )
        db.session.add(new_reminder)
        db.session.commit()
        flash("Reminder Added Successfully", "success")
        return redirect(url_for("reminder.reminders"))

    user_reminders = Reminder.query.filter_by(user_id=session["user_id"]).all()
    return render_template("reminder.html", reminders=user_reminders)


@reminder_bp.route("/reminders/mark_paid/<int:reminder_id>")
@login_required
def mark_paid(reminder_id):
    r = Reminder.query.filter_by(reminder_id=reminder_id, user_id=session["user_id"]).first()
    if r:
        r.status = "Paid"
        db.session.commit()
        flash("Reminder Status Updated Successfully", "success")
    return redirect(url_for("reminder.reminders"))
