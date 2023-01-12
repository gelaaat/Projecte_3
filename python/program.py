import psycopg2

DADES_DB = {
    'host': 'localhost',
    'dbname': 'projecte',
    'user': 'user',
    'password': 'password',
    'port': '5432'
}

#Funciones que executarem durant el programa
def crear_taules():
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()

    #Creeem les estacions
    curs.execute("""CREATE SCHEMA IF NOT EXISTS arduino1 AUTHORIZATION "{usuari}\"""".format(usuari = DADES_DB['user']))
    curs.execute("""CREATE SCHEMA IF NOT EXISTS arduino2 AUTHORIZATION "{usuari}\"""".format(usuari = DADES_DB['user']))
    curs.execute("""CREATE SCHEMA IF NOT EXISTS arduino3 AUTHORIZATION "{usuari}\"""".format(usuari = DADES_DB['user']))

    #TEMPERATURA de la primera estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperatura1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperatura5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperaturadia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperaturames (temps CHARACTER(3) NOT NULL PRIMARY KEY, valor REAL)''')

    #HUMITAT de la primera estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitat1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitat5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitatdia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitatmes (temps CHARACTER(3) NOT NULL PRIMARY KEY, valor REAL)''')

    #TEMPERATURA segona estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperatura1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperatura5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperaturadia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperaturames (temps CHARACTER(3) NOT NULL PRIMARY KEY, valor REAL)''')

    #HUMITAT de la segona estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitat1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitat5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitatdia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitatmes (temps CHARACTER(3) NOT NULL PRIMARY KEY, valor REAL)''')

    #Pressio de la segona estacio
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressio1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressio5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressiodia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressiomes (temps CHARACTER(3) NOT NULL PRIMARY KEY, valor REAL)''')

    #Garatge
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino3.portagaratge (estat CHARACTER(7))''')

    def crear_Files():
        
        #Fem primer per les hores
        for i in range(0, 24, 1):
            curs.execute("INSERT INTO arduino1.temperatura1h(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.temperatura1h(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino1.humitat1h(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.humitat1h(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.pressio1h(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
        
        #Fem per els 5min
        for i in range(5, 65, 5):
            curs.execute("INSERT INTO arduino1.temperatura5min(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.temperatura5min(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino1.humitat5min(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.humitat5min(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.pressio5min(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
        
        #Fem pels dies del mes
        for i in range(1, 31):
            curs.execute("INSERT INTO arduino1.temperaturadia(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.temperaturadia(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino1.humitatdia(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.humitatdia(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.pressiodia(temps) VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
        
        #Fem els mesos
        mesos = ['Jan', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec']
        for i in mesos:
            curs.execute("INSERT INTO arduino1.temperaturames(temps) VALUES ('{temps}') ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.temperaturames(temps) VALUES ('{temps}') ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino1.humitatmes(temps) VALUES ('{temps}') ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.humitatmes(temps) VALUES ('{temps}') ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.pressiomes(temps) VALUES ('{temps}') ON CONFLICT(temps) DO NOTHING".format(temps=i))
            
    crear_Files()

    conexion.commit()
    conexion.close()

def insertar_dada(arduino, sensor, interval, nom_columna, nom_columna_variable, fila, dada):
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()
    print("UPDATE {arduino}.{sensor}{interval} SET {nom_columna_variable} = {dada} WHERE {nom_columna} = {fila}".format(arduino = arduino, sensor = sensor, interval = interval, nom_columna = nom_columna, nom_columna_variable = nom_columna_variable, fila = fila, dada = dada))
    curs.execute("UPDATE {arduino}.{sensor}{interval} SET {nom_columna_variable} = {dada} WHERE {nom_columna} = {fila}".format(arduino = arduino, sensor = sensor, interval = interval, nom_columna = nom_columna, nom_columna_variable = nom_columna_variable, fila = fila, dada = dada))
    conexion.commit()
    conexion.close()

def garatge(estat = 'oberta'):
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()
    curs.execute("UPDATE arduino3.portagaratge SET estat = {estat}".format(estat = estat))
    conexion.close()

def recuperar_dades(arduino, sensor, interval):
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()
    curs.execute("SELECT * FROM {arduino}.{sensor}{interval} ORDER BY temps ASC".format(arduino = arduino, sensor = sensor, interval = interval))
    print(curs.fetchall())
    conexion.close()

def canviar_dades():
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()

    #TEMPERATURA de la primera estació
    curs.execute('ALTER TABLE arduino1.temperatura5min ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino1.temperatura1h ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino1.temperaturadia ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino1.temperaturames ALTER COLUMN valor SET DATA TYPE REAL')

    #HUMITAT de la primera estació
    curs.execute('ALTER TABLE arduino1.humitat5min ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino1.humitat1h ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino1.humitatdia ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino1.humitatmes ALTER COLUMN valor SET DATA TYPE REAL')

    #TEMPERATURA segona estació
    curs.execute('ALTER TABLE arduino2.temperatura5min ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino2.temperatura1h ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino2.temperaturadia ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino2.temperaturames ALTER COLUMN valor SET DATA TYPE REAL')

    #HUMITAT de la segona estació
    curs.execute('ALTER TABLE arduino2.humitat5min ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino2.humitat1h ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino2.humitatdia ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino2.humitatmes ALTER COLUMN valor SET DATA TYPE REAL')

    #Pressio de la segona estacio
    curs.execute('ALTER TABLE arduino2.pressio5min ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino2.pressio1h ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino2.pressiodia ALTER COLUMN valor SET DATA TYPE REAL')
    curs.execute('ALTER TABLE arduino2.pressiomes ALTER COLUMN valor SET DATA TYPE REAL')

    conexion.commit()
    conexion.close()

crear_taules()

canviar_dades()

insertar_dada('arduino1', 'temperatura', '1h', 'temps', 'valor', 21, 24)

recuperar_dades('arduino1', 'temperatura', '1h')
