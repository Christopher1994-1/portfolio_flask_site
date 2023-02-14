const page1 = document.getElementById("review-page-1");
const page2 = document.getElementById("review-page-2");
const indicator1 = document.getElementById("page-indicator-1");
const indicator2 = document.getElementById("page-indicator-2");

// page one
indicator1.addEventListener("click", function() {
  page1.style.display = "flex";
  page2.style.display = "none";
  indicator1.style.backgroundColor = "black";
  indicator2.style.backgroundColor = "gray";
});

// page two
indicator2.addEventListener("click", function() {
  page1.style.display = "none";
  page2.style.display = "flex";
  indicator1.style.backgroundColor = "grey";
  indicator2.style.backgroundColor = "black";
});
