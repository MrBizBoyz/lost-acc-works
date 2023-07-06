$(()=>{
  var sec = 0;
  var tenthSec = 0;
  var min = 0;
  var hour = 0;


 setInterval(()=>{
  sec++;


  if ( sec > 9) {
    sec = 0;
    tenthSec++;
  }


  if (tenthSec > 5) {
    tenthSec  = 0;
    min++;
    hour++;
  }
    console.log(hour + "" + min + ":" + tenthSec + "" + sec );




  }, 10);
});
