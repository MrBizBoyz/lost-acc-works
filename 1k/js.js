console.log("share the love");



function k(x) {
  if (x < 1000) {
    return x;
  }

  else {
    var k = x / 1000
    return k + "k";
  }
}

console.log(k(800));
console.log(k(1234));
