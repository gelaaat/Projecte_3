#Llibreries que necessitarem pel programa
import bluetooth
import time 
import psycopg2
from datetime import date


#Adreçes MAC dels dispositius Bluetooth que ens connectarem
arduino1="00:18:E4:40:00:06"
arduino2="20:15:03:23:75:18"
arduino3="98:D3:32:20:F7:10"
arduino4=""
port=1

#Variables globals pel funcionament del programa
data=""
datat=""
datatt=""
data2=""
count=0
portaAnterior = ""


#Prova amb dates
CURRENT_TIME_ANTERIOR = time.strftime("%H %M", time.localtime())
CURRENT_TIME = ''

today_anterior = str(date.today())[8:]
today = ''

mes_anterior = str(date.today())[5:7]
mes = ''

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
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperatura1min (temps INT NOT NULL PRIMARY KEY, valor INT)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperatura1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperatura5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperaturadia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.temperaturames (temps INT NOT NULL PRIMARY KEY, valor REAL)''')

    #HUMITAT de la primera estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitat1min (temps INT NOT NULL PRIMARY KEY, valor INT)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitat1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitat5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitatdia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino1.humitatmes (temps INT NOT NULL PRIMARY KEY, valor REAL)''')

    #TEMPERATURA segona estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperatura1min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperatura1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperatura5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperaturadia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.temperaturames (temps INT NOT NULL PRIMARY KEY, valor REAL)''')

    #HUMITAT de la segona estació
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitat1min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitat1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitat5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitatdia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.humitatmes (temps INT NOT NULL PRIMARY KEY, valor REAL)''')

    #Pressio de la segona estacio
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressio1min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressio1h (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressio5min (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressiodia (temps INT NOT NULL PRIMARY KEY, valor REAL)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino2.pressiomes (temps INT NOT NULL PRIMARY KEY, valor REAL)''')

    #Garatge
    curs.execute('''CREATE TABLE IF NOT EXISTS arduino3.portagaratge (estat CHARACTER(7), id INT)''')

    def crear_Files():
        #Fem els minuts
        for i in range(1, 6, 1):
            curs.execute("INSERT INTO arduino1.temperatura1min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino1.humitat1min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.temperatura1min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.humitat1min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.pressio1min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))

        #Fem les hores
        for i in range(0, 24, 1):
            curs.execute("INSERT INTO arduino1.temperatura1h VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.temperatura1h VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino1.humitat1h VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.humitat1h VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.pressio1h VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
        
        #Fem per els 5min
        for i in range(0, 60, 5):
            curs.execute("INSERT INTO arduino1.temperatura5min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.temperatura5min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino1.humitat5min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.humitat5min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.pressio5min VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
        
        #Fem pels dies del mes
        for i in range(1, 31, 1):
            curs.execute("INSERT INTO arduino1.temperaturadia VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.temperaturadia VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino1.humitatdia VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.humitatdia VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.pressiodia VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
        
        #Fem els mesos
        
        for i in range(1, 13, 1):
            curs.execute("INSERT INTO arduino1.temperaturames VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.temperaturames VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino1.humitatmes VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.humitatmes VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))
            curs.execute("INSERT INTO arduino2.pressiomes VALUES ({temps}) ON CONFLICT(temps) DO NOTHING".format(temps=i))

        #Fem per la porta de garatge
        curs.execute("INSERT INTO arduino3.portagaratge VALUES ('tancada', 1)")
    crear_Files()

    conexion.commit()
    conexion.close()

def insertar_dada(arduino, sensor, interval, nom_columna, nom_columna_variable, fila, dada):
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()
    curs.execute("UPDATE {arduino}.{sensor}{interval} SET {nom_columna_variable} = {dada} WHERE {nom_columna} = {fila}".format(arduino = arduino, sensor = sensor, interval = interval, nom_columna = nom_columna, nom_columna_variable = nom_columna_variable, fila = fila, dada = dada))
    conexion.commit()
    conexion.close()

def garatge(estat= 'oberta'):
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()
    curs.execute("UPDATE arduino3.portagaratge SET estat = '{estat}' WHERE id=1".format(estat = estat))
    conexion.commit()
    conexion.close()

def recuperar_dades(arduino, sensor, interval):
    conexion = psycopg2.connect(host=DADES_DB['host'], dbname=DADES_DB['dbname'], user=DADES_DB['user'], password=DADES_DB['password'], port=DADES_DB['port'])
    curs = conexion.cursor()
    curs.execute("SELECT * FROM {arduino}.{sensor}{interval} ORDER BY temps ASC".format(arduino = arduino, sensor = sensor, interval = interval))
    dades = curs.fetchall()
    conexion.close()
    return dades

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

#Creeem els Schemas i taules de la nostra base de dades
crear_taules()


#Main loop del programa
while 1:

    #Agafem els valors del temps

    CURRENT_TIME = time.strftime("%H %M", time.localtime()) #Retorna el temps en hh-mm 
    today = str(date.today())[8:] #Retorna data aaaa-mm-dd per tant nomes agafarem dd
    mes = str(date.today())[5:7] #Retorna data aaaa-mm-dd per tant nomes agafarem mm
    Kai=int(CURRENT_TIME[4])
    if Kai<=4:
        Kai=Kai+1
    else:
        Kai=Kai-4

    '''
    Primer configurarem i comprovarem el garatge, perque el Bluetooth no interfereixi en els altres, 
    ja que es comprova tota l'estona sense desconnectar-lo
    '''
    
    first_time=0
    

    while( CURRENT_TIME[4] == CURRENT_TIME_ANTERIOR[4] and (CURRENT_TIME[4] != '0' and CURRENT_TIME[4] != 5) ):
        CURRENT_TIME_ANTERIOR = time.strftime("%H %M", time.localtime())
        
        if first_time==0:
            try:
                sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                sock.connect((arduino3,port))
                first_time=1
                
            
            except:
                print('no')
                sock.close()
                break

        data2=sock.recv(1204)
        porta=""
        for valor in data2:
            porta=porta+chr(valor)
        

        if int(porta)==0:
            text_porta="tancada"
        else:
            text_porta="oberta"

        if(porta != portaAnterior):
            print(text_porta)
            garatge(text_porta)
            portaAnterior = porta
        


    '''
        *********MAIN PROGRAMA**************
    '''
    if ( CURRENT_TIME[4] != CURRENT_TIME_ANTERIOR[4] ):

        CURRENT_TIME_ANTERIOR = time.strftime("%H %M", time.localtime())

        try:

            sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((arduino2,port))
            sock.send('1')
            ack=sock.recv(1204)
            
            while(ack ==" "):
                ack=sock.recv(1204)
                
            time.sleep(0.12)
            data=sock.recv(1204)
            time.sleep(0.1)
            datat=sock.recv(1204)
            temp1=""
            humitat1=""
            press=""
            sock.close()

            for valor in data:
                temp1=temp1+chr(valor)

            for valor in datat:
                humitat1=humitat1+chr(valor)

            if int(temp1)<=3 or int(temp1)>99:
                print('eeiii ho he cambiat')
                temp1=temp1_ant
                humitat1=humitat1_ant

            humitat1_ant=humitat1
            temp1_ant=temp1
            
            print(str(temp1))
            print(str(humitat1))
            
            insertar_dada('arduino1', 'temperatura', '1min', 'temps', 'valor', Kai, int(temp1))
            insertar_dada('arduino1', 'humitat', '1min', 'temps', 'valor',Kai, int(humitat1))

            sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((arduino1,port))
            sock.send('1')
            ack=sock.recv(1204)
            while(ack ==" "):
                ack=sock.recv(1204)
                
            time.sleep(0.12)
            data=sock.recv(1204)
            time.sleep(0.1)
            datat=sock.recv(1204)
            time.sleep(0.12)
            datatt=sock.recv(1204)
            sock.close()
            temp2=""
            humitat2=""
            press=""
            
            for valor in data:
                temp2=temp2+chr(valor)

            for valor in datat:
                humitat2=humitat2+chr(valor)
            
            for valor in datatt:
                press=press+chr(valor)
            
            print(str(temp2))
            print(str(humitat2))
            print(str(press))

            
            insertar_dada('arduino2', 'temperatura', '1min', 'temps', 'valor', Kai, float(temp2))
            insertar_dada('arduino2', 'humitat', '1min', 'temps', 'valor', Kai , float(humitat2))
            insertar_dada('arduino2', 'pressio', '1min', 'temps', 'valor', Kai , float(press))
        
        except:
            sock.close()
    
    CURRENT_TIME = time.strftime("%H %M", time.localtime()) 


    #Tot seguit farem la lògica per omplir els gràfics

    #Aquest if es per fer les mitjanes per omplir el grafic dels 5min
    if(CURRENT_TIME[4] == '5' or CURRENT_TIME[4] == '0'):

        #Fem primera la primera arduino
        #Temperatura
        dades_temperatura_1min = recuperar_dades('arduino1', 'temperatura', '1min')

        sumatori = 0
        longitud = 0

        for dada in dades_temperatura_1min:

            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino1', 'temperatura', '5min', 'temps', 'valor', CURRENT_TIME[3:], resultat)

        #Humitat
        dades_humitat_1min = recuperar_dades('arduino1', 'humitat', '1min')
        
        sumatori = 0
        longitud = 0

        for dada in dades_humitat_1min:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino1', 'humitat', '5min', 'temps', 'valor', CURRENT_TIME[3:], resultat)


        #Fem la segona estacio
        #Temperatura
        dades_temperatura_1min = recuperar_dades('arduino2', 'temperatura', '1min')
        
        sumatori = 0
        longitud = 0

        for dada in dades_temperatura_1min:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'temperatura', '5min', 'temps', 'valor', CURRENT_TIME[3:], resultat)

        #Humitat
        dades_humitat_1min = recuperar_dades('arduino2', 'humitat', '1min')
        
        sumatori = 0
        longitud = 0

        for dada in dades_humitat_1min:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'humitat', '5min', 'temps', 'valor', CURRENT_TIME[3:], resultat)

        #Pressio
        dades_pressio_1min = recuperar_dades('arduino2', 'pressio', '1min')
        
        sumatori = 0
        longitud = 0

        for dada in dades_pressio_1min:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'pressio', '5min', 'temps', 'valor', CURRENT_TIME[3:], resultat)

    #Aquest if es per fer les mitjanes per omplir el grafic de les hores
    if(CURRENT_TIME[3] == "0" and CURRENT_TIME[4] == "0"):
        #Aqui farem les mitjanes per posar-ho al grafic de les hores

        #Fem primera la primera arduino
        #Temperatura
        dades_temperatura_5min = recuperar_dades('arduino1', 'temperatura', '5min')
        
        sumatori = 0
        longitud = 0

        for dada in dades_temperatura_5min:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino1', 'temperatura', '1h', 'temps', 'valor', CURRENT_TIME[:2], resultat)

        #Humitat
        dades_humitat_5min = recuperar_dades('arduino1', 'humitat', '5min')
        
        sumatori = 0
        longitud = 0

        for dada in dades_humitat_5min:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino1', 'humitat', '1h', 'temps', 'valor', CURRENT_TIME[:2], resultat)



        #Fem ara per la segona estacio
        #Temperatura
        dades_temperatura_5min = recuperar_dades('arduino2', 'temperatura', '5min')
        
        sumatori = 0
        longitud = 0

        for dada in dades_temperatura_5min:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'temperatura', '1h', 'temps', 'valor', CURRENT_TIME[:2], resultat)
        

        #Humitat
        dades_humitat_5min = recuperar_dades('arduino2', 'humitat', '5min')
        
        sumatori = 0
        longitud = 0

        for dada in dades_humitat_5min:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'humitat', '1h', 'temps', 'valor', CURRENT_TIME[:2], resultat)


        #Pressio
        dades_pressio_5min = recuperar_dades('arduino2', 'pressio', '5min')
        
        ssumatori = 0
        longitud = 0

        for dada in dades_pressio_5min:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'pressio', '1h', 'temps', 'valor', CURRENT_TIME[:2], resultat)

    #Aquest if es per fer mitjanes per omplir el grafic dels dies
    if(today != today_anterior):

        #Fem primera la primera arduino
        #Temperatura
        dades_temperatura_1h = recuperar_dades('arduino1', 'temperatura', '1h')
        
        sumatori = 0
        longitud = 0

        for dada in dades_temperatura_1h:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino1', 'temperatura', 'dia', 'temps', 'valor', today_anterior, resultat)

        #Humitat
        dades_humitat_1h = recuperar_dades('arduino1', 'humitat', '1h')
        
        sumatori = 0
        longitud = 0

        for dada in dades_humitat_1h:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino1', 'humitat', 'dia', 'temps', 'valor', today_anterior, resultat)



        #Fem ara per la segona estacio
        #Temperatura
        dades_temperatura_1h = recuperar_dades('arduino2', 'temperatura', '1h')
        
        sumatori = 0
        longitud = 0

        for dada in dades_temperatura_1h:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'temperatura', 'dia', 'temps', 'valor', today_anterior, resultat)
        

        #Humitat
        dades_humitat_1h = recuperar_dades('arduino2', 'humitat', '1h')
        
        sumatori = 0
        longitud = 0

        for dada in dades_humitat_1h:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'humitat', 'dia', 'temps', 'valor', today_anterior, resultat)


        #Pressio
        dades_pressio_1h = recuperar_dades('arduino2', 'pressio', '1h')
        
        sumatori = 0
        longitud = 0

        for dada in dades_pressio_1h:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'pressio', 'dia', 'temps', 'valor', today_anterior, resultat)
        today_anterior = str(date.today())[8:]

    #Aquest if es per fer mitjanes per omplir el grafic dels messos
    if(mes != mes_anterior):

        #Fem primera la primera arduino
        #Temperatura
        dades_temperatura_dia = recuperar_dades('arduino1', 'temperatura', 'dia')
        
        sumatori = 0
        longitud = 0

        for dada in dades_temperatura_dia:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino1', 'temperatura', 'dia', 'temps', 'valor', mes_anterior, resultat)

        #Humitat
        dades_humitat_dia = recuperar_dades('arduino1', 'humitat', 'dia')
        
        sumatori = 0
        longitud = 0

        for dada in dades_humitat_dia:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino1', 'humitat', 'dia', 'temps', 'valor', mes_anterior, resultat)



        #Fem ara per la segona estacio
        #Temperatura
        dades_temperatura_dia = recuperar_dades('arduino2', 'temperatura', 'dia')
        
        sumatori = 0
        longitud = 0

        for dada in dades_temperatura_dia:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'temperatura', 'dia', 'temps', 'valor', mes_anterior, resultat)
        

        #Humitat
        dades_humitat_dia = recuperar_dades('arduino2', 'humitat', 'dia')
        
        sumatori = 0
        longitud = 0

        for dada in dades_humitat_dia:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'humitat', 'dia', 'temps', 'valor', mes_anterior, resultat)


        #Pressio
        dades_pressio_dia = recuperar_dades('arduino2', 'pressio', 'dia')
        
        sumatori = 0
        longitud = 0

        for dada in dades_pressio_dia:
            
            if(dada[1] == None):
                continue
            else:
                sumatori = sumatori + dada[1]
                longitud = longitud + 1

        resultat = 0
        resultat = sumatori/longitud

        insertar_dada('arduino2', 'pressio', 'dia', 'temps', 'valor', mes_anterior, resultat)
        mes_anterior = str(date.today())[5:7]