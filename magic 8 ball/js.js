///// magic 8 ball //////

var answers = ["yes","no","not so sure","not so good","porblay","ask again"] ;





$(function(){

  $("#button").click(function(){
    if($("#textBox").val()){
      ask();
    }


  });




});

function ask (){
  var rnd = Math.floor(Math.random() * answers.length);
  $("#result").html(answers[rnd]);

}
