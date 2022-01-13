'use strict';

const share = document.getElementById("share-link");

function copyToClipboard(evt) {
    evt.preventDefault();
    // const id =  document.getElementById("display").dataset.id;
    navigator.clipboard.writeText(location.href);//TODO update to static url 
    // (Don't update to static url) - didn't cover changing domain names yet
    alert("URL Copied.");
}

share.addEventListener('click', copyToClipboard);

// `http://localhost:5000/results/${id}` -> location.href
//`http://3.91.73.97/results/${id}` is the instance version (if location.href doesn't work, try this)