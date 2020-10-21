// SIGN UP FORM

    // NAME VALIDATION

function nameCheck(nameTag, errorTag) {
    
    var fN = document.forms['signUpForm'][nameTag].value;
    var fNE = document.getElementById(errorTag);
    var letters = /^[A-Za-z]+$/;

    if (fN.length < 3) {
        fNE.innerHTML = 'You Need To Enter More Than 3 Letters!';
    }
    else if(fN.match(letters)) {
        fNE.innerHTML = '';
    } else {
        fNE.innerHTML = 'You Can Only Enter Letters!'
    }
};

// CALENDAR FOR DOB ON SIGN UP

$(document).ready(function(){
    $('.datepicker').datepicker({
        format: 'dd mmmm, yyyy',
        showClearBtn: true,
        autoClose: true,
        yearRange: 100,
    });
    $('.modal').modal();
    $('.tooltipped').tooltip();
});

// IMAGE PREVIEW UPON UPLOAD
// IMAGE CODE TAKEN FROM 

function preview_image(event) 
{
 var reader = new FileReader();
 reader.onload = function()
 {
  var output = document.getElementById('output');
  output.src = reader.result;
 }
 reader.readAsDataURL(event.target.files[0]);

 $('#preview-image').css('display','block');
}

// POP OUT MENUS AND ACTIVATION

$(document).on('click', '#profile-icon', function() {
    $('#profile-pop-out-section').toggle();
})

$(document).on('click', '#image-post-icon', function() {
    $('#image-post').click();
})

$(document).on('click', '#messages-icon', function() {
    $('#messages-pop-out-section').click();
})

// SETTINGS THEMES SWITCHES

$(document).on('click', '#dark_switch', function() {
    $('#light_theme').prop('checked', false);
})

$(document).on('click', '#light_switch', function() {
    $('#dark_theme').prop('checked', false);
})