# -*- coding: utf-8 -*-

from os import access
import random
import time
from PQTs.Selenium.Base import BaseAcciones

from PQTs.Utilizar import urlSpotifysinginUS

from selenium.common import exceptions
from selenium.webdriver.common.by import By

class Acciones(BaseAcciones):

    def ingresarSpotify(self):
        self.ir(urlSpotifysinginUS)

    def loginSpotify(self,cuenta,password):
        xpathInputEmail = (By.ID,"login-username")
        xpathInputPassword = (By.ID,"login-password")        
        xpathBotonLogin= (By.ID,"login-button")
        visibleInputEmail = self.explicitWaitElementoVisibility(11,xpathInputEmail)
        if visibleInputEmail:
            self.escribir(xpathInputEmail,cuenta)
            
            visibleInputPassword = self.explicitWaitElementoVisibility(11,xpathInputPassword)
            if visibleInputPassword:
                self.escribir(xpathInputPassword,password)
                

                visibleBotonLogin = self.explicitWaitElementoVisibility(11,xpathBotonLogin)
                if visibleBotonLogin:
            
                    self.click(xpathBotonLogin)
                    self.explicitWaitElementoInvisibility(11,xpathBotonLogin)


                    return True

                else:
                    print(f"visibleBotonLogin {xpathBotonLogin}")
            else:
                print(f"visibleInputPassword {visibleInputPassword}")
        else:
            print(f"visibleInputEmail {visibleInputEmail}")

    
    def nuevalista(self):
        xpathnuevalista = (By.XPATH, "//*[@id='main']/div/div[2]/nav/div[1]/div[2]/div/div[1]/button")
        visiblenuevalista = self.explicitWaitElementoVisibility(1200,xpathnuevalista)
        if visiblenuevalista:
            self.click(xpathnuevalista)
            print('Click nueva lista')
            return True
        else:
            print(f"visibleNuevalista {visiblenuevalista}")

    def buscaryagregarartista(self):
        listartistas=["The Beatles","Mariah Carey","Elvis Presley","Rihanna","Michael Jackson",
        "Madonna","Billie Eilish","Bruno Mars","Britney Spears","Bachman-Turner Overdrive",
        "Bad Bunny","Bad English","Bananarama","The Bangles","Barenaked Ladies","Toni Basil",
        "Les Baxter","Bay City Rollers","The Beach Boys","The Beatles","Stephanie Beatriz",
        "Bee Gees","The Bellamy Brothers","Regina Belle","Lauren Bennett","Berlin","Bradley Cooper",
        "Chuck Berry","Beyoncé","Mr. Acker Bilk","Mary J. Blige","Blondie","Blue Swede","James Blunt",
        "Michael Bolton","Bon Jovi","Jon Bon Jovi","Gary U.S. Bonds","Krayzie Bone","Debby Boone",
        "Pat Boone","Boston","David Bowie","Box Tops","Brandy","Toni Braxton","Bread",
        "Bobby Brown","Chris Brown","Sleepy Brown","The Browns","Peabo Bryson",
        "The Buckinghams","The Byrds"]

        itemsagregar=[
            [
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[2]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[3]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[4]/div/div[3]/button'
        ],
        [
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[3]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[4]/div/div[3]/button'
        ]]
       
        mylistartistas=random.sample(listartistas, 3)
        print (mylistartistas)
        
        xpathbuscarartista=(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/section/div/div/input')
                
        visiblebuscarartista= self.explicitWaitElementoVisibility(1200,xpathbuscarartista)
        if visiblebuscarartista:
            
            for  elem in mylistartistas:
                self.clear(xpathbuscarartista)
                self.escribir(xpathbuscarartista,elem)
                time.sleep(5)
                print('Click nueva lista')
                it=0
                for item in itemsagregar[it]:
                    xpathcancion=(By.XPATH,item )
                    self.click(xpathcancion)
                    print("cancion agregada")
                    time.sleep(5)
                    it+=1
        
        else:
            print(f"visibleNuevalista {visiblebuscarartista}")


        

      
        


    
