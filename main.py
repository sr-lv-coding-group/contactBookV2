import os
import sqlite3



####################
# DATABASE FUNCTIONS
####################

def select(cursor, select_statement):
    result = cursor.execute(select_statement)
    return result


def insert(cursor, insert_statement):
    result = cursor.execute(insert_statement)
    return result


def update(cursor, update_statement):
    result = cursor.execute(update_statement
    return result


def delete(cursor, delete_statement):
    result = cursor.execute(delete_statement)
    return result


def initialize_db(db):
    print(">>> initialize db")
    print("checking supplied database...")
    while(not isinstance(db, dict)):
        print("\tdatabase was not supplied.\n\tplease select another database to initialize or choose to create a new database.")
        database_names = [f for f in os.listdir('.') if ((os.path.isfile(f)) and (os.path.splitext(f)[1] == ".db"))] 
        if (database_nanmes):
            print("\tdatabases found in '.' directory:")
            for db_name in database_names:
                print(f"\t\t{db_name}\n")
        else:
            print("\tunable to locate database (.db) in directory.\n\tplease select a different directory or choose to create a new database.")
            db=default_db
    try:
        assert isinstance(db, dict), "bad db, not dictionary"
        assert os.path.exists(db['filepath']), "bad filepath, does not exist"
        print("\tconfirmed, supplied database file is located")
    except (AssertionError):
        print(f"\tunsuccessful, supplied database file was not located")
    conn = sqlite3.connect(db['filepath'])
    cur = conn.cursor()
    cur.execute(db['droptable_statement'])
    cur.execute(db['createtable_statement'])
    cur.execute(db['initial_insert_statement'])
    conn.commit()
    return conn



####################
# HELPER FUNCTIONS
####################

def column_width_text(value):
    return str(value).ljust(20)


def print_contact_records(cur):
    result = cur.execute("SELECT * FROM CONTACTS;")
    column_names = [column_width_text(description[0]) for description in result.description]
    print(">>> contacts")
    print(f"\t|{column_names[0]}|{column_names[1]}|{column_names[2]}|{column_names[3]}|{column_names[4]}")
    records = result.fetchall()
    if (not records):
        print("\t   NO RECORDS FOUND   ")
    else:
        for record in records:
            record = [column_width_text(value) for value in record] 
            print(f"\t {record[0]} {record[1]} {record[2]} {record[3]} {record[4]}")
    print("\n\n")

    
def prompt_menu(options):
# Function to print menu options
# Should be moved to Cli.py file
    print("\n\n")
    print(">>> menu")
    for option_id, option in options.items():
        print(f"\t{option_id}: {option['desc']}")
    return input(">>> Enter menu option:\n>>> ")



####################
# MAIN
####################
                            
def main():
    DIRECTORY="."
    DBNAME="contacts.db"
    FILEPATH=os.path.join(DIRECTORY, DBNAME)
    TABLENAME="CONTACTS"
    COLUMNNAMES="name,age,phonenumber,location"
    DROPTABLE_STATEMENT=f"DROP TABLE {TABLENAME}" 
    CREATETABLE_STATEMENT=f"CREATE TABLE IF NOT EXISTS {TABLENAME} (contactid INTEGER PRIMARY KEY ASC,\
                                                      name TEXT,\
                                                      age INTEGER,\
                                                      phonenumber INTEGER,\
                                                      location TEXT);"
    INITIAL_INSERT_STATEMENT=f"INSERT INTO {TABLENAME} ({COLUMNNAMES}) "+\
        "VALUES " +\
        "('Daniel', 35, 5555551212, 'Las Vegas'), "+\
        "('Dennis', 27, 1234567890, 'New York'), "+\
        "('Keegan', 39, 4569876543, 'New York'), "+\
        "('Neil', 58, 5551112222, 'New York'), "+\
        "('Matt', 32, 1233334444, 'New York'), "+\
        "('Alice', 25, 1234567890, 'New York'), "+\
        "('Heather', 50, 5557778888, 'New York'), "+\
        "('John', 21, 1239990000, 'New York'), "+\
        "('Amanda', 36, 4562223333, 'New York'), "+\
        "('Zach', 22, 5554445555, 'New York');"
    SELECT_STATEMENT=f"SELECT {COLUMNNAMES} FROM {TABLENAME};"
    INSERT_STATEMENT=f"INSERT INTO {TABLENAME} ({COLUMNNAMES}) VALUES ('Gene', 94, 3456789234, 'San Bernadino');"
    UPDATE_STATEMENT=f"UPDATE {TABLENAME} "+\
        "SET name = 'Brandon',"+\
            "age = 43,"+\
            "phonenumber = 5459891123,"+\
            "location = 'Las Vegas' "+\
        "WHERE name = 'Gene';"
    DELETE_STATEMENT=f"DELETE FROM {TABLENAME} WHERE name='Brandon';"
    default_db= {
        'directory': DIRECTORY,
        'name': DBNAME,
        'filepath': FILEPATH,
        'droptable_statement' : DROPTABLE_STATEMENT,
        'createtable_statement' : CREATETABLE_STATEMENT,
        'initial_insert_statement' : INITIAL_INSERT_STATEMENT,
        'select_statement' : SELECT_STATEMENT,
        'insert_statement' : INSERT_STATEMENT,
        'update_statement' : UPDATE_STATEMENT,
        'delete_statement' : DELETE_STATEMENT
    }
    menu = {
        0: {"func": exit, "sql_statement":None, "desc": "Exit"},
        1: {"func": select,"sql_statement":default_db["select_statement"], "desc": "Select"},
        2: {"func": insert,"sql_statement":default_db["insert_statement"], "desc": "Insert"},
        3: {"func": update,"sql_statement":default_db["update_statement"], "desc": "Update"},
        4: {"func": delete,"sql_statement":default_db["delete_statement"], "desc": "Delete"},
    }
    conn = initialize_db(default_db)
    choice = None

    while(choice != 0):
        print_contact_records(conn.cursor())
        user_input = prompt_menu(menu) 
        choice = int(user_input or 0)
        print("\tuser selected... \'" + user_input + "\'")
        #os.system('cls' if os.name == 'nt' else 'clear')

        try:
            if ((choice <= 0) or (choice >= len(menu))):
                raise ValueError(f'invalid input:, {choice}')
            else:
                menu[choice]["func"](conn.cursor(), menu[choice]["sql_statement"])
        except ValueError as ve:
            print(f">>> invalid input. Please select from the available options. {ve}")

    print(">>> closing connection....")
    try: 
        conn.close()
        print("\tsuccess, closed connection.")
    except e:
        print("\tfailure, connection closed with error" \
            "\n>>> error\n" + e)
    print(">>> exiting...")


if __name__ == "__main__":
    main()
