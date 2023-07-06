$(()=>{


//jordan
  //$("#button").click(()=>{

    //var tb = $("#input").val()
    //var name = tb.split("");
    //name[0] = name[0].toUpperCase();
    //var result = name.join("");
    //$("#result").html(result)


  //});




  var name = "racecar";
  var nameSplit = name.split("");
  var backwardsArray = [];

  // if (name === bs) {
  //
  // }


  for (var i = nameSplit.length -1; i >= 0; i--) {
    backwardsArray.push(nameSplit[i]);
  }
  var bs = backwardsArray.join("");

  if(name === bs){
    console.log("is a palodrom");
  }
  else{
      console.log("not a palodrom");
  }
});
