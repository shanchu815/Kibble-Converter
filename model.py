"""Models for MVP."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Food(db.Model):
    """A pet food."""

    __tablename__ = 'foods'

    food_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    product_name = db.Column(db.String)
    brand_name = db.Column(db.String)
    ing_id = db.Column(db.Integer,
                        autoincrement=True)

    brands = db.relationship('Brand', backref='foods')
    ingredients = db.relationship('Ingredient', backref='foods')

    def __repr__(self):
        return f'<Food product name={self.product_name} food id={self.food_id}>'



class Brand(db.Model):
    """A brand of pet food."""

    __tablename__ = 'brands'

    brand_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String,
                        db.ForeignKey('foods.brand_name'))
    product_name = db.Column(db.String,
                        db.ForeignKey('foods.product_name'))
    ing_id = db.Column(db.Integer,
                        db.ForeignKey('foods.ing_id'))

    ingredients = db.relationship('Ingredient', backref='brands')

    def __repr__(self):
        return f'<Brand name={self.name} brand id={self.brand_id}>'


class Ingredient(db.Model):
    """An ingredient label"""

    __tablename__ = 'ingredients'

    label_id = db.Column(db.Integer,
                        db.ForeignKey('foods.ing_id'),
                        primary_key=True)
    title_id = db.Column(db.Integer,
                        autoincrement=True)
    sub_id = db.Column(db.Integer,
                        autoincrement=True)
    ing_1 = db.Column(db.String)
    ing_2 = db.Column(db.String)
    ing_3 = db.Column(db.String)
    ing_4 = db.Column(db.String)
    ing_5 = db.Column(db.String)

    # fillers = db.relationship('Filler', backref='ingredients')
    title_ingredients = db.relationship('TitleIngredient', backref='ingredients')
    subtitle_ingredients = db.relationship('SubtitleIngredient', backref='ingredients')

    def __repr__(self):
        return f'<Ingredient ingredient label={self.label_id} title id={self.title_id}>'

class Filler(db.Model):
    """A filler ingredient"""

    __tablename__ = 'fillers'

    filler_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    label_name = db.Column(db.String)
    common_name = db.Column(db.String)
    impact = db.Column(db.String)
    related_descriptor = db.Column(db.String)

    def __repr__(self):
        return f'<Filler filler_id={self.filler_id} common name={self.common_name}>'

class TitleIngredient(db.Model):
    """A title ingredient"""

    __tablename__ = 'title_ingredients'

    title_id = db.Column(db.Integer,
                        db.ForeignKey('ingredients.title_id'),
                        primary_key=True)
    descriptor = db.Column(db.String)
    ing_1_name = db.Column(db.String)
    content_1 = db.Column(db.Float)
    ing_2_name = db.Column(db.String)
    content_2 = db.Column(db.Float)
    ing_3_name = db.Column(db.String)
    content_3 = db.Column(db.Float)

    def __repr__(self):
        return f'<Title title_id={self.title_id} ingredient 1 name={self.ing_1_name}>'

class SubtitleIngredient(db.Model):
    """A subtitle ingredient"""

    __tablename__ = 'subtitle_ingredients'

    sub_id = db.Column(db.Integer,
                        db.ForeignKey('ingredients.sub_id'),
                        primary_key=True)
    descriptor = db.Column(db.String)
    ing_1_name = db.Column(db.String)
    content_1 = db.Column(db.Float)
    ing_2_name = db.Column(db.String)
    content_2 = db.Column(db.Float)
    ing_3_name = db.Column(db.String)
    content_3 = db.Column(db.Float)

    def __repr__(self):
        return f'<Subtitle sub_id={self.sub_id} ingredient 1 name={self.ing_1_name}>'


def connect_to_db(flask_app, db_uri="postgresql:///fillers", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    #if this is set to False instead of echo, terminal will not show huge long loading data
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
