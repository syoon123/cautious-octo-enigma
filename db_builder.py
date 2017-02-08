from pymongo import MongoClient
from pprint import pprint
import csv

server = MongoClient("127.0.0.1")
db = server.coctoenigma
students = db.students

d1 = csv.DictReader(open("peeps.csv"))
d2 = csv.DictReader(open("courses.csv"))

def getStudents(peeps, courses):
    studentList = {}
    for k in peeps:
        k["courses"] = []
        studentList[k["id"]] = k
    for k in courses:
        if k["id"] in studentList:
            studentList[k["id"]]["courses"].append({
                "code": k["code"],
                "mark": k["mark"],
            })
    
    db.students.insert_many(studentList.values())
    return

getStudents(d1, d2)
'''
print students.count()
cursor =  students.find()
for doc in cursor:
    pprint(doc)
'''
