const canvas = document.getElementById('canvas1');
//creo una istanza del rendering di canvas, ha built in 2d drawing methods
const ctx = canvas.getContext('2d');
//definisco width e hight della canvas, uso tutto lo schermo
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

//*canvas settings
ctx.fillStyle = 'white';
ctx.strokeStyle = 'white';
ctx.lineWidth = 1;

class Particle {
  constructor(effect) {
    this.effect = effect;
    this.x = Math.floor(Math.random() * this.effect.width);
    this.y = Math.floor(Math.random() * this.effect.height);
  }
  draw(context){
    context.fillRect(this.x, this.y, 50, 50); //(x,y, width, height)
  }
}

//Manager di tutto
class Effect{
  constructor(width, height){
    this.width = width;
    this.height = height;
    this.particles = [];
    this.numberOfParticles = 50;
  }
  init(){
    for(let i = 0 ; i < this.numberOfParticles ; i++){
      this.particles.push(new Particle(this)); //this references Effect class
    }
  }
  render(context){
    this.particles.forEach(particle => {
      particle.draw(context);
    });
  }
}

const effect = new Effect(canvas.width, canvas.height);
effect.init(); //pusha una nuova particella i
effect.render(ctx);
console.log(effect)