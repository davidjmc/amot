const fs = require('fs')

const TICKS_PER_HOUR = 60

let valve = 1

// durations in minutes
let DURATION = {
    'toilet': 1,
    'shower': 10,
    'toothbrush': 5,
    'dishes': 15,
    'clothes': 90,
    'eat': 1,
    'leak': 24 * 60,
    'water': 60
}

let FAUCET_AFTER_TOILET_DURATION = 1

// type: consumption (liters / minute)
let CONSUMPTIONS = {
    'toilet': 6,
    'faucet': 4,
    'shower': 6,
    'toothbrush': 1, // faucet 25% open
    'dishes': 2, // faucet half open
    'clothes': 150 / 90,
    'eat': 4, // faucet
    'leak': 0.1,
    'water': -10,
}


// updating durations and consumptions based on TICKS_PER_HOUR
// - duration is now measured in intervals of (60 / TICKS_PER_HOUR) minutes
// - consumption is now measured in liters per / interval duration
for (event_type of Object.keys(DURATION)) {
    DURATION[event_type] = DURATION[event_type] / 60 * TICKS_PER_HOUR
}
for (event_type of Object.keys(CONSUMPTIONS)) {
    CONSUMPTIONS[event_type] = CONSUMPTIONS[event_type] * (60 / TICKS_PER_HOUR)
}

let event = (desc, start, end, duration) => {
    duration = duration ?? DURATION[desc]
    // https://gist.github.com/gordonbrander/2230317
    return {
        'id': '_' + Math.random().toString(36).substr(2, 9),
        'desc': desc,
        'start': start * TICKS_PER_HOUR,
        'end': end * TICKS_PER_HOUR,
        'duration': duration,
        'consumption': CONSUMPTIONS[desc] + (desc == 'toilet' ? CONSUMPTIONS['faucet'] * FAUCET_AFTER_TOILET_DURATION : 0)
    }
}

let faucet = (start, end, duration) => {
    // return ['faucet', start * TICKS_PER_HOUR, end * TICKS_PER_HOUR, duration]
    // return {
    //     'desc': 'faucet',
    //     'start': start * TICKS_PER_HOUR,
    //     'end': end * TICKS_PER_HOUR,
    //     'duration': duration,
    //     'consumption': CONSUMPTIONS['faucet']
    // }
    return event('faucet', start, end, duration)
}

let toilet = (start, end) => {
    return [
        event('toilet', start, end)
        // faucet(start, end, 1)
    ]
}

let shower = (start, end, duration) => {
    return event('shower', start, end, duration)
}

let toothbrush = (start, end, duration) => {
    return event('toothbrush', start, end, duration)
}

let dishes = (start, end, duration) => {
    return event('dishes', start, end, duration)
}

let clothes = (start, end, duration) => {
    return event('clothes', start, end, duration)
}

let eat = (start, end) => {
    return event('eat', start, end)
}

let leak = (start, end) => {
    return event('leak', start, end)
}


let faucet_after_toilet_duration = 1

let habits = [
    [
        toilet(6, 12),
        toilet(6, 12),
        toilet(12, 18),
        toilet(12, 18),
        toilet(18, 23),

        shower(6, 12),
        shower(12, 20),
        shower(20, 23),

        eat(6, 9),
        eat(9, 12),
        eat(12, 15),
        eat(15, 18),
        eat(18, 22),

        // leak(6, 22),

        toothbrush(6, 12),
        toothbrush(12, 20),
        toothbrush(20, 23),

        faucet(6, 12, 10),
        faucet(12, 17, 10),
        faucet(18, 22, 10),

        dishes(6, 12),
        dishes(12, 17),
        dishes(18, 22),

        // clothes(6, 12),
    ],
    ...Array(5).fill([
        toilet(6, 7),
        shower(6, 7),
        eat(6, 7),
        toothbrush(6, 7),
        eat(18, 20),
        eat(20, 22),
        dishes(18, 22),
        toilet(18, 23),
        shower(18, 19)
    ]),
    [
        toilet(6, 12),
        toilet(6, 12),
        toilet(12, 18),
        toilet(12, 18),
        toilet(18, 23),
        toilet(18, 23),

        shower(6, 12),
        shower(12, 20),
        shower(20, 23),

        eat(6, 9),
        eat(9, 12),
        eat(12, 15),
        eat(15, 18),
        eat(18, 22),

        toothbrush(6, 12),
        toothbrush(12, 20),
        toothbrush(20, 23),

        faucet(6, 12, 10),
        faucet(12, 17, 10),
        faucet(18, 22, 10),

        dishes(6, 12),
        dishes(12, 17),
        dishes(18, 22),

        clothes(6, 12),
    ],
]

// habits = habits.map(day => {
//     return day.sort((e1, e2) => e1.start - e2.start)
// })


let water_level = 1000

let day = 0
let time = 60 * 5

let day_events = habits[day]
let active_events = []

// console.debug(day_events)

let parseTime = () => {
    let d = new Date(time * (60 / TICKS_PER_HOUR) * 60 * 1000)
    d.setTime(d.getTime() + d.getTimezoneOffset()*60*1000)
    let h = `0${d.getHours()}`.substr(-2)
    let m = `0${d.getMinutes()}`.substr(-2)
    return `${day} / ${h}:${m}`
}

let times_str = []
let levels_str = []

let tick = () => {
    time++
    if (time == 23 * 60 + 30) {
        time = 5 * 60
        day =  (day + 1) % 7
        day_events = habits[day]
    }
    // console.log(time)
    let old_level = water_level

    // update level based on active events
    let ended_events = []
    for (event of active_events) {
        water_level -= event.consumption * Math.min(event.duration, time - (event.last_tick ?? event.started_at)) * valve
        event.last_tick = time
        if (time - event.started_at >= event.duration) {
            ended_events.push(event)
        }
    }
    for (event of ended_events) {
        let evt_i = active_events.findIndex(e => e.id == event.id)
        active_events = [...active_events.slice(0, evt_i), ...active_events.slice(evt_i + 1)]
        console.log(parseTime(), 'ended...', event)
    }

    // select events to start
    let started_events = []
    let possible_events = day_events.filter(e => time >= e.start)

    for (event of possible_events) {
        if (active_events.length == 0 && started_events.length == 0 && (event.end - time) < (event.end - event.start) * Math.random()) {
            started_events.push(event)
        }
    }

    // add events to active_events
    for (event of started_events) {
        event.started_at = time
        active_events.push(event)
        let evt_i = day_events.findIndex(e => e.id == event.id)
        day_events = [...day_events.slice(0, evt_i), ...day_events.slice(evt_i + 1)]
        console.log(parseTime(), 'starting...', event)
    }

    if (old_level != water_level) {
        // console.log(parseTime(), 'water: ', old_level, water_level)
    }
    console.log(parseTime(), water_level)
    times_str.push(`"${parseTime()}"`)
    levels_str.push(water_level)
}

// for (i = 0; i < 23 * TICKS_PER_HOUR; i++) {
//     tick()
// }
setInterval(() => {
    tick()
}, 100)

fs.unlink('public/labels.json', () => {
    fs.writeFile('public/labels.json', `[${times_str.join(',')}]`, () => {})
})
fs.unlink('public/levels.json', () => {
    fs.writeFile('public/levels.json', `[${levels_str.join(',')}]`, () => {})
})