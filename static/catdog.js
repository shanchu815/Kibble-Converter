'use strict';

function randomImageFact(){
    let randomIndex = Math.random();
    const image = document.getElementById('random-image');
    const fact = document.getElementById('random-fact');

    if (randomIndex < 0.5){
        fetch('https://dog.ceo/api/breeds/image/random')
        .then(response => response.json())
        .then(jsonData => {
            let dogPicUrl = jsonData["message"];
            image.src = `${dogPicUrl}`;
        });
        fetch('/api/get_dog_fact')
        .then(response => response.text())
        .then(dogFact => {
            fact.innerHTML += `${dogFact}`;
        });
    }

    else {
            fetch('/api/get_cat_image')
            .then(response => response.text())
            .then(urlText => {
            image.src = `${urlText}`;
        });
            fetch('https://catfact.ninja/fact?max_length=140')
            .then(response => response.json())
            .then(jsonData => {
                let catFactUrl = jsonData["fact"];
                fact.innerHTML += `${catFactUrl}`;
        });
    }
}

randomImageFact();

let scrollButton = document.getElementById("scroll-button");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollButton.style.display = "block";
    } 
    else {
    scrollButton.style.display = "none";
    }
}

function topFunction(evt) {
    evt.preventDefault();
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

scrollButton.addEventListener('click', topFunction)