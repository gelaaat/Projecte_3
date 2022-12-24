const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const db = require('./queries');

require('dotenv').config({
    path: path.resolve(__dirname, '../') + '/.env'
});




const PORT = process.env.PORT || 8000;
const PUBLIC_FOLDER = path.join(path.dirname(__dirname), 'public');

app.use(bodyParser.json());
app.use(
    bodyParser.urlencoded({
        extended: true,
    })
);

app.use(express.static(PUBLIC_FOLDER));

app.get('/temperatura/:id_arduino/:interval', (req, res) => {
    db.getData('temperatura', req.params.id_arduino, req.params.interval).then((temp) =>{
        res.send(temp);
        
    }).catch((err)=>{
        res.send(err);
    });
    
});

app.get('/humitat/:id_arduino/:interval', (req, res) => {
    db.getData('humitat', req.params.id_arduino, req.params.interval).then((hum) =>{
        console.log('he entrat');
        res.send(hum);
        
    }).catch((err)=>{
        res.send(err);
    });
    
});

app.listen(PORT, () => {
    console.log('Servidor iniciat al port: ' + PORT);
});