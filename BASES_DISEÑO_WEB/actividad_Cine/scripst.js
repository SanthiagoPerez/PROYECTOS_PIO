function validarFormulario(){
    var nombre = document.getElementById("nombre").ariaValueMax;

    if (nombre == ""){
        alert("Por favor, ingresa tu nombre.")
        return false
    }
    alert("Formulario enviado con exito")
    return true
}

document.getElementById("CambiarColor").onclick = function(){
    var titulo = document.getElementById("Titulo");
    titulo.style.color = titulo.style.color == 'red' ? '#4CAF50': 'red';
}