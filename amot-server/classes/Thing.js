const fs = require('fs')
const path = require('path')
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

    adl() {
        let adl = fs.readFileSync(path.join(__dirname, 'adl.template')).toString()
        let components_str = this.components.map(c => `'${c.type}': '${c.filename}'`).join(', ')
        let attachments_str = this.attachments.map(a => `'${a.from.type}':'${a.to.type}'`).join(',')
        let starter_str = `'${this.starter[0].type}'`
        let adapt_type = this.adaptability?.type ?? false ? `'${this.adaptability?.type}'` : 'None'
        let adapt_timeout = this.adaptability?.timeout ?? 'None'

        return adl
            .replace('__COMPONENTS__', components_str)
            .replace('__ATTACHMENTS__', attachments_str)
            .replace('__STARTER__', starter_str)
            .replace('__ADAPT_TYPE__', adapt_type)
            .replace('__ADAPT_TIMEOUT__', adapt_timeout)
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