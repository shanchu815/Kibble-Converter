'use strict';

const imageURLS = ['https://api.thecatapi.com/v1/images/search?format=src&size=full&mime_types=png,jpg&api_key=', 'https://dog.ceo/api/breeds/image/random'];
const factURLS = ['https://catfact.ninja/fact?max_length=140', 'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1'];

function randomImage(imageURLS){
    let imageUrlIndex = Math.floor(Math.random() * 1);
    let imageURL = imageURLS[imageUrlIndex];
    const image = document.getElementById('random-image')

    if (imageUrlIndex == 1){
        fetch(imageURL)
        .then(response => response.json())
        .then(jsonData => {
            let dogPicUrl = jsonData["message"];
            image.innerHTML += `${dogPicUrl}`;
        });
    }

    else {
            const catKey = '74a565ba-44ea-412b-b5e2-845bf9f18314';
            let catPicUrl = imageURL + catKey;
            image.innerHTML += `${catPicUrl}`;
    };
}

function randomFact(factURLS){
    let factUrlIndex = Math.floor(Math.random() * 1);
    let factURL = factURLS[factUrlIndex];
    const fact = document.getElementById('random-fact')

    if (factUrlIndex == 1){
        fetch(factURL)
        .then(response => response.json())
        .then(jsonData => {
            let dogFactUrl = jsonData[0]["fact"];
            fact.innerHTML += `${dogFactUrl}`;
        });
    }

    else {
        fetch(factURL)
        .then(response => response.json())
        .then(jsonData => {
            let catFactUrl = jsonData["fact"];
            fact.innerHTML += `${catFactUrl}`;
        });
    };
}

randomFact()
randomImage()