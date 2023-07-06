$(()=>{

});




let bill = $("#bill");
let billWidth = bill.width();
let billHeight = bill.height();
let width = $(window).width();
let height = $(window).height();




$(()=>{
  console.log("jquery");


  // bill.attr('height', billWidth + "px");
  bill.css({
    "position": "absolute",
    "left" : (width / 2) - (billWidth / 2),
    "top" : (height / 2) - (billWidth / 2)
   });

   bill.click(()=>{
     click();
   });

   bill.hover(()=>{
     hover();
   });

   // setInterval(function(){
   //    backgroundColorChange();
   //  }, 1);
});


function click(){

  moveBill();

}

function hover(){
  let max = 3;
  let chance = Math.floor(Math.random() * max);
console.log(chance);
  if(chance === max -1){
    moveBill();
  }
}

function moveBill(){
  let x = Math.floor(Math.random() * ((width - billWidth) - 0)) + 0;
  let y = Math.floor(Math.random() * ((height - billHeight) - 0)) + 0;

  bill.animate({
    "left" : x,
     "top" : y
    });
}

function backgroundColorChange(){

  let r = Math.floor(Math.random() * 255);
  let g = Math.floor(Math.random() * 255);
  let b = Math.floor(Math.random() * 255);

  $("body").css("background-color", "rgba(" + r + "," + g + "," + b + " ,0.5)");//changes background color
}
