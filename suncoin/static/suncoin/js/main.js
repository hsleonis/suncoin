jQuery(document).ready(function($){
    $("form.captcha-form").submit(function(event) {

       //var googleResponse = $("#g-recaptcha-response").val();
       if (grecaptcha.getResponse() == ""){
            event.preventDefault();
            $('<p style="color:red !important" class=error-captcha"><span class="glyphicon glyphicon-remove " ></span> Please fill up the captcha.</p>" ').insertAfter("form.captcha-form");
       }
    });
});