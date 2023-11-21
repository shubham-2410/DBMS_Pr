from pymongo.mongo_client import MongoClient

url = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.2"

try:
    client = MongoClient(url)
    client.admin.command('ping')
    print("Connection Successfull")
except Exception as e:
    print("Connection Error : " , e)

dbs = client.list_database_names()
print(dbs)

db_name = input("Select db to use : ")
db = client[db_name]

collections = db.list_collection_names()
print(collections)

col_name = input("Select collection to use : ")
collection = db[col_name]

def showAll():
    docs = collection.find({})
    for doc in docs:
        print(doc)

def insert():
    name= input("Enter name : ")
    roll = int(input("Enter roll number : "))
    subject = input("Enter Subject : ")
    marks = int(input("Enter Marks : "))
    
    doc={
        'name':name,
        'rno':roll,
        'subject':subject,
        'marks':marks
    }

    collection.insert_one(doc)

def update():
    roll = int(input('Enter roll : '))
    subject = input("Enter subject : ")
    marks = int(input("Enter new marks : "))

    findDoc={
        'rno' :roll,
        'subject':subject
    }

    updateDoc={
        '$set':{
            'marks':marks
        }
    }

    collection.update_one(findDoc , updateDoc)
    # showAll()

def remove():
    roll=int(input("Enter roll no : "))
    name=input("Enter name : ")

    doc ={
        'rno':roll,
        'name':name
    }

    collection.delete_one(doc)


showAll()
# insert()
# showAll()
# update()
# showAll()

remove()
showAll()