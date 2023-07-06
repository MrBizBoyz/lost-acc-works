$(()=>{



  $("#button").click(()=>{
    var text = $("#textBox").val();
    $("#h1").html("my name is " + text + " and i'm cool ");


      $("#h1").animate({
        fontSize: "50px",
        marginTop: "300px"
      }, 2000);


    });

    $("#h1").click(()=>{

      $("#button").hide();
    })


});




// $("body").css("background-color", "red");
