var tab = document.getElementById("tablaArea");
var fil=0;col=0;
var op = false;

function BuscarArea() {
            var id = $('#selectArea').val();
            // console.log(id);
            var buscar = document.getElementById('buscarArea').value;
            $.ajax({
               data: {'id':id, 'buscar':buscar},
               url: '/reserva/busquedaAjax/',
                type: 'get',
                success: function (data) {
                    console.log(data);
                    var html = "";
                    var cont = 1;
                    for (var i=0; i<data.length; i++){
                        html+= '<tr>\n' +
                            '<th>'+cont+'</th>\n' +
                            '<td class="d-none id">'+data[i].pk +'</td>\n' +
                            '<td nowrap="true" class="nombre">'+data[i].fields.nombre +'</td>\n' +
                            '<td class="text-center sector">'+data[i].fields.sector+'</td>\n' +
                            '<td class="text-center tmp_maximo">'+data[i].fields.tmp_maximo+'</td>\n' +
                            '<td class="elegirArea btn btn-success d-block" data-dismiss="modal" ">ELEGIR!</td>\n' +
                            '/tr>';
                        cont++;
                    }
                    $('#datosModal').html(html);
                    AreaComun();
                }
            });
        };

function AreaComun() {
    $(".elegirArea").click(function() {

        var id = "";
        var nombre = "";
        var sector = "";
        var tmp_maximo = "";
        var tabla = "";
        var select = "";
        var multiselect = "";

        // Obtenemos todos los valores contenidos en los <td> de la fila
        // seleccionada
        $(this).parents("tr").find(".tmp_maximo").each(function() {
            tmp_maximo = $(this).html();
        });
        $(this).parents("tr").find(".sector").each(function() {
            sector = $(this).html();
        });
        $(this).parents("tr").find(".nombre").each(function() {
            nombre = $(this).html();
        });
        $(this).parents("tr").find(".id").each(function() {
            id = $(this).html();
        });
        // {#console.log(valores + " "+ id);#}

        var cont = 0;
        var cont_element = -1;
        if (verificar(nombre, sector)){
            $("body").overhang({
                        type: "warn",
                        message: "No puede Agregar 2 veces la misma Area!",
                        duration: 4,
                        overlay: true
                    });
        } else{
            for (var i =0; i<tab.rows.length; i++){
                cont++;
                cont_element++;
            }
            if (cont <= 3){
                tabla+='<tr> \n' +
                '<td class="nombre">'+nombre+'</td>\n' +
                '<td class="sector">'+sector+'</td>\n' +
                '<td>'+tmp_maximo+'</td>\n' +
                    '<td class="col-6 d-none invisible" id="select_select'+cont_element+'"></td>\n' +
                    '<td><input type="time" name="detallereserva_set-'+cont_element+'-hora" class="form-control"></td>\n' +
                    '<td><input type="time" name="detallereserva_set-'+cont_element+'-tmp_uso" class="form-control"></td>\n' +
                '<td class="eliminarArea btn btn-danger d-block" data-dismiss="modal" >Eliminar</td>\n' +
                    '<td class="id d-none">'+id+'</td>\n' +
                '</tr>';

                multiselect+='<option value="'+id+'" selected>Opc</option>\n';

                select+='<select class="custom-select d-none hidden invisible" id="detallereserva_set-'+cont_element+'-id_area_comun" name="detallereserva_set-'+cont_element+'-id_area_comun"></select>';

            $('#listAreas').append(tabla);
            $('#select_select'+cont_element).append(select);
            $('#detallereserva_set-'+cont_element+'-id_area_comun').append(multiselect);
            } else {
                $("body").overhang({
                        type: "warn",
                        message: "Solo se permite reserva de 3 Areas por Propietario!",
                        closeConfirm: true,
                        duration: 4
                    });
            }

        }

        EliminarArea();

        // $('#listAreas').val(categoria);

        // $('#pk-visitante').val(id);
    });
};

function verificar(nombre, sector){
    for (var i =0; i<tab.rows.length; i++){
        if (tab.rows[i].cells[0].innerHTML == nombre &&
            tab.rows[i].cells[1].innerHTML == sector){
            op = true;
            fil = i; col=0;
        }else{
            op=false;
        }
    }
    return op;
};


function EliminarArea() {
    $(".eliminarArea").click(function() {
        var sel = document.getElementById("id_area_social");
        var id = "";
        var nombre = "";
        var sector = "";

        // Obtenemos todos los valores contenidos en los <td> de la fila
        // seleccionada

        $(this).parents("tr").find(".sector").each(function() {
            sector = $(this).html();
        });
        $(this).parents("tr").find(".nombre").each(function() {
            nombre = $(this).html();
        });
        $(this).parents("tr").find(".id").each(function() {
            id = $(this).html();
        });

        for (var i =0; i<tab.rows.length; i++){
        if (tab.rows[i].cells[0].innerHTML == nombre &&
            tab.rows[i].cells[1].innerHTML == sector){
            // console.log("entro");
            if (sel.options.valueOf()[i-1].value == id){
                sel.remove(i-1);
            }
            tab.rows[i].remove();
        }else{
            // tab.rows[i].remove();
        }
    }

        // if (!verificar(nombre, sector)){
        //     $('#eliminarArea').remove();
        //     console.log(nombre + " "+ sector);
        // }
    });
};
