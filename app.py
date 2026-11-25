from flask import Flask
from database import db
import os

# -------------------- App Setup --------------------
app = Flask(__name__)
app.secret_key = "replace-this-with-something-random-later"

# Absolute path so SQLite always finds the instance folder
basedir = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(basedir, "instance")
os.makedirs(instance_path, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(instance_path, "financial_bot.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# -------------------- Import Models --------------------
from models.user import User
from models.profile import Profile
from models.goal import Goal
from models.budget import Budget
from models.expense import Expense
from models.saving import Saving
from models.investment import Investment
from models.reminder import Reminder

# -------------------- Import & Register Blueprints --------------------
from routes.auth import auth
from routes.profile import profile_bp
from routes.goal import goal_bp
from routes.dashboard import dashboard_bp
from routes.budget import budget_bp
from routes.expense import expense_bp
from routes.saving import saving_bp
from routes.investment import investment_bp
from routes.reminder import reminder_bp
from routes.summary import summary_bp

app.register_blueprint(auth)
app.register_blueprint(profile_bp)
app.register_blueprint(goal_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(budget_bp)
app.register_blueprint(expense_bp)
app.register_blueprint(saving_bp)
app.register_blueprint(investment_bp)
app.register_blueprint(reminder_bp)
app.register_blueprint(summary_bp)

# -------------------- Create Tables --------------------
with app.app_context():
    db.create_all()

# -------------------- Run --------------------
if __name__ == "__main__":
    app.run(debug=True)
