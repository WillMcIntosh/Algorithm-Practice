function checkPalindrome(inputString) {
//take the input string and put it into an array, splitting with ''
  let arr = inputString.split('');
  let revArr = [];
  let newString = '';
// so from length -1 to 0 indices in the array, take each one and pus h it to a new array
    for( let i=arr.length-1;i>=0;i--){
    revArr.push(arr[i]);
  }
  newString = revArr.join('');
// instead of having to write if (x === y) return true, can
// just return the output of the test. neater. 
  return inputString === newString
}
