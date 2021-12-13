"""CRUD operations."""

from model import db, Food, Brand, Ingredient, BrandFood, FoodIngredient, IngredientData, connect_to_db

# Functions start here!


if __name__ == '__main__':
    from server import app
    connect_to_db(app)