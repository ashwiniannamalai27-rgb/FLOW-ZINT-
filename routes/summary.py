from flask import Blueprint, render_template, session
from models.budget import Budget
from models.expense import Expense
from utils.auth_utils import login_required

summary_bp = Blueprint("summary", __name__)


@summary_bp.route("/summary")
@login_required
def summary():

    # Get all budgets for the logged-in user
    budgets = Budget.query.filter_by(user_id=session["user_id"]).all()

    # Get all expenses for the logged-in user
    expenses = Expense.query.filter_by(user_id=session["user_id"]).all()

    # Calculate totals
    total_budget = sum(b.monthly_limit for b in budgets)
    total_expenses = sum(e.amount for e in expenses)

    remaining = total_budget - total_expenses

    if total_expenses <= total_budget:
        status = "Within Budget"
    else:
        status = "Budget Exceeded"

    # Report dictionary for charts
    report = {
        "budget": total_budget,
        "expense": total_expenses,
        "savings": remaining,
        "status": status
    }

    return render_template(
        "summary.html",
        report=report,
        total_budget=total_budget,
        total_expenses=total_expenses,
        remaining=remaining,
        status=status
    )