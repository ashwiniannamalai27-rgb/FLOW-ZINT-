from models.expense import Expense
from models.budget import Budget
from models.saving import Saving


def calculate_score(user_id):

    budgets = Budget.query.filter_by(user_id=user_id).all()
    expenses = Expense.query.filter_by(user_id=user_id).all()
    savings = Saving.query.filter_by(user_id=user_id).all()

    total_budget = sum(b.monthly_limit for b in budgets)
    total_expense = sum(e.amount for e in expenses)
    total_savings = sum(s.amount for s in savings)

    score = 100

    # Budget Check
    if total_expense > total_budget:
        score -= 30

    # Savings Check
    if total_budget > 0:
        saving_percent = (total_savings / total_budget) * 100

        if saving_percent >= 20:
            score += 5
        elif saving_percent >= 10:
            score -= 5
        else:
            score -= 20

    # Spending Ratio
    if total_budget > 0:
        ratio = total_expense / total_budget

        if ratio > 1:
            score -= 10
        elif ratio > 0.8:
            score -= 5

    # Limits
    if score > 100:
        score = 100

    if score < 0:
        score = 0

    # Wellness Level
    if score >= 80:
        status = "Excellent"

    elif score >= 60:
        status = "Good"

    elif score >= 40:
        status = "Average"

    else:
        status = "Needs Improvement"

    return {
        "score": score,
        "status": status
    }