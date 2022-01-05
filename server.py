from flask import Flask, request, render_template, redirect
from model import connect_to_db
import crud
import os
# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)
# A secret key is needed to use Flask sessioning features
app.secret_key = 'W33d1sl33t1845!'
cat_key = os.environ['key']

@app.route('/')
def start_here():
    """Home page."""

    return render_template("homepage.html")

@app.route("/disclaimer")
def show_disclaimer():
    """Shows the disclaimer."""

    return render_template("disclaimer.html")

@app.route("/calculator")
def calculate():
    """Shows the protein calculator page."""

    return render_template("calculator.html")

@app.route("/fillout")
def fill_out():
    """Shows the fillout form"""

    return render_template("fillout.html")

@app.route("/save-list", methods = ['POST'])
def save_choices():
    """Saves the chosen form options as a new food object"""

    product_name = request.form.get("product_name")
    ingredient_name = request.form.get("ingredient_name")
    descriptor = request.form.get("descriptor")
    grain = request.form.get("grains")
    additive = request.form.get("additives")
    protein = request.form.get("proteins") 
    preservative = request.form.get("preservatives")

    if (product_name is not None and
        ingredient_name is not None and 
        descriptor is not None):
         
        new_food = crud.create_food(product_name)
        crud.add_title_ingredients_to_food(new_food, crud.get_details_by_ingredient_name_and_descriptor(ingredient_name, descriptor))

        if grain is not None:
            crud.add_grain_to_food(new_food, crud.get_grain_by_id(grain))
        if additive is not None:
            crud.add_additive_to_food(new_food, crud.get_additive_by_id(additive))
        if protein is not None:
            crud.add_protein_to_food(new_food, crud.get_protein_by_id(protein))
        if preservative is not None:
            crud.add_preservative_to_food(new_food, crud.get_preservative_by_id(preservative))

    else:
        return redirect('/fillout')

    return redirect('/results/' + new_food.food_id)

@app.route('/results/<food_id>')
def show_result(food_id):
    """Displays the choices as a unique shareable result page"""

    if not crud.get_food_by_id(food_id):
        return "Invalid id"
    else:        
        food = crud.get_food_by_id(food_id)

        return render_template("result.html", food = food)

@app.route('/api/get_cat_image')
def get_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search?format=src&size=full&mime_types=png,jpg&api_key='
    cat_pic_url = url + cat_key

    return cat_pic_url


"""Cat photo api"""
#x-api-key = 74a565ba-44ea-412b-b5e2-845bf9f18314
"""Use it as the 'x-api-key' header when making any request to the API, 
or by adding as a query string parameter e.g. 
'api_key=74a565ba-44ea-412b-b5e2-845bf9f18314'"""
# https://docs.thecatapi.com/example-by-type
# https://api.thecatapi.com/v1/images/search?format=src&size=full&mime_types=png,jpg&api_key=YOUR-API-KEY
# this doesn't return a json object, it literally just returns a random image url

#Random Dog fact api
"""https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all to get all the facts at once.
Change all to parameter ?number= to specify the number of facts you want to receive."""
# https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1 returns:
# [
#   {
#       "fact": "Many foot disorders in dogs are caused by long toenails."
#   }
# ]

"""Random Cat fact api"""
# https://catfact.ninja/fact?max_length=140 returns:
# {"fact":"The Cat Fanciers Association (CFA) recognizes 44 breeds of cats.","length":64}

# Example request: curl --location --request GET 'https://catfact.ninja/fact?max_length=140' \
# --header 'Accept: application/json'

"""Random Dog photo api"""
# https://dog.ceo/api/breeds/image/random returns:
# {
#     "message": "https://images.dog.ceo/breeds/redbone/n02090379_1448.jpg",
#     "status": "success"
# }

if __name__ == '__main__':
    from model import connect_to_db
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
