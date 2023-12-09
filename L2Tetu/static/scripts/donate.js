$(document).ready(function () {
  $('#coins').on('input', function () {
    var coins = $(this).val();
    var dollarCost = calculateDollarCost(coins);

    // Update the dollar cost input field
    $('#dollar-cost').val('$' + dollarCost.toFixed(2));
  });
});

function calculateDollarCost(coins) {
  var baseDollarCost = coins / 30; // Assuming 30 coins = $1
  var bonus = 0;

  if (coins > 599) {
    bonus = baseDollarCost * 0.10; // 10% bonus for coins above 600
  }

  var totalDollarCost = baseDollarCost - bonus;

  return totalDollarCost;
}

function validateAndPrepareCheckout() {
    var coins = parseFloat(document.getElementById('coins').value);
    var dollarCostField = document.getElementById('dollar-cost');
    var dollarCost = parseFloat(dollarCostField.value.replace('$', ''));

    console.log(coins);
    console.log(dollarCost);

    // Ensure the Dollar Cost is at least $5
    if (isNaN(dollarCost) || dollarCost < 5) {
        alert('Dollar Cost must be a minimum of $5.');
        return false;  // Prevent form submission
    }

    // Prepare Checkout
    var checkoutLink = document.getElementById('checkout-link');
    checkoutLink.href = 'checkout/?coins=' + coins + '&dollars=' + dollarCost;
    window.location.href = checkoutLink.href;

    return true;  // Allow form submission if validation passes and checkout is prepared
}