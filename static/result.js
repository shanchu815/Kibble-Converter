'use strict';

const share = document.getElementById("share-link");

function copyToClipboard(evt) {
    evt.preventDefault();
    if (navigator.clipboard) {
        navigator.clipboard.writeText(location.href);
        alert("URL Copied.");
    }
    alert(`Copy this url: ${location.href}`);
}

share.addEventListener('click', copyToClipboard);

// `http://localhost:5000/results/${id}` -> location.href
//`http://3.91.73.97/results/${id}` is the instance version (if location.href doesn't work, try this)