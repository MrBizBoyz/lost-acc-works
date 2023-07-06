var gameWidth = 400;
var gameHeight = 400;
var c;
var x;
var y;
var boxSize = 50;
var pumpkinImg;
var raindropImg;
var pumpkin;
var raindrop;
var score = 0;

function preload() {
  pumpkinImg = loadImage('images/jacko.png');
  raindropImg = loadImage('images/raindrop.png');
}

function setup(){
  c = createCanvas(gameWidth, gameHeight);
  c.parent("canvas");
  noCursor();
  pumpkin = new Pumpkin(pumpkinImg);
  raindrop = new RainDrop(raindropImg);
}


function update() {
  pumpkin.update();
  raindrop.update();
}


function draw() {
  update();
  background(100);
  pumpkin.draw();
  raindrop.draw();
}

class Item{
  constructor(pic) {
    this.x = x;
    this.y = y;
    this.size = 50;
    this.pic = pic;

  }

  update(){

  }

  draw(){
    image(this.pic, this.x - this.size / 2, this.y - this.size / 2, this.size, this.size, 0, 0, this.pic.width, this.pic.height)
  }
}

class RainDrop extends Item{
  constructor(pic) {
    super(pic);
    this.x = Math.random() * (gameWidth - this.size);
    this.y = -this.size;
    this.speed = 3;

  }

  update(){
    this.y += this.speed;
    if(this.y  - this.size / 2> gameHeight){
      this.x = Math.random() * (gameWidth - this.size);
      this.y = -this.size;
      score++;
    }
  }
}

class Pumpkin extends Item{
  constructor(pic) {
    super(pic);
  }

  update(){
    this.x = mouseX;
    this.y = mouseY;
  }
}
