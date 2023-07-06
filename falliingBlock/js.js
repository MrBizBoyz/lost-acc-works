
let gameWidth = 600;
let gameheight = 400;
let boxSize = 40;
let speed = 10;
let drivingCar;
let person;

function setup() {
  createCanvas(gameWidth, gameheight );
  drivingCar = new DrivingCar();
  person = new Person();

}
  function draw() {
  update();
  background(51);
// fill(255,0,0);
   // rect(x,y, boxSize, boxSize);
   // y = y + speed;

  drivingCar.draw()
  person.draw()


}
// if(y > gameheight ){
//     y = -boxSize;

//}
//}

  function update() {
    person.update()
  }

  class DrivingCar {
  constructor() {
  this.x = 50;
  this.y = 0;
  this.boxSize = boxSize;
  }
  update(){

  }



  draw(){
    fill(255,0,0);
    rect(this.x,this.y, this.boxSize, this.boxSize);
    this.y = this.y + speed;
    if(this.y > gameheight ){
      this.y = -boxSize;
    }
  }
}
