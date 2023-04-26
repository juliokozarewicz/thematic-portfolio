window.sessionStorage.clear();

/* paralax init */
function paralax(class_name, type_tag) {

    document.addEventListener("mousemove", parallax);
    function parallax(event) {
    this.querySelectorAll("."+class_name+" "+type_tag).forEach((shift) => {
        const position = shift.getAttribute("value");
        const x = (window.innerWidth - event.pageX * position) / 90;
        const y = (window.innerHeight - event.pageY * position) / 90;

        shift.style.transform = `translateX(${x}px) translateY(${y}px)`;
    });
    }
}
/* paralax end */

/* menu init */
function status_menu() {

    try {

        this.status_menu = window.sessionStorage.getItem('status_menu')

        if (this.status_menu === 'menu_on') {

            /* SET STATUS */
            this.status_menu = window.sessionStorage.setItem('status_menu', 'menu_off')

            /* FRAME ALL ANIMATION */
            document.getElementById('idmenuall').style="-webkit-animation: menuclose 1s forwards;";

            /* HAMBURGUER ANIMATION */
            document.getElementById("idmhamb").classList.remove("mhamb2");
            document.getElementById("idmhamb").classList.add("mhamb");

            document.getElementById("idline1").classList.remove("line11");
            document.getElementById("idline1").classList.add("line1");

            document.getElementById("idline2").classList.remove("line12");
            document.getElementById("idline2").classList.add("line2");

            document.getElementById("idline3").classList.remove("line13");
            document.getElementById("idline3").classList.add("line3");

            /* HIDE CONTENT */
            document.getElementById('idmenulist').style = "display: none;";

        } else if (this.status_menu === 'menu_off') {

            /* SET STATUS */
            this.status_menu = window.sessionStorage.setItem('status_menu', 'menu_on')

            /* FRAME ALL ANIMATION */
            document.getElementById('idmenuall').style="-webkit-animation: menuopen 1s forwards;";

            /* HAMBURGUER ANIMATION */
            document.getElementById("idmhamb").classList.toggle("mhamb2");
            setTimeout(function() {
                document.getElementById("idline1").classList.toggle("line11");
                document.getElementById("idline2").classList.toggle("line12");
                document.getElementById("idline3").classList.toggle("line13");
            }, 1050);
            
            /* SHOW CONTENT */
            setTimeout(function() {
                document.getElementById('idmenulist').style = "display: flex;";
            }, 700);

        } else if (this.status_menu === null) {

            /* SET STATUS */
            this.status_menu = window.sessionStorage.setItem('status_menu', 'menu_on')

            /* FRAME ALL ANIMATION */
            document.getElementById('idmenuall').style="-webkit-animation: menuopen 1s forwards;";

            /* HAMBURGUER ANIMATION */
            document.getElementById("idmhamb").classList.toggle("mhamb2");
            setTimeout(function() {
                document.getElementById("idline1").classList.toggle("line11");
                document.getElementById("idline2").classList.toggle("line12");
                document.getElementById("idline3").classList.toggle("line13");
            }, 700);

            /* SHOW CONTENT */
            setTimeout(function() {
                document.getElementById('idmenulist').style = "display: flex;";
            }, 1050);

        }

    } catch (error) {
        console.log('***** [ ERROR - STATUS MENU ! ] *****')
        console.log(error)
    }

}
/* menu end */

/* audio init */
function change(id_checkbox, id_tag_audio) {

    let decider = document.getElementById(id_checkbox);

    if(decider.checked){
        document.getElementById(id_tag_audio).pause();
    } else {
        document.getElementById(id_tag_audio).play(); 
    }
    
}
/* audio end */

/* scroll slider init */
function scrollLft(class_tag_slider) {
    document.getElementsByClassName(class_tag_slider)[0].scrollBy({
        left: -500,
        behavior: 'smooth'
    });
}

function scrollRight(class_tag_slider) {
    document.getElementsByClassName(class_tag_slider)[0].scrollBy({
        left: 500,
        behavior: 'smooth'
    });
}
/* scroll slider end */

/* unload page init */
function unloadPage(pg_unload) {

    var element = document.getElementById(pg_unload);

    element.style.display = "none";

}
/* unload page end */