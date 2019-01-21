$(document).ready( function() {
    // -------- Initialize Isotope ----------//
    $( function() {
    // quick search regex
    var qsRegex;
    var buttonFilter;
    var isoOptions = {
        itemSelector: '.player_class',
        filter: function() {
            var $this = $(this);
            var searchResult = qsRegex ? $this.text().match( qsRegex ) : true;
            var buttonResult = buttonFilter ? $this.is( buttonFilter ) : true;
            return searchResult && buttonResult;
        },
        getSortData: {
            cost: '.cost parseInt'
            }
    };
    // -------- List FUNCTION ----------//
    var isIsotopeEnabled = true;
    
    // init Isotope
    var $container = $('.grid_test').isotope( isoOptions );
    
    $('.toggle-button').click(function(){
        $('.grid_test').toggleClass('listme');
        $('.togglelist').toggleClass('toggleactive');
    });
    // -------- Filter FUNCTION ----------//
    var filters = {};
    $('#filter').on( 'click', '.button', function() {
        var $this = $(this);
        var $buttonGroup = $this.parents('.button-group');
        var filterGroup = $buttonGroup.attr('data-filter-group');
        filters[ filterGroup ] = $this.attr('data-filter');
        var filterValue = '';
        for ( var prop in filters ) {
        filterValue += filters[ prop ];
        }
        buttonFilter = filterValue;
        $container.isotope();
    });
    // -------- Sort FUNCTION ----------//
    $('#sorts').on( 'click', '.button', function() {
        var sortByValue = $(this).attr('data-sort-by');
        $container.isotope({ sortBy: sortByValue });
    });
    
    // -------- Search FUNCTION ----------//
    var $quicksearch = $('.quicksearch').keyup( debounce( function() {
        qsRegex = new RegExp( $quicksearch.val(), 'gi' );
        $container.isotope();
    }) );
    
    // -------- Active buttons ----------//
    

    $('.button-group').each( function( i, buttonGroup ) {
        var $buttonGroup = $( buttonGroup );
        $buttonGroup.on( 'click', 'button', function() {
        $buttonGroup.find('.secondary').removeClass('secondary');
        $( this ).addClass('secondary');
        $buttonGroup.find('.is-checked').removeClass('is-checked');
        $( this ).addClass('is-checked');
        });
    });
    // -------- Debounce so filtering doesn't happen every millisecond ----------//
    function debounce( fn, threshold ) {
    var timeout;
    return function debounced() {
        if ( timeout ) {
        clearTimeout( timeout );
        }
        function delayed() {
        fn();
        timeout = null;
        }
        setTimeout( delayed, threshold || 100 );
        };
    }
    });
})