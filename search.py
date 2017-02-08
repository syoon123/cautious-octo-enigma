from pymongo import MongoClient
import csv

server = MongoClient("149.89.150.100")
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
            k["students"].append(a._id)
            print "Hello"
        teachers.insert_one(k)
    return

getTeachers(d1)

