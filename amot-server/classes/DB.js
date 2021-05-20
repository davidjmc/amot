const { components, things } = require('../firebase')
const fs = require('fs')

class DB {
    static async getComponent(id) {
        let component = await components.doc(id).get()
        if (!component.exists) {
            throw `Component ${id} does not exist`
        }
        return component.data()
    }

    static async getThing(id) {
        let thing = await things.doc(id).get()
        if (!thing.exists) {
            throw `Thing ${id} does not exist`
        }
        return thing.data()
    }

    static async getFile(filename, path = 'components') {
        if (!fs.existsSync(`./library/${path}/${filename}.py`)) {
            throw `File ${filename}.py does not exists`
        }
        return fs.readFileSync(`./library/${path}/${filename}.py`)
    }
}

module.exports = DB
