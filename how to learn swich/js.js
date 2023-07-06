var screenHight = 800
var screenwidth = 800



function setup() {
  createCanvas(800, 800);

}


function draw() {
  background(51);
  drawBox("purple");
}


function drawBox(color) {
  // if (color === "red") {
  // fill(255,0,0);
  // }
  //
  // else if (color === "green") {
  //   fill(0,255,0);
  // }
  //
  //
  // else if (color === "bule") {
  //   fill(0,0,255);
  // }
  //
  // else {
  //   fill(255);
  // }

  switch (color) {
    case "red":
      fill(255,0,0);
      break;
    case "green":
      fill(0,255,0);
      break;
    case "blue":
      fill(0,0,255);
      break;
    default:
      fill(255);

  }
  rect(100, 100, 100, 100);
}

function update() {

}
