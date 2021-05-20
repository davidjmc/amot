class ThingLoader {
    static async load(thingId) {
        if (thingId === false) {
            // thing cant be loaded
            return new Response('0')
        }
        return await Thing.load(thingId)
    }
}

module.exports = ThingLoader