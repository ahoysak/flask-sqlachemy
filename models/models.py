from main import db

class Cars(db.Model):
    brand = db.Column(db.String(20))
    type = db.Column(db.String(20))
    number = db.Column(db.Integer)
    user_id = db.Column(db.Integer, primary_key=True)

class Users(db.Model):
    first_name = db.Column(db.String(15))
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(15))
    email = db.Column(db.String(15))
    password = db.Column(db.String(15))
    nickname = db.Column(db.String(20))
    text = db.Column(db.String(20))

