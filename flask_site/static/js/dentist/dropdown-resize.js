const nav1 = document.querySelector('.menu');

function updateNavDisplay() {
    const screensize = window.innerWidth;

    if (screensize < 760) {
        nav1.style.top = '70%';
    } else if (screensize > 760){
        nav1.style.display = 'none';
    }

    if (window.innerWidth < 760) {
        navMenu.style.top = "30%"
      }else if (window.innerWidth > 760){
          navMenu.style.top = "20%";
      }; 
}

updateNavDisplay();

window.addEventListener('resize', updateNavDisplay);
window.addEventListener('scroll', updateNavDisplay);

