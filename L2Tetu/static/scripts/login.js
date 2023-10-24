$(document).ready(function() {
    $('#login-button').on('click', function() {
        var username = $('#username').val();
        var password = $('#password').val();

        $.ajax({
            url: '/custom_login/',
            type: 'post',
            data: {
                'username': username,
                'password': password
            },
            headers: {
                'X-CSRFToken': csrf_token
            },
            success: function(response) {
                if (response.success) {
                    Swal.fire({
                        position: 'top',
                        icon: 'success',
                        background: 'rgba(33, 29, 30, 0.6)',
                        title: 'Welcome ' + username + '!',
                        timer: 1000,
                        showConfirmButton: false
                    }).then(function() {
                        window.location.href = '/accounts/profile/';
                    });
                } else {
                    Swal.fire({
                        icon: 'error',
                        text: response.message
                    });
                }
            }
        });
    });
});

var passwordInput = document.getElementById('password');
var togglePassword = document.getElementById('toggle-password');

togglePassword.addEventListener('click', function () {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        togglePassword.classList.remove('fa-eye');
        togglePassword.classList.add('fa-eye-slash');
    } else {
        passwordInput.type = 'password';
        togglePassword.classList.remove('fa-eye-slash');
        togglePassword.classList.add('fa-eye');
    }
});