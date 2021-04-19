const { query } = require('express');
const express = require('express');
const app = express();
const server = require('http').createServer(app);
const WebSocket = require('ws');
const mongoose = require('mongoose');
const wss = new WebSocket.Server({ server:server})
const db = 'mongodb+srv://barroz:6969@cluster0.vb8kd.mongodb.net/Amot?retryWrites=true&w=majority';
const Thing = require('./models/thingSchema.js');
let conn = [];
let clients = {};
let socketId = () => {
    return new Date().getTime()
}

mongoose.connect(db, {
    useNewUrlParser:true,
    useCreateIndex:true,
    useUnifiedTopology:true,
    useFindAndModify:false,
}).then(() =>{
    console.log('Connection Success')
}).catch((err) => console.log('Fail :' + err));
 
app.use('/css',express.static(__dirname + '/css'));
app.use('/images',express.static(__dirname + '/images'));
app.use('/js',express.static(__dirname + '/js'));

wss.on('connection', function connection(ws){
    console.log('Novo cliente conectado!')
    // console.log(ws);
    conn.push(ws);

    let id = socketId()
    clients[id] = ws

    // ws.on('close', ((id) => {
    //     () => { delete clients[id] }
    // })(id))
    // ws.close();
    // ws.unique_id = id
    // ws.on('close', (event) => {
    //     delete clients[this.unique_id]
    // })
    // ws.onclose.
    // ws.send('Bem vindo!!');
    // ws.on('message', function incoming(message){
    //     console.log('received: %s', message);
        // ws.send('Valor do nível da água : ' + message);
    // })
})
// setInterval(()=> {
//     console.log(Object.keys(clients));
// },1000);
app.get('/waterlevel', function(req, res){
    res.sendStatus(200);
    console.log(req.query);
    let arr = req.query;
    // console.log(req.query.thing_id[0], req.query.water_level[0]);
    // console.log(arr.thing_id[0]);
    for(let i = 0; i < arr.thing_id.length; i++){
        Thing.find({thing_id:req.query.thing_id[i]}, function(err, docs){
            if(docs.length == 0){
                let storeThing = new Thing({
                    thing_id: req.query.thing_id[i],
                    water_level: req.query.water_level[i]
                });
                storeThing.save();
            }else{
                Thing.findOne({thing_id:req.query.thing_id[i]}, function (err, doc){
                    doc.water_level = req.query.water_level[i];
                    doc.save();
                });
            }
        });
    }
    setTimeout(()=> {
        Thing.find({}, function(err, things){
            conn.forEach(ws => {
                ws.send(JSON.stringify(things));
            })
        });
    },100);
    // console.log(req.query.thing_id);
    // console.table(conn);
    // console.log(req.query.thing_id);
    // let ws;
    // for(let i = 0; i < conn.length; i++){
    //     ws = conn[i];
    //     ws.send(new ArrayBuffer(req.query)); 
    // }

    // console.log(req.query);
    // console.log(conn);
});
app.get('/', function(req, res){
    res.sendFile(__dirname + '/dashboard.html')
});
server.listen(5100, () =>console.log('Escutando na porta : 5100'));