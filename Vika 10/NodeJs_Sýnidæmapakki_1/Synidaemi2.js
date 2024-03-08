var http = require('http'); // sækjum http module-ið
var fs = require('fs'); // sækjum fs module-ið

http.createServer(function(req, res){
	// köllum á readFile aðferðina í file system (eða fs)
	fs.readFile('main/index.html', function(err, data){
		res.writeHead(200);
		// skrifum innihald skránnar í response-ið okkar
		res.write(data);
		res.end();
	});
}).listen(8080);
console.log('Server is listening on port 8080');