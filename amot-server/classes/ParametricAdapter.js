const Adapter = require('./Adapter')
const Adaptation = require('./Adaptation')

class ParametricAdapter extends Adapter {
    constructor(thing) {
        super(thing)
    }

    async adaptFor(request) {
        let variables = await this.monitor(request)

        let changes = await this.analyzer(variables)

        let adaptation = this.planner(changes)
        return adaptation
    }

    // return variables used in condition from request
    // TODO - be generic
    async monitor(request) {
        return {
            temperature: parseInt(request.headers['temperature'])
        }
    }

    // return the "command" for the correct condition based on variables
    // TODO - be generic
    async analyzer(variables) {
        let temperature = variables.temperature
        console.log(temperature)
        if (temperature > 70) {
            return {
                sleep_time: 5
            }
        } else if (temperature > 50) {
            return {
                sleep_time: 3
            }
        } else if (temperature > 0) {
            return {
                sleep_time: 1
            }
        }
    }

    planner(changes) {
        let adaptation = new Adaptation()
        adaptation.appVars = changes

        return adaptation
    }
}

module.exports = ParametricAdapter