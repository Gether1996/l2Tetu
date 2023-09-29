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