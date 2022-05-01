from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    Video = db.Column(db.Text, primary_key=True)
    Metadata = db.Column(db.String, unique=True, nullable=False)
    Frame = db.Column(db.String, unique=True, nullable=False)


db.session.add(User(name="Flask", email="example@example.com"))
db.session.commit()

users = User.query.all()

