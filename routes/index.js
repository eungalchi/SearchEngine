var express = require('express');
var router = express.Router();

var mysql = require('mysql');
var config = require('../config/default.json');


var connection = mysql.createConnection({
  host:  config.Customer.dbConfig.host, //'52.78.221.205',
  user: config.Customer.dbConfig.user, //'quantec',
  password: config.Customer.dbConfig.password, //'!quant0330', // 본인 비번 쓰기!
  database: config.Customer.dbConfig.database, //'QTDB',
  port : config.Customer.dbConfig.port //3306
});


connection.connect;


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


module.exports = router;
