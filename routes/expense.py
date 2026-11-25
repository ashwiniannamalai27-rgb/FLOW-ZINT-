from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from models.expense import Expense
from utils.auth_utils import login_required

expense_bp = Blueprint("expense", __name__)


@expense_bp.route("/expenses", methods=["GET", "POST"])
@login_required
def expenses():

    if request.method == "POST":

        category = request.form.get("category")
        amount = request.form.get("amount")
        expense_date = request.form.get("date")

        if not category or not amount or not expense_date:
            flash("Please fill all fields.", "danger")
            return redirect(url_for("expense.expenses"))

        new_expense = Expense(
            user_id=session["user_id"],
            category=category,
            amount=float(amount),
            expense_date=expense_date
        )

        db.session.add(new_expense)
        db.session.commit()

        flash("Expense Added Successfully!", "success")

        return redirect(url_for("expense.expenses"))

    user_expenses = Expense.query.filter_by(
        user_id=session["user_id"]
    ).all()

    total = sum(exp.amount for exp in user_expenses)

    return render_template(
        "expense.html",
        expenses=user_expenses,
        total=total
    )