import mysql.connector as mc
options={
        "host": "localhost",
        "user": "root",
        "password": "@Shubham24",
        "database": "shubham"
}

try:
    client = mc.connect(**options)
    print("Connection successful Client:", client)
    cursor = client.cursor()
except Exception as e:
    print("Connection error:", e)
    exit(0)

def showAll():
    query = "SELECT * from user"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

def insert():
    roll = int(input("Enter Roll Number : " ))
    name = input("Enter name : ")
    query = f"INSERT into user value({roll} , '{name}')"

    cursor.execute(query)
    client.commit()

    print("New tupple added !!")
    showAll()

def update():
    roll = int(input("Enter roll : "))
    name = input("Enter new name : ")
    query=f"UPDATE user set name='{name}' where rollNo={roll}"

    cursor.execute(query)
    client.commit()

    showAll()

def delete():
    roll = int(input("Enter roll to be delete : "))
    query=f"DELETE from user where rollNo={roll}"

    cursor.execute(query)
    client.commit()

    showAll()

def search():
    name = input("Enter string to search in name : ")
    query = f"select * from user where name like '%{name}%'"

    cursor.execute(query)
    result = cursor.fetchall()

    print(result)

print("\n\t\t\tLibrary\t\t\t")
print("1. Show all books")
print("2. Add new Book")
print("3. update Book information")
print("4. delete Book information")
print("5. search Book information")

while True:
    ch = int(input("\nEnter option : "))

    if ch == 1:
        print("\n\tShow All\n")
        showAll()

    elif ch == 2:
        print("\n\tInserting\n")
        insert()

    elif ch == 3:
        print("\n\tUpdating\n")
        update()

    elif ch == 4:
        print("\n\tDeleting\n")
        delete()

    elif ch == 5:
        print("\n\tSearching\n")
        search()

    elif ch >= 6:
        client.close()
        print("\nThank you !\n")
        break