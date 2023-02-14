window.onscroll = function() {
    let secondNavbar = document.querySelector(".second-navbar");
    let dropdown = document.querySelector("#services-dropdown");
    let dropdown_pages = document.querySelector("#pages-dropdown");
    let navbarPlaceholder = document.querySelector(".navbar-placeholder");
    let navMenu = document.querySelector(".menu")
    if (window.pageYOffset >= 250) {
      secondNavbar.style.position = "fixed";
      secondNavbar.style.top = "0";
      secondNavbar.style.width = "100%";
      secondNavbar.style.zIndex = "1";
      dropdown.style.top = "50";
      dropdown_pages.style.top = "50";
      secondNavbar.style.transition = "top 0.6s ease-in-out";
      navbarPlaceholder.style.display = "block";
      navbarPlaceholder.style.height = secondNavbar.offsetHeight + "px";
      navMenu.style.top = '70%';
    }
      
      else if (window.pageYOffset < 250) {
      secondNavbar.style.top = "-70px";
      secondNavbar.style.position = "initial";
      navbarPlaceholder.style.display = "none";
      navbarPlaceholder.style.height = "0";
      dropdown.style.top = "16%";
      dropdown_pages.style.top = "16%";
      navMenu.style.top = '20%';
    }
  };


  