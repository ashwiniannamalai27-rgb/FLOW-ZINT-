from models.expense import Expense
from models.budget import Budget
from models.saving import Saving


def credit_suggestions(user_id):

    suggestions = []

    budgets = Budget.query.filter_by(user_id=user_id).all()
    expenses = Expense.query.filter_by(user_id=user_id).all()
    savings = Saving.query.filter_by(user_id=user_id).all()

    total_budget = sum(b.monthly_limit for b in budgets)
    total_expense = sum(e.amount for e in expenses)
    total_savings = sum(s.amount for s in savings)

    # Budget usage
    if total_budget > 0:

        ratio = total_expense / total_budget

        if ratio > 0.9:
            suggestions.append(
                "Reduce monthly spending to improve financial stability."
            )

    # Savings
    if total_savings < total_budget * 0.2:
        suggestions.append(
            "Increase your savings to build a strong financial profile."
        )

    suggestions.append(
        "Always pay EMIs and bills on time."
    )

    suggestions.append(
        "Avoid unnecessary loans."
    )

    suggestions.append(
        "Keep your credit utilization below 30%."
    )

    return suggestions