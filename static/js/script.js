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


    // DOB VALIDATION 

function dobCheck() {

    var userInput = document.forms['signUpForm']['DOB'].value;
    var popUp = document.getElementById('dob-error')

    if (userInput == '') {
        popUp.innerHTML = 'You Need To Complete This Form!';
    };
};


    // PASSWORD VALIDATION

function passCheck(passTag, passTagTwo, popUpTag) {

    var userInput = document.forms['signUpForm'][passTag].value;
    var passConfirm = document.forms['signUpForm'][passTagTwo].value;
    var popUp = document.getElementById(popUpTag);

    console.log('Function Loaded')
    console.log(userInput)

    if (userInput == '') {
        popUp.innerHTML = 'You Need To Complete This Form!';
        console.log('1st if')
    } else if ( userInput.length < 10) {
        console.log('2nd if')
        popUp.innerHTML = 'Your Password Is Too Small!';
    } else if ( userInput = passConfirm ) {
        console.log('3rd if')
        popUp.innerHTML = 'Password Do Not Match!';
    } else {
        console.log('else')
        popUp.innerHTML = '';
    };
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