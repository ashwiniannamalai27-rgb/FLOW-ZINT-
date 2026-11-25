from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from models.investment import Investment
from utils.auth_utils import login_required

investment_bp = Blueprint("investment", __name__)


def get_recommendation(risk_level):
    risk = risk_level.lower()
    if risk == "low":
        return "Fixed Deposit (FD), Public Provident Fund (PPF), Government Bonds"
    elif risk == "medium":
        return "Mutual Funds, Index Funds, Balanced Funds"
    elif risk == "high":
        return "Stocks, ETFs, Cryptocurrency (High Risk)"
    else:
        return "Invalid Risk Level"


@investment_bp.route("/investments", methods=["GET", "POST"])
@login_required
def investments():
    if request.method == "POST":
        risk_level = request.form.get("risk_level")
        recommendation = get_recommendation(risk_level)

        new_inv = Investment(user_id=session["user_id"], risk_level=risk_level, recommendation=recommendation)
        db.session.add(new_inv)
        db.session.commit()
        flash("Investment Recommendation Saved Successfully", "success")
        return redirect(url_for("investment.investments"))

    user_investments = Investment.query.filter_by(user_id=session["user_id"]).all()
    return render_template("investment.html", investments=user_investments)
