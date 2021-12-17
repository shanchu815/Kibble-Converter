'use strict';

const firstForm = document.getElementById(calc1);
const secondForm = document.getElementById(calc2);

function trueProteinContent(a, b) {
    return (a/(100-b)) * 100;
}

function firstCalculator(evt){
    evt.preventDefault();
    const crudeProtein = parseInt(firstForm['crude-protein'].value);
    const moisture = parseInt(firstForm['moisture'].value)
    const result = trueProteinContent(crudeProtein, moisture);
    document.getElementById('true-protein').innerHTML = `${result}`;
}

function secondCalculator(evt){
    evt.preventDefault();
    const crudeProtein = parseInt(secondForm['crude-protein'].value);
    const moisture = parseInt(secondForm['moisture'].value)
    const result = trueProteinContent(crudeProtein, moisture);
    document.getElementById('true-protein2').innerHTML = `${result}`;
}

firstForm.addEventListener('submit', firstCalculator);
secondForm.addEventListener('submit', secondCalculator);

function confirm_reset() {
    return confirm("Are you sure you want to reset all fields?");
}