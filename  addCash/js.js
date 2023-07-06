


$(()=>{
  $("#Q").focus();
  $("#Q").select();


  $("#Q").keyup((e)=>{
    if(e.which === 13){
      $("#D").select();

    }
  });

  $("#D").keyup((e)=>{
    if(e.which === 13){
      $("#N").select();
    }
  });

  $("#N").keyup((e)=>{
    if(e.which === 13){
      $("#P").select();
    }
  });

  $("#P").keyup((e)=>{
    if(e.which === 13){
      add();
    }
  });








  $("#button").click(()=>{
    //total();
    add

  });

  function add(){
    var q = parseInt($("#Q").val()) * 0.25;
    var n = parseInt($("#N").val()) * 0.05;
    var d = parseInt($("#D").val()) * 0.10;
    var p = parseInt($("#P").val()) * 0.01;
    var total = q + n + d + p;
    $("#h1").html("$"+total)
  }

});
