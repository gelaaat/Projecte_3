const { Pool, Client } = require("pg");
const path = require('path')

require('dotenv').config({
    path: path.resolve(__dirname, '../') + '/.env'
});

const pool = new Pool({
    user: process.env.PGUSER,
    host: process.env.PGHOST,
    database: process.env.PGDATABASE,
    password: process.env.PGPASSWORD,
    port: process.env.PGPORT,
    idle_in_transaction_session_timeout: 5000,
    max: 9999
});

const getData = async (sensor, id_arduino, interval='', columna_id) => {
    const client = new Client({
        user: process.env.PGUSER,
        host: process.env.PGHOST,
        database: process.env.PGDATABASE,
        password: process.env.PGPASSWORD,
        port: process.env.PGPORT,
    })
    
    try {
        await client.connect();
        const resposta = await pool.query(`SELECT * FROM arduino${id_arduino}.${sensor}${interval} ORDER BY ${columna_id} ASC`);
        let data = resposta.rows;

        client.end().catch(err => {
            console.error('No sha pogut desconnectar el client ', err)
        });

        return data;
        
    } catch (error) {
        console.log(error);
        client.end()
    }
};

module.exports = { getData }