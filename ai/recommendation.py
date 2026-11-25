from models.expense import Expense
from models.budget import Budget
from models.saving import Saving


def generate_recommendations(user_id):
    recommendations = []

    budgets = Budget.query.filter_by(user_id=user_id).all()
    expenses = Expense.query.filter_by(user_id=user_id).all()
    savings = Saving.query.filter_by(user_id=user_id).all()

    total_budget = sum(b.monthly_limit for b in budgets)
    total_expense = sum(e.amount for e in expenses)
    total_savings = sum(s.amount for s in savings)

    # Expense Check
    if total_expense > total_budget:
        recommendations.append(
            "⚠️ Your expenses are higher than your monthly budget."
        )
    else:
        recommendations.append(
            "✅ Great! You are staying within your budget."
        )

    # Savings Check
    if total_savings < (0.20 * total_budget):
        recommendations.append(
            "💰 Try saving at least 20% of your monthly budget."
        )
    else:
        recommendations.append(
            "🎉 Excellent! Your savings are on track."
        )

    # Spending Habit
    if total_budget > 0:
        ratio = total_expense / total_budget

        if ratio > 0.90:
            recommendations.append(
                "📉 Your spending is very high. Reduce unnecessary expenses."
            )
        elif ratio > 0.70:
            recommendations.append(
                "🙂 Your spending is moderate. Try to save a little more."
            )
        else:
            recommendations.append(
                "🌟 You are managing your money wisely."
            )

    return recommendations