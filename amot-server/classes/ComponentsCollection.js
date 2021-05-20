const Component = require('./Component')

class ComponentsCollection {
    constructor(components) {
        this.components = components
    }

    static async load(componentsIds) {
        let components = []
        for (let compId of componentsIds) {
            components.push(await Component.load(compId))
        }
        return new ComponentsCollection(components)
    }

    getByType(type) {
        return this.components.find(c => c.type == type)
    }
}

module.exports = ComponentsCollection