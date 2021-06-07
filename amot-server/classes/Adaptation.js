class Adaptation {
    constructor(componentsToAdd = [], componentsToRemove = [], config = []) {
        this.adl = ''
        this.componentsToAdd = componentsToAdd
        this.componentsToRemove = componentsToRemove
        this.config = config
        // this.newAdl = ''
    }

    merge(adaptation) {
        // TODO
    }

    hasChanges() {
        return this.componentsToAdd.length > 0 || this.componentsToRemove.length > 0
    }
}

module.exports = Adaptation