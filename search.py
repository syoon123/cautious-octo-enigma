from pymongo import MongoClient
import csv

server = MongoClient("149.89.150.100")
db = server.coctoenigma
students = db.students
teachers = db.teachers

f1 = open("teachers.csv")
d1 = csv.DictReader(f1)

def getTeachers(dict):
    for k in dict:
        k["students"] = []
        print k["code"]
        names = students.find({'courses.code' : k["code"] })
        #print names
        for a in names:
            k["students"].append(a._id)
            print "Hello"
        teachers.insert_one(k)
    return

getTeachers(d1)

