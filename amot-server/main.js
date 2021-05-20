const net = require('net')

const self_port = 60010

// load classes
const Request = require('./classes/Request')
const Response = require('./classes/Response')
const ThingLoader = require('./classes/ThingLoader')
const Thing = require('./classes/Thing')



(async () => {
    let request = new Request('START\nThing:1')
    if (request.isStart()) {
        let thing = await ThingLoader.load(request.getThingId())
        console.log(typeof thing)
        // let response = Response.from(thing)
        // console.log(thing)
    }
    process.exit()
})()

// process.exit()

// const server = new net.Server()
// server.listen(self_port, '0.0.0.0', 5, () => {
//     console.log(`listening on ${self_port}`)
// })


// server.on('connection', socket => {
//     // console.log('connected')

//     socket.on('data', async data => {
//         let request = new Request(data.toString('ascii'))

//         if (request.isStart()) {
//             let response = await ThingLoader.load(request.getThingId)
//         }
//         console.log(response)


//         // let response = '0'
//         // switch(method) {
//         //     case 'START':
//         //         response = functions.startThing(headers)
//         //         if (!response) {
//         //             response = "ERROR"
//         //         }
//         //         socket.write(response)
//         //         break
//         //     case 'ADAPT':
//         //         response = functions.evolveThing(headers)
//         //         socket.write(response)
//         //         break
//         // }

//     })
// })
