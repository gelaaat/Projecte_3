const { Pool } = require("pg");



const getData = async (sensor, id_arduino, interval='') => {
    try {
        const pool = new Pool({
            user: process.env.PGUSER,
            host: process.env.PGHOST,
            database: process.env.PGDATABASE,
            password: process.env.PGPASSWORD,
            port: process.env.PGPORT,
        });

        console.log(`SELECT * FROM arduino${id_arduino}.${sensor}${interval}`);
        await pool.connect();
        const resposta = await pool.query(`SELECT * FROM arduino${id_arduino}.${sensor}${interval}`);
        let data = resposta.rows; 
        return data;

    } catch (error) {
        console.log(error);
    }
};
/*
const portaGaratge = async () => {

};  
*/
module.exports = { getData }