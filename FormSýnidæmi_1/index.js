const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({extended: false}));

app.get('/', (req, res) => {
	res.sendFile(__dirname+'/index.html');
});

app.post('/', (req, res) => {	
	password = req.body.password;
	res.redirect('/'+password);
});

app.get('/*', (req, res) => {	
	res.write('HÆ, hvað ert þú að gera hér ?');
	res.end();
});

app.listen(3000, () => {
	console.log('App is listening on port 3000');
});

