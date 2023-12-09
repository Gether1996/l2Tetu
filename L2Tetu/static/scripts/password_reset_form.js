function resetPassword(userId) {
    console.log(userId);
    var newPassword1 = document.getElementById('newPassword1').value;
    var newPassword2 = document.getElementById('newPassword2').value;

    if (!newPassword1) {
        alert("New password cannot be empty");
        return;
    }

    if (newPassword1 != newPassword2) {
        alert("Passwords don't match.");
        return;
    }

    if (newPassword1.length > 16) {
        alert("Maximum password length is 16 characters");
        return;
    }

    // Prepare data for the POST request
    var data = {
        id: userId,
        new_password: newPassword1,
    };

    // Make a POST request using the fetch API
    fetch('/password_reset_confirm_post/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Password reset failed');
        }
        // Redirect to the success page after a successful password reset
        window.location.href = '/password_reset_success/' + userId + '/';
    })
    .catch(error => {
        // Handle errors
        console.error('Password reset error', error);
    });
}