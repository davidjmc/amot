const { query } = require('express');
const express = require('express');
const app = express();
const server = require('http').createServer(app);
const WebSocket = require('ws');
const wss = new WebSocket.Server({ server:server})
let conn = [];
let clients = {};

let socketId = () => {
    return new Date().getTime()
}
wss.on('connection', function connection(ws){
    console.log('Novo cliente conectado!')
    // console.log(ws);
    console.log(ws);
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
    // console.table(conn);
    // console.log(req.query.thing_id);
    // let ws;
    // for(let i = 0; i < conn.length; i++){
    //     ws = conn[i];
    //     ws.send(new ArrayBuffer(req.query)); 
    // }
    conn.forEach(ws => {
        ws.send(JSON.stringify(req.query));
    })
    // console.log(req.query);
    // console.log(conn);
});
server.listen(5000, () =>console.log('Escutando na porta : 5000'));