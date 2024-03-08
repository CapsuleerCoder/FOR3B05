var c = document.getElementById('teikniblad');
var ctx = c.getContext('2d');
var shape = "kassi"; // Breyta sem segir okkur hverskonar form á að teikna		
var start_x; // Upphafshnit
var start_y; // Upphafshnit
var radius; // Radíus hrings
var width; // Vídd ferhyrnings
var height; // Hæð ferhyrnings
var colorSelector = document.getElementById('color_selector');
var hringTakki = document.getElementById('hringur');
var kassaTakki = document.getElementById('kassi');
var linuTakki = document.getElementById('lina');
var clearTakki = document.getElementById('clear');
var lineWidthSelector = document.getElementById('lineWidth');
var undoArray = [];
var redoArray = [];
var undoTakki = document.getElementById('undo')
var redoTakki = document.getElementById('redo')
var img = new Image();
saveCanvasState()

c.addEventListener('mousedown', start); // forritið hlustar eftir atburðinum mousedown (þ.e.a.s. að músatakka sé haldið niðri) og bregst við honum með svarfallinu start
c.addEventListener('mouseup', addShape); // sama og að ofan nema fyrir mouseup sem er þegar músatakka er sleppt og svarfallið er addShape

hringTakki.addEventListener('click', changeShape);
kassaTakki.addEventListener('click', changeShape);
linuTakki.addEventListener('click', changeShape);
lineWidthSelector.addEventListener('change', lineWidth);
clear.addEventListener('click', clearCanvas);
colorSelector.addEventListener('input', litaVal);
undoTakki.addEventListener('click', undoLast);
redoTakki.addEventListener('click', redoLast);

function litaVal (event) {
        ctx.fillStyle = event.target.value;
        ctx.strokeStyle = event.target.value;
}

function clearCanvas() {
        ctx.fillStyle = 'white'; 
        ctx.fillRect(0, 0, c.width, c.height);
}

function lineWidth(event) {
        ctx.lineWidth = event.target.value; 
}

function changeColor(event) {
    ctx.strokeStyle = event.target.id;
}

function changeShape(event) {
    shape = event.target.id;
}

function start(event) 
{
    start_x = event.offsetX;
    start_y = event.offsetY;
}

function isFilled() {
    return document.querySelector('input[name="fill_type"]:checked').value === 'Filled';
}

function saveCanvasState() {
    undoArray.push(c.toDataURL());
}

function undoLast() {
    if (undoArray.length > 0) { 
        redoArray.push(undoArray.pop());
        redrawCanvas(undoArray[undoArray.length - 1]);
    }
}

function redoLast() {
    if (redoArray.length > 0) {
        undoArray.push(redoArray.pop());
        redrawCanvas(undoArray[undoArray.length - 1]);
    }
}

function redrawCanvas(dataURL) {
    img.onload = function() {
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.drawImage(img, 0, 0, c.width, c.height);
    };
    img.src = dataURL;
}

function addShape(event) {
    						
    switch (shape) {
        case "kassi":				
            width = event.offsetX - start_x;
            height = event.offsetY - start_y;				                
            ctx.beginPath();
            ctx.rect(start_x, start_y, width, height);
            if (isFilled()) {
                ctx.fill();
            } else {
                ctx.stroke();
            }
            ctx.closePath();
            break;
        case "hringur":
            var a = event.offsetX - start_x;
            var b = event.offsetY - start_y;
            radius = Math.sqrt(a*a + b*b);
            ctx.beginPath();
            ctx.arc(start_x, start_y, radius, 0, 2 * Math.PI);
            if (isFilled()) {
                ctx.fill();
            } else {
                ctx.stroke(); 
            }
            ctx.closePath();
            break;
        case "lina":
            ctx.beginPath();
            ctx.moveTo(start_x, start_y);
            ctx.lineTo(event.offsetX, event.offsetY);
            ctx.stroke();
            ctx.closePath();
            break;
    }
    saveCanvasState();			
}