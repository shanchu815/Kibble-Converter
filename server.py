from flask import Flask, request, render_template, jsonify, redirect, url_for
import uuid

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
    """Saves the chosen form options"""
    
    random_id = str(uuid.uuid4())

    # Juvian on discord said: since you already have a db,
    # you should just add+commit instead of write to file and just query instead of read file
    # so basically i need to call the crud functions that create a new food

    #the Food class is going to need random_id as a key if i'm going to use it to pull it from the db

    # with open("db.json", "w+") as f:
    #     try:
    #         info = json.load(f)
    #     except:
    #         info = {}
    #     info[random_id] = [request.form.get('ing1'), request.form.get('ing2')]
    #     json.dump(info, f)

    # name = request.form.get("p_name")
    # d_key = request.form.get("descriptor")
    # first = request.form.get("ing1")
    # second = request.form.get("ing2")
    # third = request.form.get("ing3")
    # fourth = request.form.get("ing4")
    # fifth = request.form.get("ing5")
    # title_1 = request.form.get("title_1")
    # title_2 = request.form.get("title_2")
    # title_3 = request.form.get("title_3")
    # cereal = request.form.get("cereals")
    # other = request.form.get("others")
    # protein = request.form.get("proteins")
    # preserv = request.form.get("preserv")

    return redirect(url_for('/results/') + random_id)

@app.route('/results/<random_id>')
def show_result(random_id):
    """Displays the choices as a result page"""
    
    # with open("db.json", "r") as f:
    #     try:
    #         info = json.load(f)
    #     except:
    #         info = {}
    if random_id not in info:
        return "Invalid id"
    else:
        return render_template("results.html", ingredients = info[random_id])

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")

    # cer = f"{ing_data[cereal]['name']}: {ing_data[cereal]['effect']}, {ing_data[cereal]['details']}"
    # oth = f"{ing_data[other]['name']}: {ing_data[other]['effect']}, {ing_data[other]['details']}"
    # pro = f"{ing_data[protein]['name']}: {ing_data[protein]['effect']}, {ing_data[protein]['details']}"
    # pres = f"{ing_data[preserv]['name']}: {ing_data[preserv]['effect']}, {ing_data[preserv]['details']}"

    # ings = []
    # if title_2 != 2.0:
    #     ings.append(title_2)
    # if title_3 != 3.0:
    #     ings.append(title_3)

    # if d_key == "dinner":
    #     description = f"The product contains at least 25% {title_1} up to a maximum of 95%. Not counting water content, the minimum is 10%. Other named ingredients: {ings} must be at least 3% each."
    # else:
    #     description = f"The product contains at least {contents[d_key]['ing_min']}% {title_1}."


beef/deer	none	    This is 95% beef/deer minimum.							
beef/deer	with/dinner	This is 25-95% beef/deer. Ingredients named afterwards make up at least 3% each.							
beef/deer	flavor	    This is 0% actual beef/deer. There may be stock or some other substitute used.		

https://gyazo.com/a97f69d97d959b6fffd2f550ebf294c9