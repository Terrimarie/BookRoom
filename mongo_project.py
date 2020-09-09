import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "book_room"
COLLECTION_NAME = "books"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.CobbectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option

def get_record():
    print("")
    book_name = input("Enter book name > ")
    author = input("Enter book author name > ")

    try:
        doc = coll.find_one({'book_name': book_name.lower(),'author': author.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error! No results found.")

    return doc

def add_record():
    print("")
    book_name = input("Enter book name > ")
    author = input("Enter book author name > ")
    rating = input("Enter book rating > ")
    publication_date = input("Enter book publication date > ")

    new_doc = {'book_name': book_name.lower(), 'author': author.lower(), 'rating': rating, 'publication_date': publication_date}

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")

def find_record():
    doc = get_record()
    if doc:
        print("")
        # k is for key and v is for value
        for k,v in doc.items():
            if k!= "_id":
                print(k.capitalize() + ": " + v.capitalize())

def edit_record():
    doc = get_record()
    if doc:
        update_doc={}
        print("")
        # k is for key and v is for value
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")

def delete_record():

    doc = get_record()

    if doc:
        print("")
        # k is for key and v is for value
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input("Is this the document you want to delete?\nY OR N > ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document deleted!")
            except: 
                print("Error accessing the database")
            else:
                print("Document not deleted")

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()