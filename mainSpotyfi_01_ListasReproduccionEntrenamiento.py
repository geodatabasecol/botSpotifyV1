# -*- coding: utf-8 -*-
#TESTTTTT

import time
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesSinginSpotify import Acciones
from threading import Thread, Barrier

password='!asdf2021'
hilos=2
def accountsSpotify():

    id=[]
    email =[]
    

    db=MongoDB(hilos)
    db.iniciarDB()
    for elem in (db.findby1("accountmanager","acc_estado",1)):
        email.append(elem["email"])
        id.append(elem["_id"])
    for elemid in id:
        db.updateOne("accountmanager",elemid,"creacionlistasentrenamiento",2)
    db.cerrarConexion()
    return email, id

users, id= accountsSpotify()
print (len(users))
    
def iniciarSpotify(barrier,email,password,i,id):


    driver = BaseConexion().conexionChrome()
    #driver = BaseConexion().conexionChromeHeadless()

    acciones = Acciones(driver)
    try:
        acciones.ingresarSpotify()
    except:
        acciones.reload()
        acciones.ingresarSpotify()

    returnLoginSpotify= acciones.loginSpotify(email,password)

    if returnLoginSpotify == True:
        print(f"Hilo {i} - SinginSpotify {returnLoginSpotify}")

    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    acciones.nuevalista()
    time.sleep(2)
    acciones.buscaryagregarartista()

    db=MongoDB(hilos)
    db.iniciarDB()
    for elemid in id:
        db.updateOne("accountmanager",elemid,"creacionlistasentrenamiento",1)
    db.cerrarConexion()
    print (f"Account {i} lista de reproduccion de entrenamiento creada ok")
    # 


barrier = Barrier(len(users))
hiloscerrados = 0
threads = []
for i in range(len(users)):
    i = Thread(target=iniciarSpotify, args=(barrier,users[i],password,i,id[i]))
    i.start()
    threads.append(i)

for i in threads:
	i.join()
 
#iniciarSpotify()


