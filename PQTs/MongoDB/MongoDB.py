# -*- coding: utf-8 -*-

import pymongo

from PQTs.Utilizar import UrlDB

class MongoDB:

    def __main__(self):
        self.UrlDB = UrlDB
        self.Client = None
        self.DB = None

    def iniciarDB(self,db):
        self.Client = pymongo.MongoClient(UrlDB)
        self.DB = self.Client[db]

    def insertOne(self,coleccion,dato):
        self.DB[coleccion].insert_one(dato)

    def insertMany(self,coleccion,dato):
        self.DB[coleccion].insert_many(dato)

    def find(self,coleccion,dato):
        return list(self.DB[coleccion].find(dato))

    def updateOne(self,coleccion,dato,actualizar):
        self.DB[coleccion].update_one(dato,actualizar)

    def cerrarConexion(self,):
        self.Client.close()