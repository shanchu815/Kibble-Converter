"""CRUD operations."""

from model import db, Food, Ingredient, FoodIngredient, IngredientData, connect_to_db

# Functions start here!
def create_food(product_name):
    """Create and return a new food"""

    food = Food(product_name=product_name)

    db.session.add(food)
    db.session.commit()

    return food

def get_food_by_id(food_id):
    """get the food by its id"""

    return Food.query.get(food_id)

def get_food_by_product_name(product_name):
    """get the food by its name"""

    return Food.query.filter_by(product_name = 'product_name').all()

def create_ingredient(ingredient_name,
                    obscure_name, 
                    descriptor, 
                    min_percentage, 
                    max_percentage):

    """create an ingredient"""

    ingredient = Ingredient(ingredient_name=ingredient_name,
                            obscure_name=obscure_name, 
                            descriptor=descriptor, 
                            min_percentage=min_percentage, 
                            max_percentage=max_percentage)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient

def get_ingredient_by_id(ingredient_id):
    """get the ingredient by its id"""

    return Ingredient.query.get(ingredient_id)

def get_ingredient_by_name(ingredient_name):
    """get the ingredient by its name"""

    return Ingredient.query.filter_by(ingredient_name = 'ingredient_name').all()

def create_food_ingredient(food, ingredient):
    """create a food ingredient"""

    food_ingredient = FoodIngredient(food=food, ingredient=ingredient)

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

def get_food_ingredient_data_by_name(product_name):
    """get all the ingredient data of a food by the product name"""

    current_food = get_food_by_product_name(product_name)
    current_ingredients = current_food.ingredients

    return current_ingredients.ingredient_data

def create_ingredient_data(ingredient, true_name):
    """create data for an ingredient"""

    ingredient_data = IngredientData(ingredient=ingredient, true_name=true_name)

    db.session.add(ingredient_data)
    db.session.commit()

    return ingredient_data

def get_ingredient_data_by_id(ingredient_id):
    """get the ingredient data by the id"""

    return IngredientData.query.get(ingredient_id)

def get_ingredient_data_by_true_name(true_name):
    """get the ingredient data by the true name"""

    return IngredientData.query.filter_by(true_name='true_name').all()

def get_ingredient_data_by_common_name(ingredient_name):
    """get the ingredient data by the common name"""

    ingredient = Ingredient.query.filter_by(ingredient_name='ingredient_name').all()

    return IngredientData.query.get(ingredient.ingredient_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)