var express = require('express'); // includum express
var app = express(); // búum til tilvik af express sem við köllum app

app.use(express.static('main')); // nú fáum við aðgang að css skjölum og öðrum fylgihlutum

// skilgreinum rútu fyrir rótina
app.get('/', function(req, res){
	// látum appið senda skrána index.html en látum eins og það komi frá rót localhost
	// __dirname er í raun slóðin þar sem forritið okkar er
	res.sendFile(__dirname+'/main/index.html');	
});

app.get('/Upplysingar', function(req, res){
	res.sendFile(__dirname+'/main/Upplysingar.html');
});

// skilgreinum rútu fyrir allt annað
/*app.get('/*', function(req, res){
	res.writeHead(404);
	res.write('404 error: Page not found');
	res.end();
});*/

app.listen(3000, function(){
	console.log('Server is listening on port 3000');
});

