const fs = require('fs')
const path = require('path')
const DB = require('./DB')
const ComponentsCollection = require('./ComponentsCollection')

class Thing {
    constructor(id, components, attachments, starter, adaptability, trialMode, vars) {
        this.id           = id
        this.adaptability = adaptability
        this.attachments  = attachments
        this.components   = components
        this.starter      = starter
        this.trialMode    = trialMode
        this.rolledBack   = false
        this.vars         = vars
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

    // possible data types: object
    appVars() {
        let vars = ''
        for (let v in this.vars) {
            let data = this.vars[v]
            if (typeof data == 'string') {
                data = `'${data}'`
            }
            vars += `${v} = ${data}`
        }
        return vars
    }

    // async getRolledBackVersions() {
    //     if (this.rolledBack === false) {
    //         this.loadRolledBack()
    //     }
    // }

    // async loadRolledBack() {
    //     await DB.getThingRolledBack(this.id)
    // }

    // save thing data to an internal backup collection
    // set thing to "trial" version
    async backup() {
        await DB.backupThing(this.id)
    }

    async setTrial() {
        this.trialMode = true
        await this.update()
    }

    isInTrial() {
        return this.trialMode
    }

    // remove the backup version and mark the current as "stable"
    async commit() {
        this.trialMode = false
        await this.update()
    }

    // return thing data to its backup data and mark current components as "unstable" (ignored?)
    async rollback() {
        await DB.rollbackThing(this.id)
    }

    async update() {
        await DB.saveThing(this)
    }

    async apply(adaptation) {
        for (let component of adaptation.componentsToAdd) {
            this.components.replaceByName(component)
        }
        for (let appVar in adaptation.appVars) {
            this.vars[appVar] = adaptation.appVars[appVar]
        }
        await this.update()

        adaptation.adl = this.adl()
        adaptation.appVars = this.appVars()
    }

    static async load(id) {
        let thing = await DB.getThing(id)
        let collection = await ComponentsCollection.load(thing.components)
        let starter = thing.starter.map(s => collection.getByType(s))
        let attachments = thing.attachments.map(att => ({
            'from': collection.getByType(att.from),
            'to': collection.getByType(att.to)
        }))
        let obj = new Thing(
            id,
            collection,
            attachments,
            starter,
            thing.adaptability,
            thing.trialMode,
            thing.vars
        )
        return obj
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
//     let t = await Thing.load('1')
//     // await t.rollback()
//     // await t.loadRolledBack()
//     // console.dir(t.rolledBack, {depth: 3})
//     // console.log(t.components)
//     // for (let c of t.components.components) {
//     //     await c.loadVersions()
//     // }
//     // t.components.map(async c => {
//     //     console.log(await c.loadVersions())
//     // })
//     // console.dir(t, {depth: 3})
//     // await t.backup()
//     // await t.setTrial()
//     // await t.rollback()

//     process.exit()
// })()

module.exports = Thing