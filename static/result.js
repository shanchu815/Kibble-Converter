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

// okay so navigator.clipboard doesn't work because we don't have a domain name
// site needs to be https for this to work -> work on getting it certified