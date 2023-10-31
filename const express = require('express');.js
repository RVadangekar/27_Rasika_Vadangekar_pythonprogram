const express = require('express');
const app = express();
app.post('/post', function(req, res) {
res.send('posting…');
});
app.all('/hello', function(req, res) {
res.send('hello…');
});
app.listen(5000);
console.log("Server running on port 5000");