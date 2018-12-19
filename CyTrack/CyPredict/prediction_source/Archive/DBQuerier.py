'''
Created on Feb 11, 2017

A static database querier class to make queries on the database. 

@author: DGXU
'''
import mysql.connector
import json

DEFAULT_DBNAME = "test"
DEFAULT_USERNAME = "root"
DEFAULT_PASSWORD = "testdb"
DEFAULT_HOST = "localhost"
DEFAULT_TB = "testtb"


dbConfig = {
   "database": DEFAULT_DBNAME,
    "user": DEFAULT_USERNAME,
    "password": DEFAULT_PASSWORD,
    "host": DEFAULT_HOST
    }
currTB = DEFAULT_TB


#prob shouldn't exist but creates a database in the host
def createDB(name):
    conn = mysql.connector.connect(**dbConfig)
    try:   
        cur = conn.cursor()
        query = 'CREATE DATABASE ' + name
        cur.execute(query)
        
    except mysql.connector.Error as err:
        print(err)
    finally:
        conn.close()
            
#creates a table maybe shouldn't use either
def createTB(tbName, colmnId, colmnDatatype, prKey):
    query = "CREATE TABLE "+tbName +" (" + colmnId[0]+ " " +colmnDatatype[0] 
    conn = mysql.connector.connect(**dbConfig)
    for i in range(1, len(colmnId)):
        query =query + ", " + colmnId[i] + " " +colmnDatatype[i]
    if prKey is not None:
        query = query+", PRIMARY KEY ("+prKey+")"
    query =query+ ")"
    #print(query)
    try:
        cur = conn.cursor()
        cur.execute(query)
    except mysql.connector.Error as err:
        print(err)
    finally:
        conn.close()
        
#Maybe shouldn't use the above to functions... Create the database and the table 
#in the actual server. In case there is a reason to use then they are there for use.

#prints out the table
def showTable(table):
    conn = mysql.connector.connect(**dbConfig)
    rows = ""
    try:
        query = "SELECT * FROM " + table
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        
        print(rows)
    except mysql.connector.Error as err:
        print(err)
    finally:
        conn.close()
        return rows
    
#inserts into the table, NOTE you don't need to include any auto-incrementing things
def insertRow(tbName, colmnId, colmnVals):
        
        if len(colmnId) != len(colmnVals):
            raise ValueError("The amount of IDs and do not match amount of values", "colmnId", "colmnVals")
        
        insertRowDict(tbName, dict(zip(colmnId, colmnVals)))
    
#inserts row using a dictionary as a param 
"""
Inserts a row into a table with the given dictionary. 

@param tbName: name of the table that is being inserted into.
@param insertDict: a dictionary of the values that are inserted into. 
            The key is the name of the column and the value is the value
            that the column should hold.
"""
def insertRowDict(tbName, insertDict):
    
    query = "INSERT INTO " + tbName + " ("
    valString = ") VALUES ("
    
    for key in insertDict:
        query += key + ", "
        valString += "%("+key+")s, "
        
    query = query[:len(query)-2] + valString[:len(valString)-2] +")"
    
    #print to check format of query string.
    #general format should be "INSERT INTO tbname (key1, key2, ... keyn) VALUES (%(key1)s, %(key2)s, ... %(keyn)s)
    print(query) 
    
    _executeQuery(query, insertDict)
    
def deleteRow(tbName, colmnIds, colmnVals, operators):
    
    if len(colmnIds) != len(colmnVals):
        raise ValueError("The amount of IDs and do not match amount of values", "colmnIds", "colmnVals")
        
    deleteRowDict(tbName, dict(zip(colmnIds, colmnVals)), dict(zip(colmnIds, operators)))

