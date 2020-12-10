var net = require('net')
const fs = require('fs')

const self_port = 60010

var server = new net.Server()
server.listen(self_port, '0.0.0.0', 5, () => {
    console.log(`listening on ${self_port}`)
})

server.on('connection', socket => {
    console.log('connected')
    socket.on('data', data => {
        data = data.toString('ascii')
        var [thing_id, components] = data.split(':')
        components = components.split(',')

        console.log('thing: ' + thing_id)
        console.log('components: ' + components)

        let response = []

        // fs.readFile(`./components/${components[0]}.py`, 'ascii', (err, data) => {
        //     socket.write(String.fromCharCode(0x1c))
        // })

        components.forEach(comp => {
            console.log(comp)
            if (!fs.existsSync(`./components/${comp}.py`))
                return
            data = fs.readFileSync(`./components/${comp}.py`)
            response.push(comp + String.fromCharCode(0x1d) + data)
        })
        socket.write(
            response.join(String.fromCharCode(0x1c))
        )




        // fs.readFile('/Users/joe/test.txt', 'utf8' , (err, data) => {
        //   if (err) {
        //     console.error(err)
        //     return
        //   }
        //   console.log(data)
        // })

    })
})
