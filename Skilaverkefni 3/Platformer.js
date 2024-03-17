const canvas = document.getElementById("myCanvas")
const ctx = canvas.getContext("2d")

const KEY_LEFT = 37;
const KEY_RIGHT = 39;
const KEY_UP = 38;
const KEY_DOWN = 40;
const KEY_SPACE = 32;
const KEY_S = 83;

setInterval(handleKeys, requestAnimationFrame)

document.addEventListener("keydown", keydown)

document.addEventListener("keyup", keyup)

const hero = 
{
    x_coord: canvas.width/2.3,
    y_coord: 1000,
    width: 50,
    height: 120,
    speed: 5,
    velocityX: 0,
    velocityY: 0,
    jumping: false
}

class Goblin
{
    constructor()
    {
        this.x = Math.random()*15
        this.y = 60
        this.width = 40
        this.height = 35
        this.speed = 2
    }
    draw()
    {
        ctx.fillStyle = "green"
        this.x += this.speed
        if (this.x+this.width >= canvas.width)
        {
            this.speed *= -1
        }
        if (this.x+this.width <= this.width)
        {
            this.speed *= -1
        }
        ctx.fillRect(this.x, this.y, this.width, this.height, this.speed)
        
    }
}

const keys = []
const enemies = []
enemies.push(new Goblin())

function game_draw() 
{
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    hero.velocityX *= 0.9;
    hero.velocityY += 0.5;
    hero.x_coord += hero.velocityX;
    hero.y_coord += hero.velocityY;

    if (hero.x_coord >= canvas.width - hero.width)
    {
        hero.x_coord =  0
    }   else if (hero.x_coord <= 0) 
    {
        hero.x_coord = canvas.width-hero.width
    }

    if (hero.y_coord >= canvas.height - hero.height)
    {
        hero.y_coord = canvas.height - hero.height
        hero.jumping = false
    }
    ctx.fillStyle = "white"
    ctx.fillRect(0,0, canvas.width, canvas.height)
    ctx.fillStyle = "#0000FF";
    ctx.fillRect(hero.x_coord, hero.y_coord, hero.width, hero.height);

    for (let i = 0; i < enemies.length; i++)
    {
        enemies[i].draw()
    }

    requestAnimationFrame(game_draw);

}


function keydown(event)
{
    if(event.keyCode == KEY_LEFT || event.keyCode == KEY_RIGHT ||
       event.keyCode == KEY_UP   || event.keyCode == KEY_SPACE ||
       event.keyCode == KEY_S)
    {
        keys[event.keyCode] = true;
    }
}

function keyup(event)
{
    if(event.keyCode == KEY_LEFT || event.keyCode == KEY_RIGHT ||
       event.keyCode == KEY_UP   || event.keyCode == KEY_SPACE ||
       event.keyCode == KEY_S)
    {
        keys[event.keyCode] = false;
    }
}


function handleKeys()
{
    if(keys[KEY_LEFT] == true)
    {
        if (hero.velocityX > -hero.speed)
        {
            hero.velocityX--;
        }
    }

    if(keys[KEY_RIGHT] == true)
    {
        if (hero.velocityX < hero.speed)
        {
            hero.velocityX++;
        }
    }

    if(keys[KEY_UP] == true)
    {
        if (!hero.jumping)
        {
            hero.velocityY = -hero.speed *2;
            hero.jumping = true
        }
    }

    if(keys[KEY_SPACE] == true)
    {
        hero.shoot();
    }

    if(keys[KEY_S] == true) 
    {

    }
}



game_draw()



















