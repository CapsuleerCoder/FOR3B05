const express = require('express');
const path = require('path');
const router = 	express();

// skrifum leið/rútu fyrir routerinn okkar
router.get('/', function(req, res){
	res.sendFile(path.join(__dirname, '../ChatServer.html'));
});

// skrifum aðra leið fyrir routerinn
router.get('/*', function(req, res){
	res.write('Adgangur oheimill!');
	res.end();
});

// flytjum routerinn út
module.exports = router;


