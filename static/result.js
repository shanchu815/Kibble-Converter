'use strict';

const share = document.getElementById("share-link");

function copyToClipboard(evt) {
    evt.preventDefault();
    const id =  document.getElementById("display").dataset.id;
    navigator.clipboard.writeText(`http://localhost:5000/results/${id}`);//TODO update to static url
    alert("URL Copied.");
}

share.addEventListener('click', copyToClipboard);