
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

  function openRecoveryRequest() {
    Swal.fire({
      title: 'Recovery email',
      html: '<input id="emailInput" class="swal2-input" placeholder="Email">',
      focusConfirm: false,
      showCancelButton: true,
      background: '#141011db',
      color: 'white',
      confirmButtonColor: '#573414',
      preConfirm: () => {
        var email = Swal.getPopup().querySelector('#emailInput').value;
        if (!email) {
          Swal.showValidationMessage('Please enter an email.');
        return false;
        }

        fetch('/password_reset_request/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token
          },
          body: JSON.stringify({ email: email })
        })
        .then(response => {
          if (response.ok) {
            return response.json();
          }
          throw new Error('Network response was not ok.');
        })
        .then(data => {
          if (data.success) {
            Swal.fire('Success', 'Password reset link sent to your email!', 'success');
          } else {
            Swal.fire('Error', 'Email not found in our system', 'error');
          }
        })
        .catch(error => {
          Swal.fire('Error', 'Something went wrong. Please try again.', 'error');
        });
      }
    });
  }