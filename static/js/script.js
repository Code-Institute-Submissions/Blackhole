// SIGN UP FORM

    // FORM VALIDATION

function formCheck(formTag, popUpTag, pattern, minLimit) {
    
    var userInput = document.forms['signUpForm'][formTag].value;
    var popUp = document.getElementById(popUpTag);

    if (userInput == '') {
        popUp.innerHTML = 'You Need To Complete This Form!'
    } else if (userInput.length < minLimit) {
        popUp.innerHTML = `You Need To Enter More Than ${minLimit} Letters!`;
    } else if(userInput.match(pattern)) {
        popUp.innerHTML = '';
    } else {
        popUp.innerHTML = 'You Can Only Enter Letters!'
    }
};


    // USERNAME VALIDATION 

function usernameCheck() {
    var userInput = document.forms['signUpForm']['username'].value;
    var popUp = document.getElementById('username-error')
    var pattern = /^[A-Za-z0-9]+$/;

    if (userInput.length < 5) {
        popUp.innerHTML = 'You Need To Enter More Than 3 Characters!'
    } else if ( userInput ){

    }
}

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