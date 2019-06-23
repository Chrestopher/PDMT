import pymysql

db = pymysql.connect("localhost", "root", "root", "pds")

cursor = db.cursor()


# def start_mysql():
#     db = pymysql.connect("localhost", "root", "root", "pds")
#
#     cursor = db.cursor()
#
#     # execute SQL query using execute() method.
#     cursor.execute("SELECT VERSION()")
#
#     # Fetch a single row using fetchone() method.
#     data = cursor.fetchone()
#     print("Database version : %s " % data)
#
#     # disconnect from server
#     db.close()


def get_all_pokemon():
    get_all_pokemon_query = "SELECT name FROM pds"

    cursor.execute(get_all_pokemon_query)
    data = cursor.fetchall()
    print(data)


if __name__ == '__main__':
    get_all_pokemon()
