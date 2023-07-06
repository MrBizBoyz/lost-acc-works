 $(()=>{

  $("#enter").click(() => {
  var textBox = $("#text").val()
  convertnum(textBox);
  })
 });


function convertnum(num){
  if (num >= 1000000) {// th place
    var temp = num / 1000000;
    temp = Math.floor(temp);
    num = num - 1000000 * temp;
      $("#m").html(temp)
  }

  else {
      $("#m").html("0")
  }
  if (num >= 100000) {// th place
    var temp = num / 100000;
    temp = Math.floor(temp);
    num = num - 100000 * temp;
      $("#hTh").html(temp)
  }

  else {
      $("#hTh").html("0")
  }
  if (num >= 10000) {// t th place
    var temp = num / 10000;
    temp = Math.floor(temp);
    num = num - 10000 * temp;
      $("#tTh").html(temp)
  }

  else {
      $("#tTh").html("0")
  }
  if (num >= 1000) {// th place
    var temp = num / 1000;
    temp = Math.floor(temp);
    num = num - 1000 * temp;
    $("#th").html(temp)
  }

  else {
    $("#th").html("0")

  }
if (num >= 100) {// h place
  var temp = num / 100;
  temp = Math.floor(temp);
  num = num - 100 * temp;
    $("#h").html(temp)
}

else {
    $("#h").html("0")
}


if (num >= 10) {// t place
  var temp = num / 10;
  temp = Math.floor(temp);
  num = num - 10 * temp;
    $("#t").html(temp)
}
  $("#o").html(num)

// if (num >= 1) {// ones place
//   var temp = num / 1;
//   temp = Math.floor(temp);
//   num = num - 1 * temp;
//   console.log("1s: " + temp);
// }
//
// else {
//   console.log("1s: 0");
// }







}
