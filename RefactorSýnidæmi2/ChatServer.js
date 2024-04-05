const app = require('express')();
const server = require('http').Server(app);
const io = require('socket.io')(server);
// sækjum næst routerinn úr routes möppunni
const router = require('./routes/index');

// nýtum okkur routerinn okkar sem við sóttum frá index.js í routes möppunni
app.use('/', router);

// hlustum eftir connection atburð á servernum og
// skrifum svarfall fyrir þann atburð
io.on('connection', function(socket){
	console.log('a new user has connected');
	// hlustum eftir því að einhver hafi aftengst
	socket.on('disconnect', function(){
		console.log('user disconnected');
	});
	// hlustum eftir því að einhver hafi sent skilaboð
	socket.on('chatmsg', function(msg){
		// sendum skilaboðin til allra biðlaranna/clientanna
		io.emit('chatmsg', msg);
	});

});

// látum serverinn okkar hlusta á porti 3000
server.listen(3000, function(){
	console.log('Server is listening on port 3000');
})

