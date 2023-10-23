function logoutConfirmation() {
    Swal.fire({
        title: 'Log-out?',
        icon: 'warning',
        iconColor: '#573414',
        showCancelButton: true,
        confirmButtonText: 'Yes',
        confirmButtonColor: '#573414',
        cancelButtonText: 'No'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/logout/";
        }
    });
}