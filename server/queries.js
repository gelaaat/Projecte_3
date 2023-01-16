const { Pool } = require("pg");



const getData = async (sensor, id_arduino, interval='', columna_id) => {
    let pool = new Pool({
        user: process.env.PGUSER,
        host: process.env.PGHOST,
        database: process.env.PGDATABASE,
        password: process.env.PGPASSWORD,
        port: process.env.PGPORT,
        idle_in_transaction_session_timeout: 5000,
    });
    pool.setMaxListeners(Infinity)    
    try {
        console.log(`SELECT * FROM arduino${id_arduino}.${sensor}${interval}`);
        await pool.connect();
        const resposta = await pool.query(`SELECT * FROM arduino${id_arduino}.${sensor}${interval} ORDER BY ${columna_id} ASC`);
        let data = resposta.rows;

        pool.end().then(mes=>{
            console.log('sha desconnectat')
        });

        pool.on('end', () =>{
            console.log('he desconnectat')
        })
            
        return data;
        

    } catch (error) {
        console.log(error);
        pool.end()
    }
};

module.exports = { getData }