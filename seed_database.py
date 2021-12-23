''' Automates all database functions.'''

import os
import json
import crud
import model
import server

os.system('dropdb pet_food')
os.system('createdb pet_food')

model.connect_to_db(server.app)
model.db.create_all()


with open('data/data.json') as f:
    ingredient_data = json.loads(f.read())

grain_list = ingredient_data[0]["grains"]
additive_list = ingredient_data[1]["additives"]
preservative_list = ingredient_data[2]["preservatives"]
protein_list = ingredient_data[3]["proteins"]
ingredient_list = ingredient_data[4]["ingredients"]

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
    effect = ingredient['effect']
    details = ingredient['details']

    crud.create_ingredient(name, effect, details)