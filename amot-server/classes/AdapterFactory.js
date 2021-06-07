const EvolutiveAdapter = require('./EvolutiveAdapter')

class AdapterFactory {
    static for(thing, type) {
        if (type == 'evolutive') {
            return new EvolutiveAdapter(thing)
        }
        return null
    }
}

module.exports = AdapterFactory