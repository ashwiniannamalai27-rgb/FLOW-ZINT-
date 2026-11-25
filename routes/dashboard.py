from flask import Blueprint, render_template, session
from models.user import User
from models.profile import Profile
from models.goal import Goal
from utils.auth_utils import login_required
from ai.recommendation import generate_recommendations
from ai.score_calculator import calculate_score
from ai.report_generator import generate_monthly_report
from ai.credit_analyzer import credit_suggestions
from ai.fraud_detector import fraud_alerts
from ai.insurance_advisor import insurance_recommendation

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    user = User.query.get(session["user_id"])
    profile = Profile.query.filter_by(user_id=user.id).first()
    goals = Goal.query.filter_by(user_id=user.id).all()

    user_id = session["user_id"]

    recommendations = generate_recommendations(user_id)
    wellness = calculate_score(user_id)
    report = generate_monthly_report(user_id)
    credit = credit_suggestions(user_id)
    fraud = fraud_alerts(user_id)
    insurance = insurance_recommendation(user_id)

    return render_template(
        "dashboard.html",
        user=user,
        profile=profile,
        goals=goals,
        recommendations=recommendations,
        wellness=wellness,
        report=report,
        credit=credit,
        fraud=fraud,
        insurance=insurance
    )