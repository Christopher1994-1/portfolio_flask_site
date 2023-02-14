window.onscroll = function() {
  let secondNavbar = document.querySelector("#services-dropdown");
  let navbarPlaceholder = document.querySelector(".navbar-placeholder");
  if (window.pageYOffset >= 250) {
    secondNavbar.style.top = "10px";
    secondNavbar.style.positon = "absolute";
   } 
  //  else if (window.pageYOffset < 250) {
  // //   secondNavbar.style.top = "-70px";
  // //   secondNavbar.style.position = "initial";
  // //   navbarPlaceholder.style.display = "none";
  // //   navbarPlaceholder.style.height = "0";
  // // }
};
