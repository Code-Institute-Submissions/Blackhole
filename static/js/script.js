// SIGN UP FORM

    // FORM VALIDATION

function formCheck(formTag, popUpTag, pattern, minLimit, returnSpecific) {
    
    var userInput = document.forms['signUpForm'][formTag].value;
    var popUp = document.getElementById(popUpTag);

    if (userInput == '') {
        popUp.innerHTML = 'You Need To Complete This Form!';
    } else if (userInput.length < minLimit) {
        popUp.innerHTML = `You Need To Enter Atleast ${minLimit} ${returnSpecific}!`;
    } else if(userInput.match(pattern)) {
        popUp.innerHTML = '';
    } else {
        popUp.innerHTML = `You Can Only Enter ${returnSpecific}!`;
    };
};


    // PASSWORD VALIDATION

function passCheck(passTag, passTagTwo, popUpTag) {

    var userInput = document.forms['signUpForm'][passTag].value;
    var passConfirm = document.forms['signUpForm'][passTagTwo].value;
    var popUp = document.getElementById(popUpTag);

    if (userInput == '') {
        popUp.innerHTML = 'You Need To Complete This Form!';
    } else if ( userInput.length < 10) {
        popUp.innerHTML = 'Your Password Is Too Small!';
    } else {
        popUp.innerHTML = '';
    };
};


// MATERALIZE FUNCTIONS

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
  var output = document.getElementById('image-output');
  output.src = reader.result;
 }
 reader.readAsDataURL(event.target.files[0]);

 $('#preview-image').css('display','block');
}


// CLEARING INPUT 

$(document).on('click', '#clear-post', function() {
    $('#activity-post').val('');
    $('#image-post').val('');
    $('#preview-image').css('display','none');
    location.reload();
})

// OPENING IMAGE UPLOAD

$(document).on('click', '#image-post-icon', function() {
    $('#image-post').click();
})

// SETTINGS THEMES SWITCHES

$(document).on('click', '#dark_switch', function() {
    $('#light_theme').prop('checked', false);
})

$(document).on('click', '#light_switch', function() {
    $('#dark_theme').prop('checked', false);
})