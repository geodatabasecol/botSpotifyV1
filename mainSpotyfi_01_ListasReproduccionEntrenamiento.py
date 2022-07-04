# -*- coding: utf-8 -*-

from cmath import e
import time
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesSingin import Acciones
from threading import Thread, Barrier

password='!asdf2021'

def accountsSpotify():

    id=[]
    email =[]
    

    db=MongoDB()
    db.iniciarDB()
    for elem in (db.findby1("accountmanager","acc_estado",1)):
        email.append(elem["email"])
        id.append(elem["_id"])
    for elemid in id:
        db.updateOne("accountmanager",elemid,"creacionlistasentrenamiento",2)
    db.cerrarConexion()
    return email
print (len(accountsSpotify()))


    
def iniciarSpotify(barrier,email,password,i):


    driver = BaseConexion().conexionChrome()
    #driver = BaseConexion().conexionChromeHeadless()

    acciones = Acciones(driver)

    acciones.ingresarSpotify()
    
    returnLoginSpotify= acciones.loginSpotify(email,password)

    if returnLoginSpotify == True:
        print(f"Hilo {i} - SinginSpotify {returnLoginSpotify}")

    time.sleep(120)
    # 

users= accountsSpotify()
barrier = Barrier(len(users))
hiloscerrados = 0
threads = []
for i in range(len(users)):
    i = Thread(target=iniciarSpotify, args=(barrier,users[i],password,i))
    i.start()
    threads.append(i)

for i in threads:
	i.join()
 
#iniciarSpotify()
