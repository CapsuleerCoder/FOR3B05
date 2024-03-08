// sækjum http module-ið
var http = require('http');
// gerum serverinn, hann hlustar eftir request og svarar með response
http.createServer(function(req, res){ 
	res.writeHead(200, {'Content-Type': 'text/html'});
	// skrifum Hello world! 
	res.write('Hello world!');
	// endum response-ið
	res.end();
	// hlustum á localhost (IP tala 127.0.0.1) á porti 80
}).listen(8080, '127.0.0.1');
// hefðum líka getað gert serverinn svona
/*
var server = http.createServer();
server.on('request', function(req, res){	
	res.writeHead(200, {'Content-Type': 'text/html'});
	res.write('Hello world!');
	res.end();
});
server.listen(8080, '127.0.0.1')	;
*/
console.log('Server is listening on port 8080');