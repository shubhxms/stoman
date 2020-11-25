import mysql.connector as mc

connection = mc.connect(host = 'localhost', user = 'root', password = 'root#123')
cursor = connection.cursor()

try:
    cursor.execute("CREATE DATABASE gs")
except:
    print("some error.")

def table_creation():
    table_query = "CREATE TABLE 'store' (serial_number int(10) NOT NULL, Item_name varchar(20), purchase_date date, mfg_date date, expiry_date date, qty int(20), price_per_unit int(20))"
    cursor.execute(table_query)

def create():
    s_no = int(input("serial number: "))
    Item_name = input("item name: ")
    prch_date = input("dop yyyy-mm-dd: ")
    mfg_date = input("dom yyyy-mm-dd: ")
    exp_date = input("doe yyyy-mm-dd: ")
    qty = int(input("quantity: "))
    price_per_unit = int(input("price: "))
    insert_query = "INSERT INTO store (serial_number, Item_name, purchase_date, mfg_date, expiry_date, qty, price_per_unit) VALUES ({}, {}, {}, {}, {}, {}, {})".format(sno, Item_name, prch_date, mfg_date, exp_date, qty, price_per_unit)
    cursor.execute(insert_query)

def search(record_to_search):
    pass

def update(record_to_update):
    pass

def delete(record_to_delete):_number}, {Item_name}, {purchase_date}, {mfg_date}, {expiry_date}, {qty}, {price_per_unit}).format(sno, Item_name, 
    pass

print("WELCOME TO STOMAN")
print("===============")
while True:
    try:
        print("==================")
        crud = int(input("Please select:\n\t0. Exit\n\t1. Create\n\t2. Search\n\t3. Update\n\t4. Delete\nchoice: "))
        if crud == 0:
            print("So long..!\n==================")
            break
        elif crud == 1:
            create()
        elif crud == 2:
            record_to_search = input("Enter name of book to search for: ")
            search(record_to_search)
        elif crud == 3:
            record_to_update = input("Enter name of book to update: ")
            update(record_to_update)
        elif crud == 4:
            record_to_delete = input("Enter name of book to delete: ")
            delete(record_to_delete)
        else:
            print("Invalid choice.")
            print("==================")
    except:
        print("Invalid choice.")