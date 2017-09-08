var count = 0;

function cc(card) {
// increment the count if card value is <= 6  
  if (card <= 6){
    count++;
  }
// decrement the count for high cards
  switch (card){
    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
      count--;
  }
// every time the function is called it will change the count
// and return the count and what to do. Vegas here I don't come.
  if (count <= 0) {
    return count + " Hold";
  } else {
    return count + " Bet";
  }
}

