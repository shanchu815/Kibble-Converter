"""Models for MVP."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Food(db.Model):
    """A pet food."""

    __tablename__ = 'foods'

    food_id = db.Column(db.String, primary_key=True)
    product_name = db.Column(db.String)

    title_ingredients = db.relationship('TitleIngredient', secondary='food_ingredients', backref='foods')
    grains = db.relationship('Grain', secondary='food_grains', backref='foods')
    additives = db.relationship('Additive', secondary='food_additives', backref='foods')
    proteins = db.relationship('Protein', secondary='food_proteins', backref='foods')
    preservatives = db.relationship('Preservative', secondary='food_preservatives', backref='foods')

    def __repr__(self):
        return f'<Food product name={self.product_name} food id={self.food_id}>'

class FoodIngredient(db.Model):
    """Ingredient combination that's in this specific food"""

    __tablename__ = 'food_ingredients'

    food_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    food_id = db.Column(db.String, db.ForeignKey('foods.food_id'))
    title_id = db.Column(db.Integer, db.ForeignKey('title_ingredients.title_id'))
    # grain_id = db.Column(db.String,
    #                     db.ForeignKey('grains.grain_id'),
    #                     nullable=True)
    # additive_id = db.Column(db.String,
    #                     db.ForeignKey('additives.additive_id'),
    #                     nullable=True)
    # protein_id = db.Column(db.String,
    #                     db.ForeignKey('proteins.protein_id'),
    #                     nullable=True)
    # preservative_id = db.Column(db.String,
    #                     db.ForeignKey('preservatives.preservative_id'),
    #                     nullable=True)

    # grains = db.relationship('Grain', backref='food_ingredients')
    # additives = db.relationship('Additive', backref='food_ingredients')
    # proteins = db.relationship('Protein', backref='food_ingredients')
    # preservatives = db.relationship('Preservative', backref='food_ingredients')

    def __repr__(self):
        return f'<Food ingredients id={self.food_ingredient_id} food id={self.food_id}>'


class TitleIngredient(db.Model):
    """The primary named ingredient & its data"""

    __tablename__ = 'title_ingredients'

    title_id = db.Column(db.Integer, primary_key=True)
    title_ingredient_name = db.Column(db.String)
    descriptor = db.Column(db.String)
    details = db.Column(db.String)

    def __repr__(self):
        return f'<Title id={self.title_id} title ingredient name={self.title_ingredient_name}>'

class FoodGrain(db.Model):
    """Grain that's in this specific food"""

    __tablename__ = 'food_grains'

    food_grain_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    food_id = db.Column(db.String, db.ForeignKey('foods.food_id'), nullable = False)
    grain_id = db.Column(db.String, db.ForeignKey('grains.grain_id'), nullable = False)

class Grain(db.Model):
    """Data on grains"""

    __tablename__ = 'grains'

    grain_id = db.Column(db.String, primary_key=True)
    # food_id = db.Column(db.String,
    #                     db.ForeignKey('foods.food_id'),
    #                     nullable=True)
    name = db.Column(db.String)
    effect = db.Column(db.String)
    details = db.Column(db.String)

    def __repr__(self):
        return f'<Grain grain_id={self.grain_id} grain name={self.name}>'

class FoodAdditive(db.Model):
    """Additive that's in this specific food"""

    __tablename__ = 'food_additives'

    food_additive_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    food_id = db.Column(db.String, db.ForeignKey('foods.food_id'))
    additive_id = db.Column(db.String, db.ForeignKey('additives.additive_id'))

class Additive(db.Model):
    """Data on additives"""

    __tablename__ = 'additives'

    additive_id = db.Column(db.String, primary_key=True)
    # food_id = db.Column(db.String,
    #                     db.ForeignKey('foods.food_id'),
    #                     nullable=True)
    name = db.Column(db.String)
    effect = db.Column(db.String)
    details = db.Column(db.String)

    def __repr__(self):
        return f'<Additive additive_id={self.additive_id} additive name={self.name}>'

class FoodProtein(db.Model):
    """Protein that's in this specific food"""

    __tablename__ = 'food_proteins'

    food_grain_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    food_id = db.Column(db.String, db.ForeignKey('foods.food_id'))
    protein_id = db.Column(db.String, db.ForeignKey('proteins.protein_id'))

class Protein(db.Model):
    """Data on the protein type"""

    __tablename__ = 'proteins'

    protein_id = db.Column(db.String, primary_key=True)
    # food_id = db.Column(db.String,
    #                     db.ForeignKey('foods.food_id'),
    #                     nullable=True)
    name = db.Column(db.String)
    effect = db.Column(db.String)
    details = db.Column(db.String)

    def __repr__(self):
        return f'<Protein protein_id={self.protein_id} protein name={self.name}>'

class FoodPreservative(db.Model):
    """Preservative that's in this specific food"""

    __tablename__ = 'food_preservatives'

    food_preservative_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    food_id = db.Column(db.String, db.ForeignKey('foods.food_id'))
    preservative_id = db.Column(db.String, db.ForeignKey('preservatives.preservative_id'))

class Preservative(db.Model):
    """Data on preservatives"""

    __tablename__ = 'preservatives'

    preservative_id = db.Column(db.String, primary_key=True)
    # food_id = db.Column(db.String,
    #                     db.ForeignKey('foods.food_id'),
    #                     nullable=True)
    name = db.Column(db.String)
    effect = db.Column(db.String)
    details = db.Column(db.String)

    def __repr__(self):
        return f'<Preservative preservative_id={self.preservative_id} preservative name={self.name}>'

def connect_to_db(flask_app, db_uri="postgresql:///pet_food", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    #if this is set to False instead of echo, terminal will not show huge long loading data
    # flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    connect_to_db(app)
