# -*- coding: utf-8 -*-

import pymongo

from PQTs.Utilizar import UrlDB, accountsDB

class MongoDB:
    
    def __main__(self):
        self.UrlDB = UrlDB
        self.Client = None
        self.DB = None
        self.accountsDB=accountsDB

    def iniciarDB(self):
        self.Client = pymongo.MongoClient("mongodb+srv://silklips:!Fps91507856@mycrypta.ugxec.mongodb.net/?retryWrites=true&w=majority")
        self.DB = self.Client["accounts"]


    def insertOne(self,coleccion,dato):
        self.DB[coleccion].insert_one(dato)

    def insertMany(self,coleccion,dato):
        self.DB[coleccion].insert_many(dato)

    def findby1(self,coleccion,clave, valor):
        return list(self.DB[coleccion].find({clave:valor}).limit(10))

    def findby2(self,coleccion,clave1, valor1,clave2,valor2):
        return list(self.DB[coleccion].find({clave1:valor1},{clave2:valor2}))


    def updateOne(self,coleccion,id,clave,valor):
        self.DB[coleccion].update_one({"_id":id},{"$set":{clave:valor}})

    def cerrarConexion(self,):
        self.Client.close()