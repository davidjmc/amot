const fs = require('fs')

const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')

const adapter = new FileSync('db.json')
const db = low(adapter)


let startThing = (headers, socket) => {
    if (!headers['Thing']) {
        return false
    }
    let thing_id = headers['Thing']
    let thing = db.get('things').find({"id": thing_id}).value()

    if (thing.components.length && !thing.components[0].type) {
        thing.components = thing.components.map(c => db.get('components').find({'id': c}).value())
    }
    if (thing.attachments.length && !thing.attachments[0].from.type) {
        thing.attachments = thing.attachments.map(a => {
            return {
                "from": db.get('components').find({'id': a.from}).value(),
                "to": db.get('components').find({'id': a.to}).value()
            }
        })
    }
    if (thing.starter.length && !thing.starter[0].type) {
        thing.starter = thing.starter.map(c => db.get('components').find({'id': c}).value())
    }

    let adl_components = thing.components.map(c => `'${c.type}': '${c.file}'`)
    console.log(adl_components)
    let adl_attachments = thing.attachments.map(a => `'${a.from.type}': '${a.to.type}'`)
    console.log(adl_attachments)
    let adl_starters = thing.starter.map(c => `'${c.type}'`)

    adl = `
Components = {
    ${adl_components.join(",\n    ")}
}

Attachments = {
    ${adl_attachments.join(",\n    ")}
}

Starter = {
    ${adl_starters.join(",\n    ")}
}

Adaptability = {
    'type': ${thing.adaptability ?? 'None'}
}
`

    let response = ['adl' + String.fromCharCode(0x1d) + adl]

    // fs.readFile(`./components/${components[0]}.py`, 'ascii', (err, data) => {
    //     socket.write(String.fromCharCode(0x1c))
    // })

    thing.components.forEach(comp => {
        console.log(comp)
        if (!fs.existsSync(`./components/${comp.file}.py`))
            return
        let data = fs.readFileSync(`./components/${comp.file}.py`)
        response.push('components/' + comp.file + String.fromCharCode(0x1d) + data);

        (''+data).split('\n').forEach(loc => {
            let _import = null
            let dependency = ''

            _import = loc.match(/import (.*)/)
            // console.log(_import)
            if (_import) {
                dependency = _import[1]
            }

            _import = loc.match(/from (?:.*)? import (.*)/)
            if (_import) {
                dependency = _import[1]
            }
            if (dependency) {
                console.log('dep: ' + dependency)
            }

            if (!fs.existsSync(`./classes/${dependency}.py`))
                return

            let data = fs.readFileSync(`./classes/${dependency}.py`)
            response.push(dependency + String.fromCharCode(0x1d) + data);
        })
    })
    return response.join(String.fromCharCode(0x1c))


}

module.exports = {
    startThing
}