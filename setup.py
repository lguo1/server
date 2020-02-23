import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Organizer(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    contact = db.Column(db.String(20), nullable=False)
    overview = db.Column(db.Text, nullable=False)
    events = db.relationship('Event', backref='Organizer', lazy='dynamic')
    proposals = db.relationship('Proposal', backref='Organizer', lazy='dynamic')
    subscriptions = db.relationship('Subscription', backref='Organizer', lazy='dynamic')
    @property
    def represent(self):
        return {
        "id": self.id,
        "overview": self.overview,
        "subscribed": False}

class Event(db.Model):
    id = db.Column(db.String(10), primary_key=True, nullable=False)
    speakerHome = db.Column(db.String(50), nullable=False)
    speaker = db.Column(db.String(50), nullable=False)
    speakerTitle = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), default="")
    weekday = db.Column(db.String(50), default="")
    date = db.Column(db.String(50), default="TBD")
    season = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(50), nullable=False)
    imageNameHome = db.Column(db.String(50), nullable=False)
    imageNameDetail = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False, default="...")
    category = db.Column(db.String(10), nullable=False)
    decided = db.Column(db.Boolean, nullable=False)
    red = db.Column(db.Float, nullable=False)
    green = db.Column(db.Float, nullable=False)
    blue = db.Column(db.Float, nullable=False)
    start = db.Column(db.String(50), nullable=False)
    end = db.Column(db.String(50), nullable=False)
    organizer = db.Column(db.String(20), db.ForeignKey('organizer.id'), nullable=False)
    bundle = db.Column(db.String(20))
    background = db.Column(db.String(20))
    funding = db.Column(db.Boolean, default=False)
    @property
    def represent(self):
        return {
        "id": self.id,
        "speaker": self.speaker,
        "speakerHome": self.speakerHome,
        "speakerTitle": self.speakerTitle,
        "time": self.time,
        "weekday": self.weekday,
        "date": self.date,
        "season": self.season,
        "year": self.year,
        "imageNameHome": self.imageNameHome,
        "imageNameDetail": self.imageNameDetail,
        "start": self.start,
        "end": self.end,
        "category": self.category,
        "location": self.location,
        "description": self.description,
        "decided": self.decided,
        "red": self.red,
        "green": self.green,
        "blue": self.blue,
        "organizer": self.organizer,
        "bundle": self.bundle,
        "backgroud": self.background,
        "funding": self.funding,
        "interest": False}

class Feedback(db.Model):
    __tablename__ = 'Feedback'
    datetime = db.Column(db.DateTime, primary_key=True,
        default=datetime.utcnow)
    email = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Login(db.Model):
    __tablename__ = 'Login'
    datetime = db.Column(db.DateTime, primary_key=True,
        default=datetime.utcnow)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

class Proposal(db.Model):
    __tablename__ = 'Proposal'
    datetime = db.Column(db.DateTime, primary_key=True,
        default=datetime.utcnow)
    email = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    organizer = db.Column(db.String(20), db.ForeignKey('organizer.id'), nullable=False)

class Subscription(db.Model):
    __tablename__ = 'Subscription'
    datetime = db.Column(db.DateTime, primary_key=True,
        default=datetime.utcnow)
    email = db.Column(db.String(20), nullable=False)
    organizer = db.Column(db.String(20), db.ForeignKey('organizer.id'), nullable=False)


db.create_all()
