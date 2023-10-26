function transferCoins(charId) {
    var characters = json_data_chars;
    var user_coins = json_data_user_coins;

    // Find the selected character by ID
    var selectedCharacter = characters.find(function(character) {
        return character.id === charId;
    });

    Swal.fire({
        title: `Transfer Coins to ${selectedCharacter.name}`,
        html: `
            <label for="transferAmount">Amount to Transfer:</label>
            <input type="number" id="transferAmount" min="1" max="${user_coins.user_coins}" step="1">
        `,
        showCloseButton: true,
        showConfirmButton: true,
        confirmButtonText: 'Transfer',
        preConfirm: () => {
            // Get values from the SweetAlert2 input fields
            var transferAmount = parseInt(document.getElementById('transferAmount').value, 10); // Convert the input to an integer with base 10
            var walletCoins = parseInt(user_coins.user_coins, 10); // Convert wallet.coins to an integer

            if (isNaN(transferAmount) || transferAmount <= 0 || transferAmount > walletCoins) {
                Swal.showValidationMessage('Invalid transfer amount.');
                return false;
            }

            fetch('/transfer_coins/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    charId: charId,
                    transferAmount: transferAmount,
                }),
            })
            .then(response => {
                if (response.ok) {
                    Swal.fire({
                      position: 'top',
                      title: `${transferAmount} transfered to ${selectedCharacter.name} successfuly.`,
                      icon: 'success',
                      showConfirmButton: false,
                      timer: 900
                    });
                    setTimeout(function() {
                          location.reload();
                        }, 900);
                } else {
                    throw new Error('Failed to update position data');
                }
            });
        },
    });
}