function palindrome(str) {
  let arr=str.split('');
  let revArr=[];
  let newstr='';
  for( let i=arr.length-1;i>=0;i--){
    revArr.push(arr[i]);
  }
  newstr = revArr.join('');
  if(newstr === str) {
    return true;
  }else {
    return false;
  }
}

palindrome("not a palindrome");
