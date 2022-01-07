'use strict';

let radioForm = document.getElementById("others");
let radios = radioForm.getElementsByTagName("input");

for(i = 0; i < radios.length; i++) {
    radios[i].onclick = function(e) {
        if(e.ctrlKey) {
        this.checked = false;
        }
    }
}