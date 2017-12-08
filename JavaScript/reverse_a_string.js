function reverseString(str) {
  let arr=str.split('');
  let revArr=[];
  for( let i=arr.length-1;i>=0;i--){
    revArr.push(arr[i]);
  }
  str = revArr.join('');
  return str;
}
reverseString("hello");
