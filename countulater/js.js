$(()=>{
  $("#button").click(()=>{
    var textbox1 =  parseInt($("#text").val());
    var textbox2 =  parseInt($("#text2").val());
    $("#h1").html( textbox1 + textbox2 + 100)
  });
});
