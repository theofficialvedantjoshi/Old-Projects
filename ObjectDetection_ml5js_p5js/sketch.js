let img;
let detector;
function preload(){
  img = loadImage('dog_cat.jpg');
  detector = ml5.objectDetector('cocossd');

}
function gotDetections(error, results) {
  if(error){
    console.log(error);
  }
  console.log(results);
  for (let i=0; i <results.length; i++) {
    let object = results[i];
    stroke(0,255,0);
    strokeWeight(4);
    noFill();
    rect(object.x,object.y,object.width,object.height);
    noStroke();
    fill(0);
    textSize(24);
    text(object.label,object.x +10,object.y +10);
    noStroke();
    fill(0);
    textSize(24);
    text("Confidence:"+nf(object.confidence * 100,2,0) + " percent",object.x +100,object.y +100);
  }
}
function setup() {
  createCanvas(640, 480);
  //console.log(detector);
  image(img,0,0);
  detector.detect(img, gotDetections);
}


