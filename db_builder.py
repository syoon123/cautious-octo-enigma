from pymongo import MongoClient
import csv

server = MongoClient("149.89.150.100")
db = server.coctoenigma
students = db.students
courses = db.courses

d1 = csv.DictReader(open("peeps.csv"))
d2 = csv.DictReader(open("courses.csv"))

def getStudents(peeps, courses):
    studentList = {}
    for k in peeps:
        studentList[k["id"]] = {
            "name": k["name"],
            "age": k["age"],
            "id": k["id"],
            "courses": []
        }
    for k in courses:
        if k["id"] in studentList:
            studentList[k["id"]]["courses"].append({
                "code": k["code"],
                "mark": k["mark"],
            })
    
    db.students.insert_many(studentList.values())
    return

getStudents(d1, d2)
print students.count()
print courses.count()
