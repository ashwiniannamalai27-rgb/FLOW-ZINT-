from models.expense import Expense


def fraud_alerts(user_id):

    alerts = []

    expenses = Expense.query.filter_by(user_id=user_id).all()

    if not expenses:
        alerts.append("No transactions found.")
        return alerts

    # Check for unusually high transactions
    for expense in expenses:

        if expense.amount > 50000:
            alerts.append(
                f"⚠️ High-value transaction detected: ₹{expense.amount}"
            )

    # Check for repeated amounts
    amount_count = {}

    for expense in expenses:
        amount_count[expense.amount] = amount_count.get(expense.amount, 0) + 1

    for amount, count in amount_count.items():

        if count >= 3:
            alerts.append(
                f"⚠️ Multiple transactions of ₹{amount} detected."
            )

    if len(alerts) == 0:
        alerts.append(
            "✅ No suspicious financial activity detected."
        )

    return alerts