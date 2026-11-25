from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from models.saving import Saving
from utils.auth_utils import login_required
from datetime import date

saving_bp = Blueprint("saving", __name__)


@saving_bp.route("/savings", methods=["GET", "POST"])
@login_required
def savings():
    if request.method == "POST":
        amount = request.form.get("amount")
        if not amount:
            flash("Please enter an amount.", "danger")
            return redirect(url_for("saving.savings"))

        new_saving = Saving(user_id=session["user_id"], amount=float(amount), saving_date=str(date.today()))
        db.session.add(new_saving)
        db.session.commit()
        flash("Saving Added Successfully", "success")
        return redirect(url_for("saving.savings"))

    user_savings = Saving.query.filter_by(user_id=session["user_id"]).all()
    total = sum(s.amount for s in user_savings)
    return render_template("saving.html", savings=user_savings, total=total)
