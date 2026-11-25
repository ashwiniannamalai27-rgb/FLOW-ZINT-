from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from models.budget import Budget
from utils.auth_utils import login_required

budget_bp = Blueprint("budget", __name__)


@budget_bp.route("/budget", methods=["GET", "POST"])
@login_required
def budget():
    if request.method == "POST":
        category = request.form.get("category")
        amount = request.form.get("amount")

        if not category or not amount:
            flash("Please fill all fields.", "danger")
            return redirect(url_for("budget.budget"))

        new_budget = Budget(user_id=session["user_id"], category=category, monthly_limit=float(amount))
        db.session.add(new_budget)
        db.session.commit()
        flash("Budget Added Successfully", "success")
        return redirect(url_for("budget.budget"))

    budgets = Budget.query.filter_by(user_id=session["user_id"]).all()
    return render_template("budget.html", budgets=budgets)


@budget_bp.route("/budget/delete/<int:budget_id>")
@login_required
def delete_budget(budget_id):
    b = Budget.query.filter_by(budget_id=budget_id, user_id=session["user_id"]).first()
    if b:
        db.session.delete(b)
        db.session.commit()
        flash("Budget Deleted Successfully", "info")
    return redirect(url_for("budget.budget"))
