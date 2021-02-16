const fs = require('fs')

const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')

const adapter = new FileSync('db.json')
const db = low(adapter)

let loadThing = thing_id => {
    let thing = db.get('things').find({"id": thing_id}).value()

    if (true || !thing._components?.[0]?.type) {
        thing._components = thing.components.map(c => db.get('components').find({'id': c}).value())
    }
    if (true || !thing._attachments?.[0]?.type) {
        thing._attachments = thing.attachments.map(a => {
            return {
                "from": thing._components.find(c => c.type == a.from),
                "to": thing._components.find(c => c.type == a.to)
            }
        })
    }
    if (true || !thing._starter?.[0]?.length) {
        thing._starter = thing.starter.map(s => thing._components.find(c => c.type == s))
    }
    return thing
}

readComponents = components => {
    let response = []
    components.forEach(comp => {
        // console.log(comp)
        if (!fs.existsSync(`./components/${comp.file}.py`))
            return
        let data = fs.readFileSync(`./components/${comp.file}.py`)
        response.push('components/' + comp.name + String.fromCharCode(0x1d) + data);

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
    return response
}

let startThing = (headers) => {
    if (!headers['Thing']) {
        return '0'
    }
    let thing_id = headers['Thing']
    let thing = loadThing(thing_id)

    let adl_components = thing._components.map(c => `'${c.type}': '${c.file}'`)
    // console.log(adl_components)
    let adl_attachments = thing._attachments.map(a => `'${a.from.type}': '${a.to.type}'`)
    // console.log(adl_attachments)
    let adl_starters = thing._starter.map(c => `'${c.type}'`)
    let adaptability = `'${thing.adaptability?.type ?? 'None'}'`

    /*
     * TODO
     * - Erase 'current' version
     */

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
    'type': ${thing.adaptability?.type ?? false ? `'${thing.adaptability.type}'` : 'None'},
    'timeout': ${thing.adaptability?.timeout ?? 'None'}
}
`

    let response = ['adl' + String.fromCharCode(0x1d) + adl]

    // fs.readFile(`./components/${components[0]}.py`, 'ascii', (err, data) => {
    //     socket.write(String.fromCharCode(0x1c))
    // })

    response.push(...readComponents(thing._components))
    return response.join(String.fromCharCode(0x1c))
}

let evolveThing = (headers) => {
    if (!headers['Thing']) {
        return false
    }
    let thing_id = headers['Thing']
    let thing = loadThing(thing_id)

    /*
     * TODO
     * - Commit 'current' version (check if there is any "current version" and update the "original" versions)
     */

    let newVersions = component => {
        return db.get('components').filter(comp => {
            return comp.name == component.name && comp.version > component.version
        }).sort((c1, c2) => c1.version > c2.version).value()
    }

    let new_components = thing._components.filter(comp => {
        return newVersions(comp).length > 0
    }).map(comp => {
        return newVersions(comp)[0]
    })
    let files = readComponents(new_components).join(String.fromCharCode(0x1c))

    // TODO
    /*
     * - Update database entry for the thing with the 'current version'
     */

    let response = ['']
    return response + String.fromCharCode(0x1e) + files
}

module.exports = {
    startThing,
    evolveThing
}