

//undirbúum strigann(canvasinn) fyrir teikningar

const c = document.getElementById("myCanvas");
const ctx = c.getContext("2d");

//gerum nokkrar grunneiningar eins og boxið, stigaskore og leikhraða
let box = 32;
let stigaskor = 0;
let gameSpeed = 100;

//gerum breytu sem geymir stefnu snáksins
let d; 


// Sækja myndirnar okkar
const ground = new Image();
ground.src = "Snake_Myndir_Og_Hljóð/img/ground";

const apple = new Image();
apple.src = "Snake_Myndir_Og_Hljóð/img/food";

//gerum snákinn
let snake = [];
snake[0] = {
    x: 9*box,
    y: 10*box
}

//gerum eplið
let apple = {
    x:Math.floor(Math.random()*17+1)*box,
    y:Math.floor(Math.random()*15+3)*box,
}
//sækjum hljóðið okkar
const eat =new Audio();
eat.src ="audio/eat.mp3";
const dead =new Audio();
eat.src ="audio/dead.mp3";

//gerum teiknifall sem teiknar allt saman
function draw(){
    ctx.drawImage(ground, 0, 0);
    ctx.drawImage(apple, apple.x, apple.y);

    for (let i=0; i<snake.length; i++){
        if (i==0){
            ctx.fillStyle = "black";
        } else {
            ctx.fillStyle = "white";
        }
        
        ctx.strokeRect(snake[i].x, snake[i].y, box, box);
        ctx.strokeStyle = "red";
        ctx.strokeRect(snake[i].x, snake[i].y, box, box);
    }

    //skrásetjum hvar hausinn er núna
    let snakeX = snake[0].x
    let snakeY = snake[0].y
    //athugum hvað er í d breytunni og breytum snakeX og snakeY hnitum í samræni við það 
    if (d === "LEFT"){ snakeX -= box};
    if (d === "Up"){ snakeY -= box};
    if (d === "Right"){ snakeX += box};
    if (d === "Down"){ snakeY += box};


    //gerum nýjan haus
    let newHead = {
        x: snakeX,
        y: snakeY
    }
    //athugum hvort við rekumst á eplið
    if (newHead.x === apple.x && newHead.Y === apple.y){
        stigaskor++
        apple = {
            x:Math.floor(Math.random()*17+1)*box,
            y:Math.floor(Math.random()*15+3)*box,
        } 
        eat.play();
    } else {
        snake.pop();    //tökum  skottið burt
    }
    
    //bætum nýja hausnum við fremst
    snake.unshift(newHead);

 


    ctx.fillStyle = "white";
    ctx.font = "40px Arial";
    ctx.fillText(stigaskor, 2.4*box, 1.6*box)
}
//gerum fall sem leyfir okkur að breyta stefnu snáksins
function direction(event) {
    if (event.keyCode === 37 && d != "RIGHT") {
        d = "LEFT";
    } else  if (event.keyCode === 38 && d != "DOWN") {
        d = "UP";
    } else  if (event.keyCode === 39 && d != "LEFT") {
        d = "RIGHT";
    } else  if (event.keyCode === 40 && d != "UP") {
        d = "DOWN";
    }


}





//hlustum eftir keydown atburði á skjali
document.addEventListener("keydown", direction)

//setjum leikjalykkjuna af stað
let game = setInterval(draw, gameSpeed);








