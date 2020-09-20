from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


class User(Base, UserMixin):
    __tablename__ = 'users'

    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self,username,password):
        self.username = username
        self.set_password(password)


class Recipe(Base):
    __tablename__ = 'recipes'

    name = db.Column(db.String(255), nullable=False)


class Pick(Base):
    __tablename__ = 'picks'

    number = db.Column(db.String(255),nullable=False)
    barcode = db.Column(db.String(255), nullable=True)

class RecipePick(Base):
    __tablename__ = 'recipe_pick'

    recipe_id = db.Column(db.Integer,db.ForeignKey('recipes.id',ondelete="SET NULL"),nullable=True)
    recipe = db.relationship('Recipe', backref="recipe_pick")
    pick_id = db.Column(db.Integer,db.ForeignKey('picks.id',ondelete="SET NULL"),nullable=True)
    pick = db.relationship('Pick', backref="recipe_pick")
    order = db.Column(db.Integer,nullable=False)