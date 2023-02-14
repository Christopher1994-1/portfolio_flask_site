const footer1 = document.querySelector(".main_footer");
const footer2 = document.querySelector('.main_footer2');


function updateNavDisplay() {
    const screensize = window.innerWidth;

    if (screensize < 981) {
        footer1.style.display = "none";
        footer2.style.display = "initial";

    } else if (screensize > 981) {
        footer1.style.display = "initial";
        footer2.style.display = "none"
    }
}

updateNavDisplay();

window.addEventListener('resize', updateNavDisplay);
