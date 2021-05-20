const DB = require('./DB')
const ComponentsCollection = require('./ComponentsCollection')

class Thing {
    constructor(id, components, attachments, starter, adaptability) {
        this.id           = id
        this.adaptability = adaptability
        this.attachments  = attachments
        this.components   = components
        this.starter      = starter
    }

    static async load(id) {
        let thing = await DB.getThing(id)
        let collection = await ComponentsCollection.load(thing.components)
        let starter = thing.starter.map(s => collection.getByType(s))
        let attachments = thing.attachments.map(att => ({
            'from': collection.getByType(att.from),
            'to': collection.getByType(att.to)
        }))
        return new Thing(
            id,
            collection,
            attachments,
            starter,
            thing.adaptability
        )
        // return new Component(
        //     id,
        //     component.name,
        //     component.version,
        //     component.type,
        //     component.file
        // )
    }
}

// (async () => {
//     console.dir(await Thing.load('1'), {depth: 3})
//     process.exit()
// })()

module.exports = Thing