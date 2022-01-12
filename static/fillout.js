// 'use strict';

// // cannot uncheck radio buttons one by one
// // instead, add a clear button to each category of radio buttons

// document.getElementById('clear-grains').onclick = function() {
//     let grainRadio = document.querySelector('input[type=radio][name=language]:checked');
//     grainRadio.checked = false;
// }

// document.getElementById('clear-additives').onclick = function() {
//     let additiveRadio = document.querySelector('input[type=radio][name=language]:checked');
//     additiveRadio.checked = false;
// }

// document.getElementById('clear-proteins').onclick = function() {
//     let proteinRadio = document.querySelector('input[type=radio][name=language]:checked');
//     proteinRadio.checked = false;
// }

// document.getElementById('clear-preservatives').onclick = function() {
//     let preservativeRadio = document.querySelector('input[type=radio][name=language]:checked');
//     preservativeRadio.checked = false;
// }

// document.getElementById("reset-button").addEventListener("click", confirm_reset);

// function confirm_reset() {
//     let text = "Are you sure you want to reset all fields?";
//     if (confirm(text) == true) {
//       text = "You pressed OK!";
//       document.getElementById("ingredients-form").reset();
//     } else {
//       text = "You canceled!";
//     }
// }