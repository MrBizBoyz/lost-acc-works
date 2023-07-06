$(function(){
  console.log("jq");
  // $("#text").keyup(function(e){
  //   $("#h1").val()

    $("body").keyup((e)=>{
      $("#result").html("KEY CODE: " + e.which);

    });

  });
