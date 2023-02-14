const nav = document.querySelector('.nav');

function updateNavDisplay() {
    const screensize = window.innerWidth;

    if (screensize < 820) {
        nav.style.display = 'initial';
    } else {
        nav.style.display = 'none';
    }
}

updateNavDisplay();

window.addEventListener('resize', updateNavDisplay);
