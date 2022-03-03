var http = require('http')
var querystring = require('querystring');
var express = require('express')
var fs = require('fs')
var app = express()

var bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

app.listen(8001, function() {
  console.log('start')
})
app.post('/cmd', function(req, res) {
  console.log('收到post请求了')
  var query = req.query
  console.log(query)
  console.log(query.cmd)
  var shell = CmdRunner(query.cmd)
  res.send(shell);
  res.end();
})

app.post('/asyncCmd', function(req, res) {
  console.log('收到post请求了')
  var query = req.query
  console.log(query)
  console.log(query.cmd)
  ret = {"code":200 , "data":true}
  res.send(ret);
  res.end();
  CmdAsync(query.cmd)
})

app.get('/', function(req, res) {
  console.log('收到get请求了')
  res.send(responser);
  res.end();
})

app.get('/api/kafka/info', function(req, res) {
    console.log('收到get请求了')
    res.send(kafkaer);
    res.end();
  })

  app.get('/api/test/minerSn/read', function(req, res) {
    console.log('收到get请求了')
    res.send(sn);
    res.end();
  })
  
function getSn(){
    var data =fs.readFileSync("/sn");
    var tmp = data.toString();
    var ret = tmp.split("\n");

    return ret[0];
}

var responser = {"code":200 , "status":"online"};
var kafkaer = [
    {
    "code": "S0401001",
    "val": "2022-02-14 09:16:49.133419"
    },
    {
    "code": "S0401002",
    "val": 1
    },
    {
    "code": "S0401003",
    "val": "49.1"
    },
    {
    "code": "S0401004",
    "val": "192.168.2.178"
    },
    {
    "code": "S0401005",
    "val": "2.5"
    },
    {
    "code": "S0401006",
    "val": "59670"
    },
    {
    "code": "S0401007",
    "val": "17073"
    },
    {
    "code": "S0401008",
    "val": "3886.0"
    },
    {
    "code": "S0401009",
    "val": "696.0"
    },
    {
    "code": "S040100A",
    "val": 0.35
    },
    {
    "code": "S040100B",
    "val": "error"
    },
    {
    "code": "S040100C",
    "val": "error"
    },
    {
    "code": "S040100D",
    "val": "{\"hci0\": \"E4:5F:01:37:99:A9\"}"
    },
    {
    "code": "S040100E",
    "val": "21.0"
    },
    {
    "code": "S040100F",
    "val": "21.0"
    },
    {
    "code": "S0401010",
    "val": "125.118.222.169"
    }
    ]
var sn = {
    "minerSn": getSn(),
    "raw": [
    "0x01",
    "0x00",
    "0x00",
    "0x08",
    "0x06",
    "0x08",
    "0x00",
    "0x00",
    "0x00",
    "0x07",
    "0x05",
    "0x06",
    "0x03",
    "0x05"
    ]
    }
function setResponse(code,data){
  responser = {"code":code , "status":data};
}

function CmdRunner(cmd) {
  var exec = require('child_process').execSync;
  var str = exec(cmd);
  return (str.toString("utf8").trim());
}

const CmdAsync = async (cmd) => {
  var exec = require('child_process').execSync;
  var str = exec(cmd);
  return (str.toString("utf8").trim());
}
module.exports = {
  setResponse
  }