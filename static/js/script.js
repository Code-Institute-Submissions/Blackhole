$(document).ready(function(){
    $('.datepicker').datepicker({
        format: 'dd mmmm, yyyy',
        showClearBtn: true,
        autoClose: true,
        yearRange: 100,
    });
    $('.sidenav').sidenav();
});

$(document).on('click', '#profile-pop-out-icon', function() {
    $('#profile-pop-out-section').toggle();
})

$(document).on('click', '#image-post-icon', function() {
    $('#image-post').click();
})

$(document).on('click', '#mentions-post-icon', function() {
    $('#mentions-post').click();
})

// SETTINGS THEMES SWITCHES

$(document).on('click', '#dark_switch', function() {
    $('#light_theme').prop('checked', false);
})

$(document).on('click', '#light_switch', function() {
    $('#dark_theme').prop('checked', false);
})