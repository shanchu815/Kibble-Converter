'use strict';

const firstForm = document.getElementById("calc1");
const secondForm = document.getElementById("calc2");

function trueProteinContent(a, b) {
    let num = (a/(100-b)) * 100;
    return +num.toFixed(2);
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
    document.getElementById(target).innerHTML = `${result}%`
}

firstForm.addEventListener('submit', calculator);
secondForm.addEventListener('submit', calculator);

function confirm_reset() {
    return confirm("Are you sure you want to reset all fields?");
}