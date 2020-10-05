$(document).ready(function(){
    $('.datepicker').datepicker({
        format: 'dd mmmm, yyyy',
        showClearBtn: true,
        autoClose: true,
        yearRange: 100,
    });
});

// need to fix for clicking else where 
$(document).on('click', '#acitivity-post', function() {
    $('#label-post').toggle();
})

$(document).on('click', '#image-post-icon', function() {
    $('#image-post').click();
})

$(document).on('click', '#mentions-post-icon', function() {
    $('#mentions-post').click();
})