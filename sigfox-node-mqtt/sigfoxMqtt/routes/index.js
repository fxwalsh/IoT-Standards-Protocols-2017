var express = require('express');
var router = express.Router();
var auth = require("../auth.js");
var config = require("../config.js");
var MongoClient = require('mongodb').MongoClient;
// Connection URL
var url = 'mongodb://'+config.dbUser+':'+config.dbPassword+'@ds121965.mlab.com:21965/sigfox_data';

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/* POST data */
router.post('/data', auth.basicAuthentication, function(req, res, next){
    console.log("POST" + JSON.stringify(req.body));

    req.checkBody("temp", "Did not recieve valid data").notEmpty().isInt();//YOU CAN MODIFY THIS TO SUIT YOUR OWN PURPOSES.
	req.checkBody("light", "Did not recieve valid data").notEmpty().isInt();
    var errors = req.validationErrors();
    if (errors) {
        res.send(errors);
        console.log(errors);
        return;
    } else {
        // Normal processing
        // Use connect method to connect to the Mongo db Server
	MongoClient.connect(url, function(err, db) {
		if(err) { return console.dir(err); }
  		console.log("Connected correctly to server");
  		var collection = db.collection('sensor_data');
  		collection.insertOne(
    		req.body, function(err, result) {
    			console.log("Inserted document into the sensor_data collection");
    			res.send("Post Successful");
  			});
  	
	});
    }


});

module.exports = router;
