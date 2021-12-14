"""CRUD operations."""

from model import db, Food, Brand, Ingredient, BrandFood, FoodIngredient, IngredientData, connect_to_db

# Functions start here!
def create_food(product_name):
    """Create and return a new food"""

    food = Food(product_name=product_name)

    db.session.add(food)
    db.session.commit()

    return food

def create_brand(brand_name, food):

    brand = Brand(brand_name=brand_name, food=food)

    db.session.add(brand)
    db.session.commit()

    return brand

def create_ingredient(ingredient_name, 
                    food, 
                    obscure_name, 
                    descriptor, 
                    min_percentage, 
                    max_percentage):

    ingredient = Ingredient(ingredient_name=ingredient_name, 
                            food=food, 
                            obscure_name=obscure_name, 
                            descriptor=descriptor, 
                            min_percentage=min_percentage, 
                            max_percentage=max_percentage)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient

def create_brand_food(food, brand):

    brand_food = BrandFood(food=food, brand=brand)

    db.session.add(brand_food)
    db.session.commit()

    return brand_food

def create_food_ingredient(food, ingredient):

    food_ingredient = FoodIngredient(food=food, ingredient=ingredient)

    db.session.add(food_ingredient)
    db.session.commit()

    return food_ingredient

def create_ingredient_data(ingredient, true_name):

    ingredient_data = IngredientData(ingredient=ingredient, true_name=true_name)

    db.session.add(ingredient_data)
    db.session.commit()

    return ingredient_data

if __name__ == '__main__':
    from server import app
    connect_to_db(app)