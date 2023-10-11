// main.js
function copyText(target) {
    const textToCopy = document.querySelector(target);
    const textArea = document.createElement("textarea");
    textArea.value = textToCopy.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
    showCopyPopup();
}

function showCopyPopup() {
    const copyPopup = document.querySelector(".copy-popup");
    copyPopup.classList.remove("hidden");
    setTimeout(() => {
      copyPopup.classList.add("hidden");
    }, 2000);
  }