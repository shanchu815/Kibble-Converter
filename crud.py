"""CRUD operations."""

from model import db, Food, Ingredient, FoodIngredient, Grain, Protein, Additive, Preservative, connect_to_db
import uuid

# Food functions
def create_food(product_name):
    """Create and return a new food"""

    uuid_id = str(uuid.uuid4())
    food = Food(food_id=uuid_id, product_name=product_name)

    db.session.add(food)
    db.session.commit()

    return food

def get_food_by_id(food_id):
    """get the food by its id/url ending"""

    return Food.query.get(food_id)

def get_food_by_product_name(product_name):
    """get the food by its name"""

    return Food.query.filter_by(product_name = 'product_name').all()

#Ingredient functions (to be automated in crud.py)
def create_ingredient(name, descriptor, details):
    """create an ingredient"""

    ingredient = Ingredient(name=name, descriptor=descriptor, details=details)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient

def get_ingredient_by_id(ingredient_id):
    """get the ingredient by its id"""

    return Ingredient.query.get(ingredient_id)

def get_ingredient_by_combo(name, descriptor):
    """get the ingredient by its name & descriptor"""

    return Ingredient.query.filter_by(name = 'name', descriptor = 'descriptor').all()

def create_grain(grain_id, name, effect, details):
    """create a grain ingredient"""

    grain = Grain(grain_id=grain_id, name=name, effect=effect, details=details)

    db.session.add(grain)
    db.session.commit()

    return grain

def create_additive(additive_id, name, effect, details):
    """create a additive ingredient"""

    additive = Additive(additive_id=additive_id, name=name, effect=effect, details=details)

    db.session.add(additive)
    db.session.commit()

    return additive

def create_preservative(preservative_id, name, effect, details):
    """create a preservative ingredient"""

    preservative = Preservative(preservative_id=preservative_id, name=name, effect=effect, details=details)

    db.session.add(preservative)
    db.session.commit()

    return preservative

def create_protein(protein_id, name, effect, details):
    """create a protein ingredient"""

    protein = Protein(protein_id=protein_id, name=name, effect=effect, details=details)

    db.session.add(protein)
    db.session.commit()

    return protein

def get_grain_by_id(grain_id):
    """get the grain by its id"""

    return Grain.query.get(grain_id)

def get_additive_by_id(additive_id):
    """get the additive by its id"""

    return Additive.query.get(additive_id)

def get_preservative_by_id(preservative_id):
    """get the preservative by its id"""

    return Preservative.query.get(preservative_id)

def get_protein_by_id(protein_id):
    """get the protein by its id"""

    return Protein.query.get(protein_id)

#Food ingredient label function
def create_food_ingredient(food, ingredient, grain, additive, protein, preservative):
    """create a food ingredient"""

    food_ingredient = FoodIngredient(food=food, ingredient=ingredient,
                                    grain=grain, additive=additive,
                                    protein=protein, preservative=preservative)

    db.session.add(food_ingredient)
    db.session.commit()

    return food_ingredient

def get_food_ingredient(food_ingredient_id):
    """get the food ingredient by its id"""

    return FoodIngredient.query.get(food_ingredient_id)

def get_food_ingredients_by_id(food_id):
    """get all the food ingredients of a food by the food id"""

    current_food = get_food_by_id(food_id)

    return current_food.ingredients

def get_food_ingredients_by_name(product_name):
    """get all the food ingredients of a food by the product name"""

    current_food = get_food_by_product_name(product_name)

    return current_food.ingredients

if __name__ == '__main__':
    from server import app
    connect_to_db(app)