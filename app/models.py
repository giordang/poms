from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    poms = db.relationship('Poms', backref='athlete', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Poms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tense = db.Column(db.Integer)
    angry = db.Column(db.Integer)
    wornOut = db.Column(db.Integer)
    unhappy = db.Column(db.Integer)
    proud = db.Column(db.Integer)
    lively = db.Column(db.Integer)
    confused = db.Column(db.Integer)
    sad = db.Column(db.Integer)
    active = db.Column(db.Integer)
    onEdge = db.Column(db.Integer)
    grouchy = db.Column(db.Integer)
    ashamed = db.Column(db.Integer)
    energetic = db.Column(db.Integer)
    hopeless = db.Column(db.Integer)
    uneasy = db.Column(db.Integer)
    restless = db.Column(db.Integer)
    unableToConcentrate = db.Column(db.Integer)
    fatigued = db.Column(db.Integer)
    competent = db.Column(db.Integer)
    annoyed = db.Column(db.Integer)
    discouraged = db.Column(db.Integer)
    resentful = db.Column(db.Integer)
    nervous = db.Column(db.Integer)
    miserable = db.Column(db.Integer)
    confident = db.Column(db.Integer)
    bitter = db.Column(db.Integer)
    exhausted = db.Column(db.Integer)
    anxious = db.Column(db.Integer)
    helpless = db.Column(db.Integer)
    weary = db.Column(db.Integer)
    satisfied = db.Column(db.Integer)
    bewildered = db.Column(db.Integer)
    furious = db.Column(db.Integer)
    fullOfPep = db.Column(db.Integer)
    worthless = db.Column(db.Integer)
    forgetful = db.Column(db.Integer)
    vigorous = db.Column(db.Integer)
    uncertainAboutThings = db.Column(db.Integer)
    bushed = db.Column(db.Integer)
    embarrassed = db.Column(db.Integer)
    tenSum = db.Column(db.Integer)
    angSum = db.Column(db.Integer)
    fatSum = db.Column(db.Integer)
    depSum = db.Column(db.Integer)
    eraSum = db.Column(db.Integer)
    vigSum = db.Column(db.Integer)
    conSum = db.Column(db.Integer)
    tmdSum = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.tense)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))