from models.profile import Profile
from models.saving import Saving


def insurance_recommendation(user_id):

    advice = []

    profile = Profile.query.filter_by(user_id=user_id).first()
    savings = Saving.query.filter_by(user_id=user_id).all()

    total_savings = sum(s.amount for s in savings)

    advice.append(
        "Health insurance is recommended for everyone."
    )

    if total_savings > 100000:
        advice.append(
            "Consider purchasing life insurance to protect your family's future."
        )

    if total_savings > 300000:
        advice.append(
            "Property insurance may help protect valuable assets."
        )

    if profile:
        advice.append(
            "Review your insurance coverage every year."
        )

    return advice