import mysql.connector as mc, getpass, rich 
from tabulate import tabulate

#mysql_uname = input("Enter mysql username: ")
#mysql_passw = getpass.getpass("Enter mysql password: ")
connection = mc.connect(host = 'localhost', user = 'root', password = 'root#123')
cursor = connection.cursor()

try:
    cursor.execute("CREATE DATABASE gs")
except:
    print("some error.")
finally:
    cursor.execute("use gs")

def table_creation():
    table_query = "CREATE TABLE IF NOT EXISTS store(serial_number int NOT NULL AUTO_INCREMENT, Item_name varchar(20), purchase_date DATE, mfg_date DATE, expiry_date DATE, qty int, price_per_unit int, PRIMARY KEY(serial_number))"
    cursor.execute(table_query)

try:
    table_creation()
except:
    print('error')

def create():
    #sno = int(input("serial number: "))
    Item_name = input("item name: ")
    prch_date = input("dop yyyy-mm-dd: ")
    mfg_date = input("dom yyyy-mm-dd: ")
    exp_date = input("doe yyyy-mm-dd: ")
    qty = int(input("quantity: "))
    price_per_unit = int(input("price: "))
    insert_query = "INSERT INTO store(Item_name, purchase_date, mfg_date, expiry_date, qty, price_per_unit) VALUES({}, {}, {}, {}, {}, {})".format(Item_name, prch_date, mfg_date, exp_date, qty, price_per_unit)
    cursor.execute(insert_query)
    connection.commit()


def search(sno_to_search):
    search_query = ("select * from store where serial_number = " + sno_to_search)
    cursor.execute(search_query)
    record = cursor.fetchone()
    print(record)


def delete(sno_to_delete):
    delete_query = ("delete from store where serial_number = " + sno_to_delete)
    cursor.execute(delete_query)
    connection.commit()


def update(record_to_update):
    delete(record_to_update)
    create()


print("WELCOME TO STOMAN")
print("===============")

while True:
    try:
        print("==================")
        crud = int(input("Please select:\n\t0. Exit\n\t1. Create\n\t2. Search\n\t3. Update\n\t4. Delete\nchoice: "))
        if crud == 0:
            print("So long..!\n==================")
            connection.close()
            break
        elif crud == 1:
            create()
        elif crud == 2:
            sno_to_search = input("Enter sno of product to search for: ")
            search(sno_to_search)
        elif crud == 3:
            record_to_update = input("Enter name of book to update: ")
            update(record_to_update)
        elif crud == 4:
            sno_to_delete = input("Enter sno of product to delete: ")
            delete(sno_to_delete)
        else:
            print("Invalid choice.")
            print("==================")
    except:
        print("except Invalid choice.")