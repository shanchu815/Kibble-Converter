from flask import Flask, request, render_template, jsonify

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


@app.route("/fillout")
def fill_out():
    """Shows the fillout form"""

    return render_template("fillout.html")

@app.route("/result")
def show_results():
    """Shows the results"""
    
    name = request.args.get("brand")
    d_key = request.args.get("descriptor")
    first = request.args.get("ing1")
    second = request.args.get("ing2")
    third = request.args.get("ing3")
    fourth = request.args.get("ing4")
    fifth = request.args.get("ing5")
    title_1 = request.args.get("title_1")
    title_2 = request.args.get("title_2")
    title_3 = request.args.get("title_3")
    cereal = request.args.get("cereals")
    other = request.args.get("others")
    protein = request.args.get("proteins")
    preserv = request.args.get("preserv")

    cer = f"{ing_data[cereal]['name']}: {ing_data[cereal]['effect']}, {ing_data[cereal]['details']}"
    oth = f"{ing_data[other]['name']}: {ing_data[other]['effect']}, {ing_data[other]['details']}"
    pro = f"{ing_data[protein]['name']}: {ing_data[protein]['effect']}, {ing_data[protein]['details']}"
    pres = f"{ing_data[preserv]['name']}: {ing_data[preserv]['effect']}, {ing_data[preserv]['details']}"

    ings = []
    if title_2 != 2.0:
        ings.append(title_2)
    if title_3 != 3.0:
        ings.append(title_3)

    if d_key == "dinner":
        description = f"The product contains at least 25% {title_1} up to a maximum of 95%. Not counting water content, the minimum is 10%. Other named ingredients: {ings} must be at least 3% each."
    else:
        description = f"The product contains at least {contents[d_key]['ing_min']}% {title_1}."

    return render_template("result.html", name=name, description=description,
    first=first, second=second, third=third, fourth=fourth, fifth=fifth,
    cer=cer, oth=oth, pro=pro, pres=pres)

contents = {
    'dinner': {'ing_min': 25,'ing_max': 95,'ing_min_water': 10,'ing2_min': 3,},
    'with': {'ing_min': 3,},
    'flavor': {'ing_min': 0,},
    'no': {'ing_min': 95,},
}

ing_data = {
    'soy': {
      'name': 'Soy',
      'effect': 'Used as a hypoallergenic source of protein & carbs',
      'details': 'Cats can develop allergies to it later in life',
    },
    'corn': {
        'name': 'Corn',
        'effect': 'Used as a source of carbs & fiber',
        'details': 'Metabolizes into sugar in the gut',
    },
    'wheat': {
        'name': 'Wheat',
        'effect': 'Used as a source of carbs',
        'details': 'Common allergen for both dogs & cats',
      },
    'toco': {
        'name': 'Tocopherols (mixed or non-mixed)',
        'effect': 'A food preservative used to add Vitamin E to products',
        'details': 'Your pet may be allergic since its derived sources (veggies, nuts or fish) are not listed on the label',
      },
    'la2p': {
        'name': 'L-ascorbyl-2-polyphosphate',
        'effect': 'Ascorbic acid aka Vitamin C',
        'details': 'There have been no controversies thus far.',
      },  
    'msbc': {
        'name': 'Menadione sodium bisulfate complex',
        'effect': 'A source of Vitamin K3',
        'details': 'A known carcinogenic & also technically illegal since AAFCO only allows it to be used in poultry feed',
      }, 
    'p1': {
        'name': 'Meat',
        'effect': 'Clean muscle (skeletal, tongue, diaphragm, heart, esophagus) from animals',
        'details': 'May or may not include fat, skin, nerves, & blood vessels',
      }, 
    'p2': {
        'name': 'Meat meal',
        'effect': 'Rendered (or processed) product from animal tissues',
        'details': 'Excludes hair, hooves, horn, hide, manure, or GI contents',
      }, 
    'p3': {
        'name': 'Meat and bone meal',
        'effect': 'Rendered (or processed) product from animal tissues & bones',
        'details': 'Excludes hair, hooves, horn, hide, manure, or GI contents',
      }, 
    'p4': {
        'name': 'Meat by-product',
        'effect': 'Clean, non-rendered (not processed) parts of animals other than muscle, usually consisting of organs, blood, & bone',
        'details': 'Excludes hair, horns, teeth, & hooves',
      }, 
    'p5': {
        'name': 'Meat digest',
        'effect': 'Materials resulting from chemical or enzymatic degradation of clean animal tissue',
        'details': 'Excludes hair, horns, teeth, hooves, & feathers',
      }, 
    'bha': {
        'name': 'Butylated Hydroxyanisole (BHA)',
        'effect': 'Artificial preservative',
        'details': 'Labelled as a carcinogen in California & banned in the EU',
      }, 
    'bht': {
        'name': 'Butylated Hydroxytoluene (BHT)',
        'effect': 'Artificial preservative',
        'details': 'Not concluded to be a carcinogen but still banned in Japan, Romania, Sweden & Australia',
      }, 
    'eth': {
        'name': 'Ethoxyquin',
        'effect': 'Artificial preservative',
        'details': 'Not concluded to be a carcinogen but still banned in the EU & Australia',
      }, 
}

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")