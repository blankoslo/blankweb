function openmenumobile(obj) {
	var menu = document.getElementById('menumobileopen');
	if (menu.style.display != 'none' ) {menu.style.display = 'none';}
	else {menu.style.display = 'block';}
}

function scrollpos() {
	var jobbpos = document.getElementById("jobb").getBoundingClientRect();
	var menneskenepos = document.getElementById("menneskene").getBoundingClientRect();
	var kontaktpos = document.getElementById("kontakt").getBoundingClientRect();
	var windowh = window.innerHeight;

	var menubutton1pos = document.getElementById("menu").children[0].children[0].children[0].getBoundingClientRect();
	var menubutton2pos = document.getElementById("menu").children[0].children[1].children[0].getBoundingClientRect();
	var menubutton3pos = document.getElementById("menu").children[0].children[2].children[0].getBoundingClientRect();

    if (jobbpos.top > windowh / 2) {
        document.getElementById("index").className = "indexactive";
        document.getElementById("menu").children[0].children[0].children[0].className = "";
        document.getElementById("menu").children[0].children[1].children[0].className = "";
        document.getElementById("menu").children[0].children[2].children[0].className = "";
    } else if (jobbpos.top < windowh / 2 && jobbpos.bottom > windowh / 2 ) {
        document.getElementById("index").className = "";
        document.getElementById("menu").children[0].children[0].children[0].className = "menuactive";
        document.getElementById("menu").children[0].children[1].children[0].className = "";
        document.getElementById("menu").children[0].children[2].children[0].className = "";
    } else if (menneskenepos.top < windowh && menneskenepos.bottom > windowh / 2 ) {
        document.getElementById("index").className = "";
        document.getElementById("menu").children[0].children[0].children[0].className = "";
        document.getElementById("menu").children[0].children[1].children[0].className = "menuactive";
        document.getElementById("menu").children[0].children[2].children[0].className = "";
    } else if (kontaktpos.top < windowh && kontaktpos.bottom > windowh / 2 ) {
        document.getElementById("index").className = "";
        document.getElementById("menu").children[0].children[0].children[0].className = "";
        document.getElementById("menu").children[0].children[1].children[0].className = "";
        document.getElementById("menu").children[0].children[2].children[0].className = "menuactive";
    } else {
        document.getElementById("index").className = "";
        document.getElementById("menu").children[0].children[0].children[0].className = "";
        document.getElementById("menu").children[0].children[1].children[0].className = "";
        document.getElementById("menu").children[0].children[2].children[0].className = "";
    }
}