//crear una función
function mostrarAlerta() {
    //variables
    const numero_1 = 10;
    var numero_2 = 5;
    let mensaje = "hola mundo";
    alert(mensaje);
    //ciclos
    for (let i = 0; i < 4; i++) {
        alert("actualizar");
    }

    //condicionales
    let num_1 = 5;
    let num_2 = 10;
    if (num_1 < numero_2) {
        console.log("es menor");
    } else {
        console.log("es mayor");
    }
}

function eliminar() {
    console.log("Personaje eliminado");
    console.error("error al eliminar");
    console.table({ "clave_1": "valor_1", "clave_2": "valor_2" });
    alert("Eliminar");
}

function actualizar() {
    let alt = document.getElementById("imgPersonaje").alt;
    if (alt == "imagen1") {
        //Acceder a un elemento del documento html por id
        document.getElementById("imgPersonaje").src = "https://vignette.wikia.nocookie.net/en.futurama/images/0/0d/Hermes.png/revision/latest?cb=20170719011119";
        //cambiamos el alt de la imagen
        document.getElementById("imgPersonaje").alt = "imagen2";
    } else {
        document.getElementById("imgPersonaje").src = "https://vignette.wikia.nocookie.net/en.futurama/images/e/e2/Hobos.jpg/revision/latest/scale-to-width-down/350?cb=20111118085946";
        document.getElementById("imgPersonaje").alt = "imagen1";
    }
}

//Función de llamado a la api de futurama
async function cargarPersonajes() {
    //conectar/llamar a la api
    const peticion = await fetch("https://futuramaapi.herokuapp.com/api/v2/characters");
    console.log("--------petición-------");
    console.log(peticion);
    console.log("-----------------------");
    const data = await peticion.json();
    console.log("-----------data-----------");
    console.log(data);
    console.log("--------------------------");
    /************Recorrer el arreglo obtenido en la peticion a la API**********/
    data.forEach(element => {
        //console.log(element.Name);
        let tarjeta = "<div class='card' style='width: 18rem;'>";
        tarjeta += "<img id='imgPersonaje' src='"+element.PicUrl+"'";
        tarjeta += "class='card-img-top imgPersonaje' alt='imagen1'>";
        tarjeta += "<div class='card-body'>";
        tarjeta += "<div class='card-body'>";
        tarjeta += "<label>Profesión: --</label><br>";
        tarjeta += "<label>Especie: --</label><br>";
        tarjeta += "<label>Planeta: --</label><br>";
        tarjeta += "<button type='button' class='btn btn-outline-danger' onclick='eliminar()''>Eliminar</button>";
        tarjeta += "&nbsp;<button type='button' class='btn btn-outline-primary' onclick='actualizar()'>Actualizar</button>";
        tarjeta += "</div></div>";
        //agregar estructura/card al div
        document.getElementById("cuerpo").innerHTML += tarjeta;
    });
}
