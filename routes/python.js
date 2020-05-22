var express = require('express');
var router = express.Router();

var spawn = require("child_process").spawn;

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



router.post('/py', function(req, res){

    var process1 = spawn('python', ["search_engine/main.py", req.body.text]);
    console.log(req.body.text)
  
    process1.stdout.on('data', function(data){
  
      //res.send(data.toString());
  
      console.log(data);
      console.log(data.toString() + "번 시나리오");
      
      var exnum = data.toString();
      var exadress = "search_engine/ex" + exnum;
      exadress = exadress.trim();
      
      console.log(exadress);
      console.log(req.body.text)
  
      var process2 = spawn('python', [exadress + ".py", req.body.text]);
  
      process2.stdout.on('data', function(data){
  
        console.log(data.toString("utf-8"));
        var sql = data.toString();
  
        connection.query(sql, function (error, results, fields) {

          try {
            console.log('The result is: ', results);
            res.json(results);
          } catch (error) {
            console.error(error);
            //throw error!
          } finally {
            console.log("어쨌든!")
            //res.send(results); 오히려 정상적인 값에서 오류남! send라서!
          }
  /*
          if (error) {
              console.error(error);
              throw error; //만약 시나리오 판정이 틀리다면 그 다음 확률이 높은 시나리오로 갈 수 있는 예외처리가 필요함! 그래도 틀리면 더 정확한 검색 요구하기,,,,
          }else {
              console.log('The result is: ', results);
              res.json(results);
          }
          */
      }) 
        //res.send(data.toString("utf-8"));
      })
  
      process2.stderr.on('data', function(data){
  
        console.log("error!" + data)
    
      })
  
    });
    process1.stderr.on('data', function(data){
  
      console.log("error!" + data)
  
    })
  });
  
  module.exports = router;
  