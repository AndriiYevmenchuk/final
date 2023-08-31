$(document).ready(() => {

    let correct1 = false;
    let correct2 = true;
    let correct3 = true;
    let correct4 = false;

    let regExp1 = /^[a-zA-Z]{1}[a-zA-Z0-9_\-]{5,15}$/;
    let regExp2 = /^[a-zA-Z0-9_\-]{5,15}$/;
    let regExp3 = /^...$/;

    $('#login').blur(() => {
        let loginX = $('#login').val();
        if (regExp1.test(loginX)){
            //перевірка зайнятості логіну
            $.ajax({
                url: '/users/ajax_reg',
                data: 'login=' + loginX,
                success: function(response) {
                    if (response.message == 'зайнятий'){
                        $('#login-mess').text('логін зайнятий')
                        correct1 = false;
                    }else{
                        $('#login-mess').text('')
                        correct1 = true;
                    }
                }
            });
        }else{
            correct1 = false;
            $('#login-mess').text('логін не відповідає вимогам безпеки')
        }
    });


    $('#email').blur(() => {
        let emailX = $('#email').val();
        $.ajax({
                url: '/users/ajax_reg_email',
                data: 'email=' + emailX,
                success: function(response) {
                    if (response.message == 'зайнятий'){
                        $('#email-mess').text('email зайнятий')
                        correct4 = false;
                    }else{
                        $('#email-mess').text('')
                        correct4 = true;
                    }
                }
            });
    });

    $('#pass1').blur(() => {
        let pass1X = $('#pass1').val();
        if (regExp2.test(pass1X)){
            correct2=true;
        }else{
            $('#pass1-mess').text('пароль має бути від 6 до 16 символів і може містити лише цифри,букви та _')
            correct2=false;
        }
    });

    $('#submit').click(() => {
        if (correct1 && correct2 && correct3 && correct4){
            $('#form1').attr('onsubmit', 'return true');
        }else{
            $('#form1').attr('onsubmit', 'return false');
            alert('форма має некоректні дані')
        }
    });



});