#import mysql.connector
import urllib
import sys
import re
import os
from collections import namedtuple
from dataclasses import dataclass
from typing import Any
import sqlite3

class MysqlBase:
        def __init__(self, ownerComp):
                op.DP.Display("{} init".format(self))
                # c=self.CUE(0,0,"a", 1, 1)
                self.conn=None
        
        def __del__(self):
                self.DisconnectDb()

        def ConnectDb(self):
                if self.conn is None:
                        # self.conn = mysql.connector.connect(host=self.Dbhost, database=self.Dbname, user=self.Dbuser, password=self.Dbpassword)
                        self.conn=sqlite3.connect('DB/CuryCueSQLite.db')
                        ui.status="SQLite connection opened"

                
                
                
                
                # if self.conn.is_connected():
                #         msg="Подключение к базе данных успешно"
                #         ui.status=msg
                #         print (msg)
                # else:
                #         msg="ОШИБКА подключения к базе данных!"
                #         ui.status=msg
                #         print (msg)

        def DisconnectDb(self):
                if self.conn is not None:
                        self.conn.close()
                        ui.status="SQLite connection closed"
        def getListFromTable(self, query, arguments):
                cursor = self.conn.cursor()
                # print (query)
                # query= query.replace("%s", "?")
                cursor.execute(query, arguments)
                rows = cursor.fetchall()
                
                return rows
        def getListByFields(self, inputQuery):
                fieldsEscaped=[]
                if inputQuery.fields_query_prefix is not None and len(inputQuery.fields_query_prefix)==len(inputQuery.fields):
                        for i in range (0, len(inputQuery.fields)):
                                fieldsEscaped.append("{}.`{}`".format(inputQuery.fields_query_prefix[i], inputQuery.fields[i]))
                else:
                        fieldsEscaped=["`{}`".format(x) for x in inputQuery.fields]
                
                fields=", ".join(fieldsEscaped)
                queryCondition=""
                queryConditionValues=[]
                
                if len(inputQuery.condition) > 0:
                        queryCondition="WHERE "+inputQuery.condition
                        queryConditionValues=inputQuery.conditionData
                if len(inputQuery.order) > 0:
                        queryCondition+=" ORDER BY {}".format(inputQuery.order)
                query="SELECT {} FROM {} {};".format(fields, inputQuery.table, queryCondition)
                # op.DP.PrintAndDisplay(query)
                return self.getListFromTable(query, queryConditionValues)
                
        def insertIntoTable(self, inputQuery):
                fieldsEscaped=", ".join(["`{}`".format(x) for x in inputQuery.fields])
                # fieldsDataEscaped=["`{}`".format(x) for x in inputQuery.fieldsDataEscaped]
                queryCondition=""
                queryConditionValues=[]
                
                myFieldsTemplate=", ".join(['?' for field in inputQuery.fieldsData])

                if len(inputQuery.condition) > 0:
                        queryCondition="WHERE "+inputQuery.condition
                        queryConditionValues=inputQuery.conditionData
                query="REPLACE INTO {} ({}) VALUES ({}) {};".format(inputQuery.table, fieldsEscaped,
                 myFieldsTemplate, inputQuery.condition)


                return self.executeUpdateQuery(query, inputQuery.fieldsData)
        def executeUpdateQuery(self, query, arguments):
                cursor = self.conn.cursor()
                
                try:
                        print (query)
                        print ("\n")
                        print (arguments)
                        # query=query.replace("%s", "?")
                        cursor.execute(query, arguments)
                        
                        self.conn.commit()
                except :
                        
                        print ("Something went wrong")
                        return (False, "Something went wrong")
                return (True, cursor.lastrowid)

        @dataclass
        class QUERY:
                table: str
                fields: []
                conditionData: []
                fields_query_prefix: Any = None
                condition: str = ""
                order: str = ""
        @dataclass
        class QUERY_INSERT:
                table: str
                fields: []
                fieldsData: []
                conditionData: []
                condition: str = ""
        @property
        def Dbname(self):
                __Dbname=str(self.ownerComp.par.Dbname)
                return __Dbname
        @property
        def Dbhost(self):
                __Dbhost=str(self.ownerComp.par.Dbhost)
                return __Dbhost
        @property
        def Dbpassword(self):
                __Dbpassword=str(self.ownerComp.par.Dbpassword)
                return __Dbpassword                               
        @property
        def Dbuser(self):
                __Dbuser=str(self.ownerComp.par.Dbuser)
                return __Dbuser

