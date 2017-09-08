var count = 0;

function cc(card) {
  
  if (card <= 6){
    count++;
  }
  switch (card){
    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
      count--;
  }

  if (count <= 0) {
    return count + " Hold";
  } else {
    return count + " Bet";
  }
}

