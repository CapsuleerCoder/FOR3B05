var mongo = require('mongodb');
var MongoClient = require('mongodb').MongoClient;
var url = 'mongodb://127.0.0.1:27017/awesomeDB';

MongoClient.connect(url, {useUnifiedTopology: true}, function(err, db) {
  if (err) throw err;
  var dbo = db.db("awesomeDB");
  var myobj = { name: "Company Inc", address: "Highway 37" };
  dbo.collection("customers").insertOne(myobj, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
});

