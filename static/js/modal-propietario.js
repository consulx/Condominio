function inicio() {
            var id = $('#selectPropietario').val();
            console.log(id);
            var buscar = document.getElementById('buscar').value;
            $.ajax({
               data: {'id':id, 'buscar':buscar},
               url: '/propietario/busquedaAjax/',
                type: 'get',
                success: function (data) {
                    console.log(data);
                    var html = "";
                    var cont = 1;
                    for (var i=0; i<data.length; i++){
                        html+= '<tr>\n' +
                            '<th>'+cont+'</th>\n' +
                            '<td class="d-none id">'+data[i].pk +'</td>\n' +
                            '<td nowrap="true" class="nombre">'+data[i].fields.nombre +' '+data[i].fields.app + ' '+data[i].fields.apm+'</td>\n' +
                            '<td class="text-center">'+data[i].fields.ci+'</td>\n' +
                            '<td class="text-center">'+data[i].fields.nro_casa+'</td>\n' +
                            '<td class="boton btn btn-success d-block" data-dismiss="modal" onclick="visitante()">ELEGIR!</td>\n' +
                            '/tr>';
                        cont++;
                    }
                    $('#datos').html(html);
                    visita();
                }
            });
        };

function visita() {
    $(".boton").click(function() {

        var id = "";
        var nombre = "";

        // Obtenemos todos los valores contenidos en los <td> de la fila
        // seleccionada
        $(this).parents("tr").find(".nombre").each(function() {
            nombre = $(this).html();
        });
        $(this).parents("tr").find(".id").each(function() {
            id = $(this).html();
        });
        // {#console.log(valores + " "+ id);#}
        $('#visitante').val(nombre);

        $('#pk-visitante').val(id);
    });
}