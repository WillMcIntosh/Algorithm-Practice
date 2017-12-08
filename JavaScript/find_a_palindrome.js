function palindrome(inputString) {

// replace all special characters with blanks and convert to lowercase
    var lettersString = inputString.replace(/[^a-z0-9]/gi, "").toLowerCase();

// split and reverse the string
    var arr = lettersString.split('');
    arr.reverse();
// rejoin as a new string
    var reverseString = arr.join('');
// returns true or false

    console.log(lettersString === reverseString);

    return lettersString === reverseString;
}

palindrome('Aba a_ba');
