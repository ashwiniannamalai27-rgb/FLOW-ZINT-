from database import db


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    age = db.Column(db.Integer)
    occupation = db.Column(db.String(100))
    monthly_income = db.Column(db.Float)
    city = db.Column(db.String(100))
    marital_status = db.Column(db.String(20))
    dependents = db.Column(db.Integer)
