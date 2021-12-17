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


