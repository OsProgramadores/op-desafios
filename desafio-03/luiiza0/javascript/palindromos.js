function palindromos(num) {
    for (let i = 1; i < num; i++) {
      let converter = i.toString().split("").reverse().join("");
      let reverse = parseInt(converter);
  
      i === reverse ? console.log(i) : "";
    }
  }
  
  palindromos(5000);
  