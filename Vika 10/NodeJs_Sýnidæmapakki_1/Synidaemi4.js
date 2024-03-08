var express = require('express');
var app = express();

// skilgreinum rútu fyrir rótina
app.get('/', function(req, res){
	// látum appið senda skrána index.html en látum eins og það komi frá rót localhost
	res.sendFile(__dirname+'/main/index.html');	
});

// hér vantar okkur rútu fyrir Upplysingar til að geta séð Upplysingar.html

app.listen(3000, function(){
	console.log('Server is listening on port 3000');
});