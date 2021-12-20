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


data = data.json()

for d in data:
    i = Ingredient(name=d.name, effect=)

#add ingredient data to ingredients table so it's one big table
#they will have NUll descriptors, but there will now be an effect column in Ingredients
#effect will be NULL for normal ingredients
#min/max percentage will be condensed into the details column for normal ingredients

#change data.json so seed_database.py can read & convert it into Ingredients table

#radio buttons dont allow multiple select - change the form html
#adjust the values of the form options to match the new classes

#add new key to Food class (STR) to store the random_id
#make new function in crud.py to get a Food object by its random_id
