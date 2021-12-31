''' Automates all database functions.'''
import os
import json
import crud
import model
import server
import random

os.system('dropdb pet_food')
os.system('createdb pet_food')

model.connect_to_db(server.app)
model.db.create_all()


with open('data/data.json') as f:
    ingredient_data = json.loads(f.read())

grain_list = ingredient_data[0]["grains"]
additive_list = ingredient_data[0]["additives"]
preservative_list = ingredient_data[0]["preservatives"]
protein_list = ingredient_data[0]["proteins"]
ingredient_list = ingredient_data[0]["ingredients"]

# movies in db = []

for grain in grain_list:

    grain_id = grain['grain_id']
    name = grain['name']
    effect = grain['effect']
    details = grain['details']

    crud.create_grain(grain_id, name, effect, details)

for additive in additive_list:

    additive_id = additive['additive_id']
    name = additive['name']
    effect = additive['effect']
    details = additive['details']

    crud.create_additive(additive_id, name, effect, details)

for preservative in preservative_list:

    preservative_id = preservative['preservative_id']
    name = preservative['name']
    effect = preservative['effect']
    details = preservative['details']

    crud.create_preservative(preservative_id, name, effect, details)

for protein in protein_list:

    protein_id = protein['protein_id']
    name = protein['name']
    effect = protein['effect']
    details = protein['details']

    crud.create_protein(protein_id, name, effect, details)

for ingredient in ingredient_list:

    name = ingredient['name']
    descriptor = ingredient['descriptor']
    details = ingredient['details']

    crud.create_title_ingredient(name, descriptor, details)

for food_index in range(4):

    title_ingredient = random.choice(model.TitleIngredient.query.all())
    grain = random.choice(model.Grain.query.all())
    protein = random.choice(model.Protein.query.all())
    additive = random.choice(model.Additive.query.all())
    preservative = random.choice(model.Preservative.query.all())

    food = crud.create_food("food"+ str(food_index))

    crud.add_title_ingredients_to_food(food, title_ingredient)
    crud.add_grain_to_food(food, grain)
    crud.add_protein_to_food(food, protein)
    crud.add_additive_to_food(food, additive)
    crud.add_preservative_to_food(food, preservative)
