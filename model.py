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

    ingredients = db.relationship('Ingredient', secondary='food_ingredients', backref='foods')

    def __repr__(self):
        return f'<Food product name={self.product_name} food id={self.food_id}>'

class FoodIngredient(db.Model):
    """An ingredient that's in this specific food"""

    __tablename__ = 'food_ingredients'

    food_ingredient_id = db.Column(db.Integer,
                                autoincrement=True,
                                primary_key=True)
    food_id = db.Column(db.Integer,
                        db.ForeignKey('foods.food_id'))
    ingredient_id = db.Column(db.Integer,
                        db.ForeignKey('ingredients.ingredient_id'))

class Ingredient(db.Model):
    """An ingredient label"""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    ingredient_name = db.Column(db.String)
    obscure_name = db.Column(db.Boolean) # True if this ingredient is of concern (like a chemical), else false
    descriptor = db.Column(db.String)
    min_percentage = db.Column(db.Float)
    max_percentage = db.Column(db.Float)

    ingredient_data = db.relationship('IngredientData', backref='ingredients')

    def __repr__(self):
        return f'<Ingredient ingredient label={self.label_id} title id={self.title_id}>'

class IngredientData(db.Model):
    """Data on obscure ingredients"""

    __tablename__ = 'ingredients_data'

    ingredient_id = db.Column(db.Integer,
                            db.ForeignKey('ingredients.ingredient_id'),
                            primary_key=True)
    true_name = db.Column(db.String)

    ingredient = db.relationship('Ingredient', backref='ingredients_data')


    def __repr__(self):
        return f'<IngredientData ingredient_id={self.ingredient_id} True name={self.true_name}>'

def connect_to_db(flask_app, db_uri="postgresql:///pet_food", echo=True):
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

#relationships:
#a brand can have many foods, a food can have many brands (many to many)
#ie: how every brand has a generic "chicken dog food"
#ingredients to food (many to many)
#ie: this food has chicken, corn & soy AND chicken is in many different foods
#ingredients to ingredient data (one to many)
