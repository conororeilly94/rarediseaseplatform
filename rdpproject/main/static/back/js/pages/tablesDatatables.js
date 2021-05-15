var TablesDatatables = function() {

    return {
        init: function() {
            App.datatables();

            $('#example-datatable').dataTable({
                columnDefs: [ { orderable: false, targets: [ 1, 5 ] } ],
                pageLength: 10,
                lengthMenu: [[10, 20, 30, -1], [10, 20, 30, 'All']]
            });

            $('.dataTables_filter input').attr('placeholder', 'Search');
        }
    };
}();