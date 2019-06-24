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


def get_all_pokemon_column(column):
    get_all_pokemon_query = "SELECT " + column + " FROM pds"

    cursor.execute(get_all_pokemon_query)
    data = list(cursor.fetchall())
    data_list = []
    for item in data:
        if item[0] is not None:
            data_list.append(item[0])
    print(data_list)
    return data_list


def get_all_pokemon_height_weight_graph():
    get_all_pokemon_query = "SELECT weight_kg, height_m, name FROM pds WHERE weight_kg IS NOT NULL"

    cursor.execute(get_all_pokemon_query)
    data = list(cursor.fetchall())
    weight_list = []
    height_list = []
    name_list = []
    for item in data:
        weight_list.append(item[0])
        height_list.append(item[1])
        name_list.append(item[2])

    data_list = [weight_list, height_list, name_list]
    print(data_list)
    return data_list


if __name__ == '__main__':
    get_all_pokemon_height_weight_graph()
