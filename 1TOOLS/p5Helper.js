function grid(size, sw, sh) {
  for (var r = 0; r < sw / size; r++) {
    for (var c = 0; c < sh / size; c++) {
      stroke(255)
      strokeWeight(1);
      line(0, r * size, sw, r * size);
      line(c * size, 0, c * size, sh);
    }
  }
}

function mouseClicked() {
  console.log("x: " + mouseX);
  console.log("y: " + mouseY);
}
