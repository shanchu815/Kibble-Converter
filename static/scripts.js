'use strict';

const firstForm = document.getElementById("calc1");
const secondForm = document.getElementById("calc2");

function trueProteinContent(a, b) {
    return (a/(100-b)) * 100;
}

function calculator(evt){
    evt.preventDefault();
    let crudeProtein;
    let moisture;
    let target;

    if(evt.target.id == "calc1"){
        crudeProtein = parseFloat(firstForm['crude-protein'].value);
        moisture = parseFloat(firstForm['moisture'].value);
        target = 'true-protein';
    }else{
        crudeProtein = parseFloat(secondForm['crude-protein'].value);
        moisture = parseFloat(secondForm['moisture'].value);
        target = 'true-protein2';
    }

    const result = trueProteinContent(crudeProtein, moisture);
    document.getElementById(target).innerHTML = `${result}`
}

// function secondCalculator(evt){
//     evt.preventDefault();
//     const result = trueProteinContent(crudeProtein, moisture);
//     document.getElementById('true-protein2').innerHTML = `${result}`;
// }

firstForm.addEventListener('submit', calculator);
secondForm.addEventListener('submit', calculator);

function confirm_reset() {
    return confirm("Are you sure you want to reset all fields?");
}

const fillOut = document.getElementById("ingredients-form");

fillOut.addEventListener('submit', displayResults);

function displayResults(evt){

    
}