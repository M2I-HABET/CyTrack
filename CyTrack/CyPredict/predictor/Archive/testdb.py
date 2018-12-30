'''
Created on Mar 4, 2017

@author: DGXU
'''
from Archive import DBQuerier
from datetime import datetime
from datetime import date
import json

if __name__ == '__main__':
    pass

js = json.dumps({"3":2, "4":4,})

#DBQuerier.insertRow("json", ["data", "date"], [js, '2017-5-8'])
#DBQuerier.insertRowDict("json", {'data':js, 'date':'2017-5-9'})
#DBQuerier.deleteRowDict("testtb", {'name':'jim'}, {'name':"="})
#DBQuerier.deleteRow("testtb", ["name"], ["'lim'"], ["="])

words = DBQuerier.read("testtb", ["name", "age"], "age", "100")
#print(words[0][0])

#DBQuerier.updateDict("testtb", {"age": '7'}, {"id":'2'}, {"id":'='})