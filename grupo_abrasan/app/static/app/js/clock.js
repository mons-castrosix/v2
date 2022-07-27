var span = document.getElementById('time');

function time() {
    var d = new Date();
    var s = d.getSeconds();
    var m = d.getMinutes();
    var h = d.getHours();
    span.textContent =
        ("0" + h).substr(-2) + ":" + ("0" + m).substr(-2) + ":" + ("0" + s).substr(-2);
}

setInterval(time, 1000);

var text=document.getElementById('saludo');
var icon=document.getElementById('icon')
function saludo(){
    fecha= new Date();
    hora=fecha.getHours();

    if(hora>=0 && hora<12){
        texto="Buenos días";
    }

    if(hora>=12 && hora<19){
        texto="Buenas tardes";
    }

    if(hora>=18 && hora<24){
        texto="Buenas noches";
    }

    text.innerHTML=texto;

    
    
}



