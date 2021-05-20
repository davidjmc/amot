class Response {
    constructor(response = '') {
        this.data = response
    }

    from(some) {
        if (some instanceof Thing) {
            return this.fromThing(some)
        }
    }

    loadFromThing(thing) {
        let response = new Response()
        // response.addFile('adl', thing.adl())
        // thing.components.map(component => {
        //     response.addFile(component.filename, component.file)
        // })
        return response
    }
}