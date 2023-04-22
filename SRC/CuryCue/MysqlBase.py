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
                        
                        if os.path.exists(self.Sqlitedatabasefile):
                                self.conn=sqlite3.connect(self.Sqlitedatabasefile)
                                ui.status="SQLite connection opened"
                        else:
                                print("File does not exist")
                                self.conn=sqlite3.connect(self.Sqlitedatabasefile)
                                self.createNewDatabase()
                
                
                
                
                # if self.conn.is_connected():
                #         msg="Connection to the database is successful"
                #         ui.status=msg
                #         print (msg)
                # else:
                #         msg="ERROR connecting to the database!"
                #         ui.status=msg
                #         print (msg)
        def createNewDatabase(self):
                sql_commands = '''
                CREATE TABLE cue (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "order" REAL DEFAULT NULL,
                name TEXT DEFAULT NULL,
                memo TEXT NOT NULL DEFAULT ' ',
                type TEXT NOT NULL DEFAULT 'Regular',
                update_mode TEXT NOT NULL DEFAULT 'Stored',
                osc_bind TEXT DEFAULT NULL,
                dmx_bind INTEGER DEFAULT NULL,
                linked INTEGER DEFAULT NULL,
                is_enabled INTEGER DEFAULT 1,
                order_new REAL DEFAULT NULL
                , frame_bind INTEGER DEFAULT 0);

                CREATE TABLE cue_float_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cue INTEGER NOT NULL,
                id_fixture INTEGER NOT NULL,
                par_name TEXT NOT NULL,
                par_value REAL DEFAULT 0,
                par_text_value TEXT,  -- make the column nullable
                fade_in REAL DEFAULT 0,
                fade_out REAL DEFAULT 0,
                delay_in REAL DEFAULT 0,
                delay_out REAL DEFAULT 0,
                UNIQUE(id_cue, id_fixture, par_name)
                );

                CREATE TABLE fixture (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "order" REAL DEFAULT 999,
                name TEXT DEFAULT NULL,
                global_object_location TEXT NOT NULL,
                type INTEGER DEFAULT 0,
                is_enabled INTEGER NOT NULL DEFAULT 1,
                UNIQUE(global_object_location)
                );

                CREATE TABLE fixture_float_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_fixture INTEGER NOT NULL,
                par_name TEXT NOT NULL,
                default_value REAL NOT NULL DEFAULT 0,
                fade_default REAL NOT NULL DEFAULT 1,
                delay_default REAL NOT NULL DEFAULT 0,
                is_enabled INTEGER DEFAULT 1
                );
                '''

                # Execute the SQL commands
                self.conn.executescript(sql_commands)

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
                        # print (query)
                        # print ("\n")
                        # print (arguments)
                        # query=query.replace("%s", "?")
                        cursor.execute(query, arguments)
                        
                        self.conn.commit()
                except :
                        
                        print ("Something went wrong")
                        ui.status="Something went wrong"
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
        def Sqlitedatabasefile(self):
                __Sqlitedatabasefile=str(self.ownerComp.par.Sqlitedatabasefile)
                return __Sqlitedatabasefile
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

