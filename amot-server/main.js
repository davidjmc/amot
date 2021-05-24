const net = require('net')

const self_port = 60010

// load classes
const Request = require('./classes/Request')
const Response = require('./classes/Response')
const ThingLoader = require('./classes/ThingLoader')


;

// (async () => {
//     let request = new Request('START\nThing:1')
//     if (request.isStart()) {
//         let thing = await ThingLoader.load(request.getThingId())
//         // console.log(thing.adl())
//         let response = Response.fromThing(thing)
//         console.log(response.toString())
//     }
//     process.exit()
// })()

// process.exit()

const server = new net.Server()
server.listen(self_port, '0.0.0.0', 5, () => {
    console.log(`listening on ${self_port}`)
})


server.on('connection', socket => {
    console.log('connected')

    socket.on('data', async data => {
        console.log(`data received: ${data}`)
        let request = new Request(data.toString('ascii'))

        console.log(`loading thing ${request.getThingId()}`)
        let thing = await ThingLoader.load(request.getThingId())

        if (request.isStart()) {
            console.log(`thing loaded, preparing response`)
            let response = Response.fromThing(thing)
            socket.write(response.toString())
            socket.destroy()
            console.log(`response sent`)
        } else if (request.isAdapt()) {
            // MAPE-K
            // let response = mapek_manager(thing, request)
        }

    })
})
