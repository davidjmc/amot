class Request {
    constructor(data) {
        [this.method, this.headers] = this.process(data)
    }

    process(data) {
        let data_lines = data.split('\n')
        let method = data_lines.shift()
        let headers = {}
        for (let line of data_lines) {
            if (line == '') {
                break
            }
            var [header, value] = line.split(':')
            headers[header] = value
        }
        return [method, headers]
    }

    isStart() {
        return this.method == 'START'
    }

    isAdapt() {
        return this.method == 'ADAPT'
    }

    getThingId() {
        return this.headers['Thing'] ?? false
    }
}

module.exports = Request