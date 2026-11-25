from database import db


class Saving(db.Model):
    __tablename__ = "savings"
    saving_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    saving_date = db.Column(db.String(20))
