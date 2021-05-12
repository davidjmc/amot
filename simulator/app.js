let express = require('express')

let app = express()
app.use(express.static('public'));


app.get('/data', (req, res) => {
    res.send('')
})

app.listen(3000)