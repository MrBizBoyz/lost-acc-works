let max = 10;
let a;
let b;
let text;




function makeRndNum() {
  a = rnd();
  b = rnd();
  $("#problem").html(a + "+" + b + "=");
}

function rnd() {
  return Math.floor(Math.random() * max)
}

$(document).ready(()=>{
  makeRndNum();
  resetTextBox();


  $("#button").click(()=>{
   check();
  });


  $("#textBox").keyup((e)=>{
    if(e.which === 13){
      check();
    }
  });

});

function check(){
  var awnser = parseInt($("#textBox").val());

  if(a + b === awnser){
    $("#result").html("(:");
    makeRndNum();
    resetTextBox();
  }

  else{
    $("#result").html("):");
    resetTextBox();
  }
}


function resetTextBox(){
  $("#textBox").focus();
  $("#textBox").val("");
}
