from app import db
from datetime import datetime

# 这个是设计数据库表的，所谓的“model”

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('Post',backref='author',lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)   

'''
    The __repr__ method tells Python how to print objects of this class, which is going to be useful for debugging. You can see the __repr__() method in action in the Python interpreter session below:

    >>> from app.models import User
    >>> u = User(username='susan', email='susan@example.com')
    >>> u
    <User susan> 
'''

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)