from pymongo import MongoClient
from pprint import pprint
import csv

server = MongoClient("127.0.0.1")
db = server.coctoenigma
students = db.students
teachers = db.teachers

d1 = csv.DictReader(open("teachers.csv"))

def getTeachers(dict):
    for k in dict:
        k["students"] = []
        print k["code"]
        names = students.find({'courses.code' : k["code"] })
        #print names
        for a in names:
            k["students"].append(a['id'])
            #pprint(a)
            #pprint(k)
        teachers.insert_one(k)
    return

getTeachers(d1)

