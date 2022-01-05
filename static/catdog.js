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
            // send a fetch request to a new server route /getCatImgUrl
            fetch('/api/get_cat_image')
            // in server.py
            // create /getCatImgUrl route 
            // const catKey = '74a565ba-44ea-412b-b5e2-845bf9f18314';
            // let catPicUrl = imageURL + catKey;
            // in 
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
        fetch('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1')
        .then(response => response.json())
        .then(jsonData => {
            let dogFactUrl = jsonData[0]["fact"];
            fact.innerHTML += `${dogFactUrl}`;
            console.log (jsonData[0])
        });
    }

    // [
    //     {
    //           "fact": "Many foot disorders in dogs are caused by long toenails."
    //     }
    // ]
        

    else {
        fetch('https://catfact.ninja/fact?max_length=140')
        .then(response => response.json())
        .then(jsonData => {
            let catFactUrl = jsonData["fact"];
            fact.innerHTML += `${catFactUrl}`;
        });
    };
}

randomFact();
randomImage();