#I don't like this but for now there are two dicts with the same keys and it goes though
#those when creating the query 
"""
Deletes one or more rows with the given conditions.

@param tbName: name of the table that is being deleted from.
@param whereDict: a dictionary containing the column id and what it should be called.
                The key is the column name that is to be checked and value is what 
                it is being compared to.
@param operatorsDict: a dictionary containing the operators that are used for the  
                conditions of the whereDict. The key is the column name and the 
                value is the operator(i.e. =, <=, >=, etc) that should be in
                between the key and the value of the whereDict.
"""
def deleteRowDict(tbName, whereDict, operatorsDict):
    if whereDict is None or len(whereDict) != len(operatorsDict):
        raise ValueError("Invalid params for WHERE statement")
    
    query = "DELETE FROM " + tbName + " WHERE "
    
    for key in whereDict:
        query += key + operatorsDict[key] + "%(" + key + ")s AND "
        
    query = query[:len(query) - 5] #gets rid of the last AND
    
    #print used to check validity of the query string.
    #format should be: "DELETE FROM tbName WHERE key1=%(key1)s AND key2<=%(key2)s AND... "
    print(query)
    
    _executeQuery(query, whereDict)
    
#works similarly to how delete works but instead retrieves data
"""
retrieves the values from the given table based on the params.

@param tbName: name of table to be read from.
@param colList: list of column names that are to be retrieved.
@param colKey: column name that is to be checked with with the key.
@param key: the value that the colKey should be.
@return: a list of tuples that represent the values in the table.
        Each tuple is a different row, the tuple has the different column values.
"""
def read(tbName, colList, colKey, key):
    if colList is None or key is None:
        raise ValueError("Invalid params for WHERE statement")
    
    query = "SELECT "
    for col in colList:
        query += col +", "
    
    query = (query[:len(query)-2] + " FROM " + tbName + 
             " WHERE " + colKey + "=" + key)
    
    #print for checking validity of query string
    #format should be: "SELECT colname1, colname2, ... colnamen FROM tbName WHERE colKey=key"
    print(query)
    
    values = ""
    try:
        conn = mysql.connector.connect(**dbConfig)
        cur = conn.cursor()
        cur.execute(query)
        values = cur.fetchall()
    except mysql.connector.Error as err:
        print(err)
    finally:
        cur.close()
        return values

#updates the parts of a database
"""
update the given fields in a table.

@param tbName: name of table to be updated.
@param fieldDict: a dictionary of the values that should be changed to.
                The key is the name of the column that is to be updated.
                The value is the value that the column should be changed to.
@param whereDict: a dictionary of the components of the WHERE clause. 
                The key is the name of the column that is checked with the value.
                The value is the value that key must match to be updated.
@param operatorsDict: a dictionary of the operators for the WHERE clause.
                The key is the corresponding column id. The value is the
                operator used in between the whereDict's key and value.
"""
def updateDict(tbName, fieldDict, whereDict, operatorsDict):
    if fieldDict is None or len(whereDict) != len(operatorsDict):
        raise ValueError("Invalid params for updateDict")
    
    query = "UPDATE " + tbName + " SET "
    for field in fieldDict:
        query += field + "=%(" + field + ")s AND " 
    query = query[:len(query) - 5] + " WHERE " #gets rid of the last AND
    
    for key in whereDict:
        query += key + operatorsDict[key] + "%(" + key + ")s AND "
    query = query[:len(query) - 5]#gets rid of the last AND
    
    fieldDict.update(whereDict)
    
    #print used for checking validity of the query string
    #format should be: "UPDATE tbName SET field1=%(field1) AND, ... fieldn=%(fieldn) WHERE key1=%(key1)s AND, ..."
    print(query)
    _executeQuery(query, fieldDict)
    
#specific table that all data from the table
#probably shouldn't use this, like no really, don't use this
#on the main DB. It is included for testing purposes only. maybe taken out later
def deleteAll(tbName):
    str = 'no'
    
#takes a query and then executes it, should be called from any method that wants to execute a query.
#may need to be expanded on in the future.
def _executeQuery(query, dic):
    conn = mysql.connector.connect(**dbConfig)
    try:
        cur = conn.cursor()
        cur.execute(query, dic)
        conn.commit()
    except mysql.connector.Error as err:
        print(err)
    finally:
        conn.close()