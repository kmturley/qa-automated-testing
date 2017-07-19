const express = require('express')
const app = express()

app.use(express.static(__dirname + '/static'))

// Allow cross origin requests
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

// Return json response
app.get('/api', function(req, res) {
  res.json({message: 'JSON: ' + new Date().toUTCString()})
})

app.listen(3000, function () {
  console.log('listening on *:3000')
})