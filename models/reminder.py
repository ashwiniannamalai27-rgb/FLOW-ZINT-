from database import db


class Reminder(db.Model):
    __tablename__ = "reminders"
    reminder_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    bill_name = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.String(20))
    status = db.Column(db.String(20), default="Pending")
