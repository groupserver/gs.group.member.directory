       	jQuery.noConflict()
       	jQuery(document).ready(function() {
       	jQuery('#memberdirectory').dataTable( {
               	"oLanguage": {"sSearch": "Filter records:"},
               	"aaSorting": [[0,'asc']],
               	"bProcessing": true,
               	"iDisplayLength": 100,
               	"sAjaxSource": 'members.json',
               	"sPaginationType": "full_numbers",
               	"aoColumns": [{"sTitle": "Name",
                               "sType": "html",
                               "sWidth": "25%"},
                              {"sTitle": "Organisation",
                               "sWidth": "10%"},
                              {"sTitle": "City",
                               "sWidth": "10%"},
                              {"sTitle": "Region",
                               "sWidth": "10%"},
                              {"sTitle": "Country"},
                              {"sTitle": "Joined",
                               "sWidth": "5%"}]
       	} );
} );

