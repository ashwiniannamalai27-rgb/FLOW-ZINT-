from models.expense import Expense
from models.budget import Budget
from models.saving import Saving

from ai.recommendation import generate_recommendations
from ai.score_calculator import calculate_score


def generate_monthly_report(user_id):

    budgets = Budget.query.filter_by(user_id=user_id).all()
    expenses = Expense.query.filter_by(user_id=user_id).all()
    savings = Saving.query.filter_by(user_id=user_id).all()

    total_budget = sum(b.monthly_limit for b in budgets)
    total_expense = sum(e.amount for e in expenses)
    total_savings = sum(s.amount for s in savings)

    report = {
        "budget": total_budget,
        "expense": total_expense,
        "savings": total_savings,
        "recommendations": generate_recommendations(user_id),
        "wellness": calculate_score(user_id)
    }

    return report