for (let i = 0; i <= 3010; i++) {
  if (String(i) === String(i).split("").reverse().join("")) {
    console.log(i);
  }
}
