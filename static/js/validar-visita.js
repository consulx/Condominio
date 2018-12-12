function validar() {
    // var ci, nombre, app, apm, visitante, hora, minutos;
    // var notificacion, titulo, mensaje, formulario;
    //
    // ci = document.getElementById('ci').value;
    // nombre = document.getElementById('nombre').value;
    // app = document.getElementById('app').value;
    // apm = document.getElementById('apm').value;
    // visitante = document.getElementById('visitante').value;
    // hora = document.getElementById('hora').value;
    // minutos = document.getElementById('minutos').value;
    //
    // formulario = document.getElementById("formulario");
    // notificacion = document.getElementById("notificacion");
    // titulo = document.getElementById("titulo");
    // mensaje = document.getElementById("mensaje");
    //
    // var campos = [ci, nombre, app, apm, visitante, hora, minutos];
    // var cont = 0;
    //
    // for (var i=0; i<= campos.length; i++) {
    //     if (campos[i] === ""){
    //         cont++;
    //     }
    // }
    // if (cont > 0){
    //     $("body").overhang({
    //         type: "error",
    //         message: "Rellene todos los campos Obligatorios *",
    //         closeConfirm: true,
    //         duration: 5
    //     });
    //
    //     return false;
    // }

    var formulario = document.formulario_visita,
        elementos = formulario.elements;

    var validarInputs = function(){
        var cont = 0;
        for (var i = 0; i < elementos.length; i++) {
            // Identificamos si el elemento es de tipo texto, email, password, radio o checkbox
            if (elementos[i].type == "text" || elementos[i].type == "email" || elementos[i].type == "number") {
                // Si es tipo texto, email o password vamos a comprobar que esten completados los input
                if (elementos[i].value.length == 0) {
                    cont ++;
                    console.log('El campo ' + elementos[i].name + ' esta incompleto');
                    elementos[i].className = elementos[i].className.replace(" error", "");
                    elementos[i].className = elementos[i].className + " error";
                    elementos[i].focus();

                    elementos[i].addEventListener("keyup", function (event) {
                            if (elementos[i].value.trim() != ""){
                                elementos[i].className = elementos[i].className.replace(" error", "");
                            }else{
                                elementos[i].className = elementos[i].className + " error";
                            }
                        }, false);

                    $("body").overhang({
                        type: "error",
                        message: "Rellene todos los campos Obligatorios *",
                        closeConfirm: true,
                        duration: 3
                    });

                    return false;
                } else {
                    elementos[i].className = elementos[i].className.replace(" error", "");
                }
            }
        }
        if (cont == 0){
            return true;
        } else{
            return false;
        }
        // return true;
    };

    if(validarInputs()){
        return true;
    }else{
        return false;
    }
}