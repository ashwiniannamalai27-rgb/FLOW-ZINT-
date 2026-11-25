from database import db


class Investment(db.Model):
    __tablename__ = "investments"
    investment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    risk_level = db.Column(db.String(20))
    recommendation = db.Column(db.String(255))
