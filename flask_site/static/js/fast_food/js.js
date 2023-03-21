let jumboDiv = document.getElementById('jumboID');
let originalTop = jumboDiv.style.top = "28%";

function menu_select() {
    if (document.getElementById('menu-bar').checked) {
        jumboDiv.style.top = "60%";
    } else {
        jumboDiv.style.top = originalTop;
    }
}





// Get all the links and items
