$(document).ready(function () {
    $('#datatable').DataTable({
        // ordering: false,
        scrollY: '350px',
        lengthMenu: [[10, 15, 20, 25, -1], [10, 15, 20, 25, "Todas"]],
        language: {
            "decimal": "",
            "emptyTable": "No hay información en la tabla",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ entrada(s)",
            "infoEmpty": "Mostrando 0 a 0 de 0 entradas",
            "infoFiltered": "(filtrada(s) de _MAX_ total de entradas)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "No hay coincidencias",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": activar para ordenar la columna ascendentemente",
                "sortDescending": ": activar para ordenar la columna descendentemente"
            }
        }
    });
});