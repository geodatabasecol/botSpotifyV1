# -*- coding: utf-8 -*-

from os import access
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
                    print(f"visibleBotonGoogle {xpathBotonLogin}")
            else:
                print(f"visibleInputPassword {visibleInputPassword}")
        else:
            print(f"visibleInputCuenta {visibleInputEmail}")


    def esperarResumeApp(self):

        xpathBotonResumeApp = (By.XPATH, "//span[contains(text(),'Resume app')]")

        visibleBotonResumeApp = self.explicitWaitElementoVisibility(1200,xpathBotonResumeApp)
        if visibleBotonResumeApp:
            print('boton encontrado')
            
            return True

        else:
            print(f"visibleBotonResumeApp {visibleBotonResumeApp}")

    def iniciarVsCode(self):

        xpathBotonResumeApp = (By.XPATH, "//span[contains(text(),'Resume app')]")
        xpathBotonOpenInBrowser = (By.XPATH, "//span[contains(text(),'Open in browser')]")

        xpathDivStatusBuilding = (By.XPATH, "//div[@status='Building']")

        # div status="Building"  //div[@status="Building"]

        self.click(xpathBotonResumeApp)

        invisibleDivStatusBuilding = self.explicitWaitElementoInvisibility(1200,xpathDivStatusBuilding)
        if invisibleDivStatusBuilding:

            visibleBotonResumeApp = self.explicitWaitElementoVisibility(60,xpathBotonResumeApp)
            if visibleBotonResumeApp:
                print('boton xpathBotonResumeApp')
                
                self.click(xpathBotonResumeApp)

            else:

                visibleBotonOpenInBrowser = self.explicitWaitElementoVisibility(60,xpathBotonOpenInBrowser)
                if visibleBotonOpenInBrowser:

                    self.click(xpathBotonOpenInBrowser)

                    return True

                else:
                    print(f"visibleBotonOpenInBrowser {visibleBotonOpenInBrowser}")

            #cantidadTabs = self.cantidadWindowHandle()

    def vscodeTab(self):

        cantidadTabs = self.cantidadWindowHandle()

        if cantidadTabs == 2:
            self.cambiarTabEspecifico(cantidadTabs[1])

            self.sleep(120)
        else:
            print(f"cantidadTabs {cantidadTabs}")
