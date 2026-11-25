from app import app
from models.user import User

with app.app_context():
    users = User.query.all()

    if not users:
        print("No users found.")
    else:
        for user in users:
            print("----------------------------")
            print("ID:", user.id)
            print("Name:", user.full_name)
            print("Email:", user.email)
            print("Phone:", user.phone)