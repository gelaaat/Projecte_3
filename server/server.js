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
    db.getData('temperatura', req.params.id_arduino, req.params.interval, 'temps').then((temp) =>{
        res.send(temp);
        
    }).catch((err)=>{
        res.send(err);
    });
    
});

app.get('/humitat/:id_arduino/:interval', (req, res) => {
    db.getData('humitat', req.params.id_arduino, req.params.interval, 'temps').then((hum) =>{
        res.send(hum);
        
    }).catch(err =>{
        res.send(err);
    });
    
});

app.get('/pressio/:id_arduino/:interval', (req, res) => {
    db.getData('pressio', req.params.id_arduino, req.params.interval, 'temps').then((press) =>{
        res.send(press);
        
    }).catch(err =>{
        res.send(err);
    });
    
});

app.get('/portagaratge/:id_arduino', (req, res) => {
    db.getData('portagaratge', req.params.id_arduino, '','estat').then(data => {
        res.send(data);
    }).catch(error => {
        res.send(error);
    })
});

app.listen(PORT, () => {
    console.log('Servidor iniciat al port: ' + PORT);
});