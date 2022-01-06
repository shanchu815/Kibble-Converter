'use strict';

function randomImage(){
    let imageUrlIndex = Math.random();
    const image = document.getElementById('random-image');

    if (imageUrlIndex < 0.5){
        fetch('https://dog.ceo/api/breeds/image/random')
        .then(response => response.json())
        .then(jsonData => {
            let dogPicUrl = jsonData["message"];
            image.src = `${dogPicUrl}`;
        });
    }

    else {
            fetch('/api/get_cat_image')
            .then(response => response.text())
            .then(urlText => {
            image.src = `${urlText}`;
        });
    }
}

function randomFact(){
    let factUrlIndex = Math.random();
    const fact = document.getElementById('random-fact');

    if (factUrlIndex < 0.5){
        fetch('/api/get_dog_fact')
        .then(response => response.text())
        .then(dogFact => {
            console.log(dogFact);
            fact.innerHTML += `${dogFact}`;
        });
    }

    else {
        fetch('https://catfact.ninja/fact?max_length=140')
        .then(response => response.json())
        .then(jsonData => {
            let catFactUrl = jsonData["fact"];
            console.log(catFactUrl);
            fact.innerHTML += `${catFactUrl}`;
        });
    };
}

randomFact();
randomImage();