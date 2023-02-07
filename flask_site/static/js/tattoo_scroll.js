// main.js
window.onscroll = function() {
    var header = document.querySelector("header");
    var navbarContainer = document.querySelector(".navbar-container");
  
    if (document.body.scrollTop > 70 || document.documentElement.scrollTop > 70) {
      navbarContainer.classList.add("scrolled");
    } else {
      navbarContainer.classList.remove("scrolled");
    }
  };