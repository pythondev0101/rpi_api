from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


class User(Base):
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


recipe_ingredients = db.Table('recipe_ingredients',
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
)


class Recipe(Base):
    __tablename__ = 'recipes'

    name = db.Column(db.String(255), nullable=False)


class Ingredient(Base):
    __tablename__ = 'ingredients'

    number = db.Column(db.Integer,nullable=False)
    # barcode, 