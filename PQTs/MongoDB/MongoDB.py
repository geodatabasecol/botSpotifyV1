# -*- coding: utf-8 -*-

import pymongo

from PQTs.Utilizar import UrlDB, accountsDB

class MongoDB:
    
    def __init__(self):
        self.UrlDB = UrlDB
        self.Client = None
        self.DB = None
        self.accountsDB=accountsDB

    def iniciarDB(self):
        self.Client = pymongo.MongoClient(self.UrlDB)
        self.DB = self.Client[self.accountsDB]


    def insertOne(self,coleccion,dato):
        self.DB[coleccion].insert_one(dato)

    def insertMany(self,coleccion,dato):
        self.DB[coleccion].insert_many(dato)

    def findby1(self,coleccion,clave, valor):
        return list(self.DB[coleccion].find({clave:valor}).limit(1))

    def findby2(self,coleccion,clave1, valor1,clave2,valor2):
        return list(self.DB[coleccion].find({clave1:valor1},{clave2:valor2}))


    def updateOne(self,coleccion,id,clave,valor):
        self.DB[coleccion].update_one({"_id":id},{"$set":{clave:valor}})

    def cerrarConexion(self,):
        self.Client.close()