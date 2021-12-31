"""CRUD operations."""

from model import db, Food, TitleIngredient, Grain, Protein, Additive, Preservative, connect_to_db
import uuid

# Food functions

# def update_food(food):

#     db.session.add(food)
#     db.session.commit()

def create_food(product_name):
    """Create and return a new food"""

    uuid_id = str(uuid.uuid4())
    food = Food(food_id=uuid_id, product_name=product_name)

    db.session.add(food)
    db.session.commit()

    return food

def add_title_ingredients_to_food(food, title_ingredient):

    food.title_ingredients.append(title_ingredient)

    db.session.add(food)
    db.session.commit()
    
def add_grain_to_food(food, grain):

    food.grains.append(grain)

    db.session.add(food)
    db.session.commit()

def add_additive_to_food(food, additive):

    food.additives.append(additive)

    db.session.add(food)
    db.session.commit()

def add_protein_to_food(food, protein):

    food.proteins.append(protein)

    db.session.add(food)
    db.session.commit()

def add_preservative_to_food(food, preservative):

    food.preservatives.append(preservative)

    db.session.add(food)
    db.session.commit()


def add_descriptor_to_title_ingredient(title_ingredient, descriptor):

    title_ingredient.descriptor = descriptor 

    db.session.add(title_ingredient)
    db.session.commit()

def get_food_by_id(food_id):
    """get the food by its id/url ending"""

    return Food.query.get(food_id)

def get_food_by_product_name(product_name):
    """get the food by its name"""

    return Food.query.filter_by(product_name = 'product_name').all()

#Ingredient functions (to be automated in crud.py)
def create_title_ingredient(title_ingredient_name, descriptor, details):
    """create a title ingredient"""

    title_ingredient = TitleIngredient(title_ingredient_name=title_ingredient_name,
                                    descriptor=descriptor, details=details)

    db.session.add(title_ingredient)
    db.session.commit()

    return title_ingredient

def get_title_ingredient_by_id(title_id):
    """get the title ingredient by its id"""

    return TitleIngredient.query.get(title_id)

def get_details_by_ingredient_name_and_descriptor(ingredient_name, descriptor):
    """get the details by its name & descriptor"""

    title_type = TitleIngredient.query.filter(TitleIngredient.title_ingredient_name == ingredient_name,
                                            TitleIngredient.descriptor == descriptor).one()

    return title_type

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
# def create_food_ingredient(food, ingredient):
#     """create a food ingredient"""

    # if grain is None:
    #     grain_id = None
    # else:
    #     grain_id = grain.grain_id

    # if additive is None:
    #     additive_id = None
    # else:
    #     additive_id = additive.additive_id

    # if protein is None:
    #     protein_id = None
    # else:
    #     protein_id = protein.protein_id

    # if preservative is None:
    #     preservative_id = None
    # else:
    #     preservative_id = preservative.preservative_id

    # food_ingredient = FoodIngredient(food_id=food.food_id, ingredient_id=ingredient.ingredient_id)

    # db.session.add(food_ingredient)
    # db.session.commit()

    # return food_ingredient

# def get_food_ingredient(food_ingredient_id):
#     """get the food ingredient by its id"""

#     return FoodIngredient.query.get(food_ingredient_id)

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