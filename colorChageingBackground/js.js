
$(()=>{
  var color;
   $("#cb").change(()=>{
     color = $("#cb").val();
     switch (color) {
       case "green":
        $("body").css("background-color", "green");
        break;


       case "yellow":
       $("body").css("background-color", "yellow");

         break;


       case "blue":
       $("body").css("background-color", "blue");

         break;


       case "red":
       $("body").css("background-color", "red");

         break;
       }
   });
});
