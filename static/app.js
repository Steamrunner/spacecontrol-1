window.App = (function($) {
    // Lights
    var lightHandler = function(id, on) {
        var url = 'http://' + HOSTNAME;
        if (on) {
            url += '/api/switch_on/' + id;
        } else {
            url += '/api/switch_off/' + id;
        }
        console.log(url);

        $.ajax(url);
    };

    $('#light-one-on').bind('click', function() {lightHandler(3, true);});
    $('#light-one-off').bind('click', function() {lightHandler(3, false);});
    $('#light-two-on').bind('click', function() {lightHandler(4, true);});
    $('#light-two-off').bind('click', function() {lightHandler(4, false);});
    $('#light-three-on').bind('click', function() {lightHandler(5, true);});
    $('#light-three-off').bind('click', function() {lightHandler(5, false);});

    $('#light-all-off').bind('click', function() {
        $.ajax('http://' + HOSTNAME + '/api/switch_all_off');
    });
    $('#light-all-on').bind('click', function() {
        $.ajax('http://' + HOSTNAME + '/api/switch_all_on');
    });

    // Coffee
    var coffeeHandler = function(id) {
        var url = 'http://' + HOSTNAME + '/api/button/' + id;
        $.ajax(url);
    };
    $('#coffee-power').bind('click', function() {coffeeHandler(0);});
    $('#coffee-small').bind('click', function() {coffeeHandler(1);});
    $('#coffee-large').bind('click', function() {coffeeHandler(2);});
});

jQuery(function() {
    app = App(jQuery);
});
