function palindromos(a, b) {
  if (isNaN(a) || isNaN(b)) return;
  for (i = a; i<=b; i++) {
  var nArr = String(i).split("").map((a)=>{
  return Number(a)
  })
  let zArr = [];
  for (j = nArr.length; j > 0; j--) {
    zArr.push(nArr[j - 1])
  }
  if (JSON.stringify(nArr) === JSON.stringify(zArr))
    console.log(i);
  }
}
palindromos(1, 1000);