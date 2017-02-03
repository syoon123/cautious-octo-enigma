from pymongo import MongoClient
import csv

server = MongoClient("149.89.150.100")
db = server.coctoenigma
students = db.students
courses = db.courses

f1 = open("peeps.csv")
f2 = open("courses.csv")
d1 = csv.DictReader(f1)
d2 = csv.DictReader(f2)

def getStudents(dict):
    for k in dict:
        students.insert_one(k)
        print k
    return 

def getCourses(dict):
    for k in dict:
        courses.insert_one(k)
        print k
    return

getStudents(d1)
getCourses(d2)
print students.count()
print courses.count()
