const EvolutiveAdapter = require('./EvolutiveAdapter')
const ParametricAdapter = require('./ParametricAdapter')

class AdapterFactory {
    static for(thing, type) {
        if (type == 'evolutive') {
            return new EvolutiveAdapter(thing)
        }
        if (type == 'parametric') {
            return new ParametricAdapter(thing)
        }
        return null
    }
}

module.exports = AdapterFactory