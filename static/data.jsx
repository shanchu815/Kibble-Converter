const ingredientData = [
    {
      id: 'soy',
      name: 'Soy',
      effect: 'Used as a hypoallergenic source of protein & carbs',
      details: 'Cats can develop allergies to it later in life',
    },
    {
        id: 'corn',
        name: 'Corn',
        effect: 'Used as a source of carbs & fiber',
        details: 'Metabolizes into sugar in the gut',
      },
      {
        id: 'wheat',
        name: 'Wheat',
        effect: 'Used as a source of carbs',
        details: 'Common allergen for both dogs & cats',
      },
      {
        id: 'toco',
        name: 'Tocopherols (mixed or non-mixed)',
        effect: 'A food preservative used to add Vitamin E to products',
        details: 'Your pet may be allergic since its derived sources (veggies, nuts or fish) are not listed on the label',
      },
      {
        id: 'la2p',
        name: 'L-ascorbyl-2-polyphosphate',
        effect: 'Ascorbic acid aka Vitamin C',
        details: 'There have been no controversies thus far.',
      },  
      {
        id: 'msbc', 
        name: 'Menadione sodium bisulfate complex',
        effect: 'A source of Vitamin K3',
        details: 'A known carcinogenic & also technically illegal since AAFCO only allows it to be used in poultry feed',
      }, 
      {
        id: 'p1', 
        name: 'Meat',
        effect: 'Clean muscle (skeletal, tongue, diaphragm, heart, esophagus) from animals',
        details: 'May or may not include fat, skin, nerves, & blood vessels',
      }, 
      {
        id: 'p2', 
        name: 'Meat meal',
        effect: 'Rendered (or processed) product from animal tissues',
        details: 'Excludes hair, hooves, horn, hide, manure, or GI contents',
      }, 
      {
        id: 'p3', 
        name: 'Meat and bone meal',
        effect: 'Rendered (or processed) product from animal tissues & bones',
        details: 'Excludes hair, hooves, horn, hide, manure, or GI contents',
      }, 
      {
        id: 'p4', 
        name: 'Meat by-product',
        effect: 'Clean, non-rendered (not processed) parts of animals other than muscle, usually consisting of organs, blood, & bone',
        details: 'Excludes hair, horns, teeth, & hooves',
      }, 
      {
        id: 'p5', 
        name: 'Meat digest',
        effect: 'Materials resulting from chemical or enzymatic degradation of clean animal tissue',
        details: 'Excludes hair, horns, teeth, hooves, & feathers',
      }, 
      {
        id: 'bha', 
        name: 'Butylated Hydroxyanisole (BHA)',
        effect: 'Artificial preservative',
        details: 'Labelled as a carcinogen in California & banned in the EU',
      }, 
      {
        id: 'bht', 
        name: 'Butylated Hydroxytoluene (BHT)',
        effect: 'Artificial preservative',
        details: 'Not concluded to be a carcinogen but still banned in Japan, Romania, Sweden & Australia',
      }, 
      {
        id: 'eth', 
        name: 'Ethoxyquin',
        effect: 'Artificial preservative',
        details: 'Not concluded to be a carcinogen but still banned in the EU & Australia',
      }, 
]

const descriptorData = [
    {
        name: 'dinner',
        ing_min: 0.25,
        ing_max: 0.95,
        ing_min_water: 0.10,
        ing2_min: 0.03,
    },
    {
        name: 'with',
        ing_min: 0.03,
    },
    {
        name: 'flavor',
        ing_min: 0,
    },
    {
        name: 'no',
        ing_min: 0.95,
    }
]




// ReactDOM.render(<ShowDetails />, document.querySelector('#ingredients'));