const express = require('express');
const path = require('path');

const app = express();
const port = 3002;

let timeout = 0;

// sendFile will go here
app.get('/', function (_, res) {
	setTimeout(() => {
		res.sendFile(path.join(__dirname, '/index.html'));
	}, timeout);
});

app.get('/delay', function (req, res) {
    timeout = req.query.timeout;
    res.send('timeout set to ' + timeout);
});

app.listen(port);
console.log('Server started at http://localhost:' + port);
