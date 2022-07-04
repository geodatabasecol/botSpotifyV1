# -*- coding: utf-8 -*-

from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesSingin import Acciones

def iniciarSpotify():

    cuenta = 'xmulsikas@gmail.com'
    password = '!asdf2021'

    driver = BaseConexion().conexionChrome()
    #driver = BaseConexion().conexionChromeHeadless()

    acciones = Acciones(driver)

    acciones.ingresarSpotify()
    
    returnLoginSpotify= acciones.loginSpotify(cuenta,password)

    if returnLoginSpotify == True:
        print(f"returnSinginSpotify {returnLoginSpotify}")

    # 


iniciarSpotify()