const mongoose = require('mongoose');
const thingSchema = new mongoose.Schema({
    thing_id:{
        type:String,
        required:true,
    },
    water_level:{
        type:Number,
        required:true,
    },
})
const Thing = mongoose.model('THINGS', thingSchema);

module.exports = Thing;