var express = require('express'); // sækjum express
var app = express(); // búum til tilvik af express og geymum það í breytunni app

// skilgreinum rútu (route á ensku) fyrir appið okkar
// ef við förum inn á slóðina localhost:3000 þá fáum við 'Hello world!'
app.get('/', function(req, res){
	res.writeHead(200);
	res.write('Hello world!');
	res.end();
});

// ef við förum inn á slóðina localhost:3000/info þá fáum við 'Very valuable information!'
app.get('/info', function(req, res){
	res.writeHead(200);
	res.write('Very valuable information!');
	res.end();
});

// látum appið hlusta á porti 3000
app.listen(3000, function(){
	console.log('Server is listening on port 3000');
});