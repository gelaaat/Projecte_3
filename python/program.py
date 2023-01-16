import psycopg2

#Guardarem les credencials de la nostre base de dades en un diccionari
DADES_DB = {
    'host': 'localhost',
    'dbname': 'projecte',
    'user': 'user',
    'password': 'password1234',
    'port': '5432'
}


#Funcions que executarem durant el programa de la base de dades
def crear_taules():
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()

    #Creeem les estacions
    curs.execute("""CREATE SCHEMA IF NOT EXISTS arduino1 AUTHORIZATION "{usuari}\"""".format(usuari = DADES_DB['user']))
    curs.execute("""CREATE SCHEMA IF NOT EXISTS arduino2 AUTHORIZATION "{usuari}\"""".format(usuari = DADES_DB['user']))
    curs.execute("""CREATE SCHEMA IF NOT EXISTS arduino3 AUTHORIZATION "{usuari}\"""".format(usuari = DADES_DB['user']))

    #TEMPERATURA de la primera estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperatura1min (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperatura1h (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperatura5min (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperaturadia (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperaturames (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')

    #HUMITAT de la primera estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitat1min (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitat1h (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitat5min (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitatdia (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitatmes (temps INT NOT NULL PRIMARY KEY, valor INT NOT NULL)''')

    #TEMPERATURA segona estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperatura1min (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperatura1h (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperatura5min (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperaturadia (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperaturames (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')

    #HUMITAT de la segona estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitat1min (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitat1h (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitat5min (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitatdia (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitatmes (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')

    #Pressio de la segona estacio
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressio1min (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressio1h (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressio5min (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressiodia (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressiomes (temps INT NOT NULL PRIMARY KEY, valor REAL NOT NULL)''')

    #Garatge
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino3.portagaratge (estat CHARACTER(7))''')
    
    def crear_Files():
        #Fem els minuts
        zero=0
        for i in range(1, 6, 1):
            curs.execute("INSERT INTO arduino1.temperatura1min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino1.humitat1min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.temperatura1min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.humitat1min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.pressio1min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))

        #Fem les hores
        for i in range(0, 24, 1):
            curs.execute("INSERT INTO arduino1.temperatura1h VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.temperatura1h VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino1.humitat1h VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.humitat1h VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.pressio1h VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
        
        #Fem per els 5min
        for i in range(0, 60, 5):
            curs.execute("INSERT INTO arduino1.temperatura5min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.temperatura5min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino1.humitat5min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.humitat5min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.pressio5min VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
        
        #Fem pels dies del mes
        for i in range(1, 31, 1):
            curs.execute("INSERT INTO arduino1.temperaturadia VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.temperaturadia VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino1.humitatdia VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.humitatdia VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
            curs.execute("INSERT INTO arduino2.pressiodia VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=zero))
        
        #Fem els mesos
        
        for i in range(1, 13, 1):
            curs.execute("INSERT INTO arduino1.temperaturames VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=0))
            curs.execute("INSERT INTO arduino2.temperaturames VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=0))
            curs.execute("INSERT INTO arduino1.humitatmes VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=0))
            curs.execute("INSERT INTO arduino2.humitatmes VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=0))
            curs.execute("INSERT INTO arduino2.pressiomes VALUES ({temps}, {zero}) ON CONFLICT(temps) DO NOTHING".format(temps=i, zero=0))
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
    conexion.commit()
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
    curs.execute('ALTER TABLE arduino1.temperatura5min ALTER COLUMN valor')
    curs.execute('ALTER TABLE arduino1.temperatura1h ALTER COLUMN valor INT NOT NULL')
    curs.execute('ALTER TABLE arduino1.temperaturadia ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino1.temperaturames ALTER COLUMN valor NOT NULL')

    #HUMITAT de la primera estació
    curs.execute('ALTER TABLE arduino1.humitat5min ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino1.humitat1h ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino1.humitatdia ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino1.humitatmes ALTER COLUMN valor NOT NULL')

    #TEMPERATURA segona estació
    curs.execute('ALTER TABLE arduino2.temperatura5min ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino2.temperatura1h ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino2.temperaturadia ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino2.temperaturames ALTER COLUMN valor NOT NULL')

    #HUMITAT de la segona estació
    curs.execute('ALTER TABLE arduino2.humitat5min ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino2.humitat1h ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino2.humitatdia ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino2.humitatmes ALTER COLUMN valor NOT NULL')

    #Pressio de la segona estacio
    curs.execute('ALTER TABLE arduino2.pressio5min ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino2.pressio1h ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino2.pressiodia ALTER COLUMN valor NOT NULL')
    curs.execute('ALTER TABLE arduino2.pressiomes ALTER COLUMN valor NOT NULL')

    conexion.commit()
    conexion.close()

def borrar_taules():
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()
    curs.execute('''DROP TABLE arduino1.temperaturames CASCADE''')
    #curs.execute('''DROP TABLE arduino1.humitatmes CASCADE''')

    curs.execute('''DROP TABLE arduino2.temperaturames CASCADE''')
    #curs.execute('''DROP TABLE arduino2.humitatames CASCADE''')
    curs.execute('''DROP TABLE arduino2.pressiomes CASCADE''')

    conexion.commit()
    conexion.close()

def borrar_files_minuts():
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()

    curs.execute('''DELETE FROM arduino1.temperatura1min WHERE temps=0''')
    curs.execute('''DELETE FROM arduino1.humitat1min WHERE temps=0''')
    curs.execute('''DELETE FROM arduino2.temperatura1min WHERE temps=0''')
    curs.execute('''DELETE FROM arduino2.humitat1min WHERE temps=0''')
    curs.execute('''DELETE FROM arduino2.pressio1min WHERE temps=0''')

    conexion.commit()
    conexion.close()

def afegir_garatge():
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()
    curs.execute('''ALTER TABLE arduino3.portagaratge ADD COLUMN id INT''')
    curs.execute('''INSERT INTO arduino3.portagaratge(id) VALUES (1)''')
    conexion.commit()
    conexion.close()

crear_taules()


#borrar_taules()






