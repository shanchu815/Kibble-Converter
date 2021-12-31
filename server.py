from flask import Flask, request, render_template, jsonify, redirect
from model import connect_to_db
import crud
# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# A secret key is needed to use Flask sessioning features

app.secret_key = 'W33d1sl33t1845!'

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
        descriptor is not None and 
        grain is not None and
        additive is not None and
        protein is not None and
        preservative is not None):
         
        new_food = crud.create_food(product_name)
    
        crud.add_title_ingredients_to_food(new_food, crud.get_details_by_ingredient_name_and_descriptor(ingredient_name, descriptor))
        crud.add_grain_to_food(new_food, crud.get_grain_by_id(grain))
        crud.add_additive_to_food(new_food, crud.get_additive_by_id(additive))
        crud.add_protein_to_food(new_food, crud.get_protein_by_id(protein))
        crud.add_preservative_to_food(new_food, crud.get_preservative_by_id(preservative))

    else:
        return redirect('/fillout')

    # new_food_ingredient = food.grains.append(new_food, ingredient_type, 
    #                                                 grain_type, additive_type, 
    #                                                 protein_type, preservative_type)

    return redirect('/results/' + new_food.food_id)

@app.route('/results/<food_id>')
def show_result(food_id):
    """Displays the choices as a unique shareable result page"""

    if not crud.get_food_by_id(food_id):
        return "Invalid id"
    else:
        
        food = crud.get_food_by_id(food_id)

        print(food)
        print(food.title_ingredients)
        # message = f"Your pet food is {pet_food.product_name}." 
    
        # for ingredient in pet_food.ingredients:
            # message = message + f"""Since it uses the {ingredient.descriptor} rule , 
            # it {ingredient.details}."""

        return render_template("result.html", food = food)


if __name__ == '__main__':
    from model import connect_to_db
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
