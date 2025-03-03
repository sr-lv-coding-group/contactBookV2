import os
import sqlite3


# def connect_db(directory=".",db_name=None):
#     if (not db_name):
# db_name = input(f">>> Write the name of the database you wish to connect: ")
#    try:
#        file_path = os.path.join(directory, db_name)
#        # Check if the file exists at the specified path.
#        # assert(os.path.exists(file_path), )
#        conn = sqlite3.connect(db_name)
#        print(f"\tSuccess! Able to connect to db: {db_name}")
#        return conn.cursor()
#    except (AssertionError):
#       print(f"\tFailure! Unable to create/connect to db: {db_name}"/
#              + "\n\n" + NameError)
#    return None
#
#
#def execute(conn=None, sql_statement=None):
#    return 0
#
#
#def select(cursor=CUR, select_statement=DEFAULT):
#    result = cursor.execute(select_statement)
#    return result
#
#
#def insert(cursor=CUR, insert_statement=DEFAULT):
#    result = cursor.execute(insert_statement)
#    return result
#
#
#def update(cursor=CUR, update_statement=DEFAULT):
#    result = cursor.execute(update_statement)
#    return result
#
#
#def delete(cursor=CUR, delete_statement=DEFAULT):
#    result = cursor.execute(delete_statement)
#    return result
#
#
#def commit(conn=CONN):
#    result = conn.commit()
#    return result
#
#
#def print_contact_records(records=None):
#    print("+++ Contacts +++")
#    for record in records:
#        print(f"Id:{record[0]}\tName: {record[1]},\tAge: {record[2]}\tPhone Number: {record[3]}\tLocation: {record[4]}")
#    print("\n")
#
#
#def print_menu_options(options):
#    print("\n\n")
#    for option_id, option in options.items():
#        print(f"\t{option_id}: {option['desc']}")
#




def initialize_db(db=None):
    print(isinstance(db, dict))
    print("=== initialize db ===")
    print("checking supplied database...")
    while(db==None):
        print("\tdatabase was not supplied.\n\tplease select another database to initialize or choose to create a new database.")
#        database_names = [f for f in os.listdir('.') if ((os.path.isfile(f)) and (os.path.splitext(f)[1] == ".db"))] 
        for f in os.listdir('.'):
            if ((os.path.isfile(f)) and (os.path.splitext(f)[1] == ".db")):
                print(database_names)

        if (database_nanmes):
            print("\tdatabases found in '.' directory:")
            for db_name in database_names:
                print(f"\t\t{db_name}\n")
        else:
            print("\tunable to locate database (.db) in directory.\n\tplease select a different directory or choose to create a new database.")
            db=default_db
    print("\tconfirmed, supplied database file is located")
    try:
        assert(os.path.exists(db['filepath'], ))
    except (AssertionError):
        print(f"\tFailure! Unable to create/connect to db.")
    
        conn = sqlite3.connect(default_db['filepath'])
        


if __name__ == "__main__":
    default_db= {
        'directory': ".",
        'name': "contacts.db",
        'filepath': './toDELETE_contacts.db',
        'insert_statement' : "INSERT INTO CONTACTS (contact_id, name, age, phonenumber, location) VALUES ('0', 'Daniel', 35, 5555551212, 'Las Vegas'),('2', 'Dennis', 27, 1234567890, 'New York'),('3', 'Keegan', 39, 4569876543, 'New York'), ('4', 'Neil', 58, 5551112222, 'New York'), ('5', 'Matt', 32, 1233334444, 'New York'), ('6', 'Alice', 25, 1234567890, 'New York'),('7', 'Heather', 50, 5557778888, 'New York'), ('8', 'John', 21, 1239990000, 'New York'), ('9', 'Amanda', 36, 4562223333, 'New York'), ('10', 'Zach', 22, 5554445555, 'New York');"
    }

    menu = {
        0: {"func": exit, "desc": "Exit"},
#        1: {"func": select, "desc": "Select"},
#        2: {"func": insert, "desc": "Insert"},
#        3: {"func": update, "desc": "Update"},
#        4: {"func": delete, "desc": "Delete"},
    }
    
    initialize_db(default_db)
    os.system('cls' if os.name == 'nt' else 'clear')



    print_contact_records(column_names='(*)', )
#    print_menu_options(menu)
#    build_sql_cmd(menu[]['desc'] )


def menu_loop2():
        try:
        # Check if the file exists at the specified path.
            assert(os.path.exists(DB),)
            conn = sqlite3.connect(DB)
            cur = conn.cursor()
            while(menu):
                result = cur.execute("SELECT * FROM CONTACTS")
                records = result.fetchall()
                print_contact_records(records)
                print_menu_options(menu)
                user_input = input(f">>> Enter your choice from 0-{len(menu)-1}: ")
                print("\tUser selected: " + user_input)

                try:
                    user_choice = int(user_input)
                    if ((user_choice < 0) or (user_choice >= len(menu))):
                        raise ValueError('*** Invalid input:', user_choice)
                    elif (user_choice == 0):
                        break
                    if callable(menu[user_choice]["func"]):
                        sql_statement = None
                        while(not sql_statement):
                            sql_statement = input(f">>> Enter SQL {menu[user_choice]['desc']} statement: ")
                            results = menu[user_choice]["func"](cur, sql_statement)
                except ValueError as ve:
                    print(f"*** Invalid input. Please select from the available options. {ve}\n\n")      
        except (AssertionError):
            print(f"\tFailure! Unable to create/connect to db: {DBNAME}\n")    

#sql_statement = "CREATE TABLE CONTACTS(contact_id INTEGER PRIMARY KEY ASC, name, age, phonenumber, location);"

#sql_statement = "INSERT INTO CONTACTS (name, age, phonenumber, location) VALUES ('Gene', 94, 3456789234, 'San Bernadino');"

