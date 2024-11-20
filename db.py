import mysql.connector
from datetime import datetime

# Databaseforbindelse
def connect_db():
    conn = mysql.connector.connect(
        host="172.21.114.12",               #host hvor databasen ligger      
        user="drinksmaster",           #username (drinksmaster)
        password="Eux20!",       #Password (Eux20!)
        database="drinksdb"        #database_name (Drinksdb)
    )
    conn.commit()
    return conn

def seach (conn, drink_name):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM drinksdb.recipes_ingredients
		LEFT JOIN drinksdb.ingredients ON drinksdb.recipes_ingredients.ingredients_id = drinksdb.ingredients.id
		LEFT JOIN drinksdb.recipes ON drinksdb.recipes_ingredients.recipes_id = drinksdb.recipes.id
		WHERE recipes.name = %s
        """, (drink_name))
    return cursor.fetchall()

def filter(conn, filter):
    cursor = conn.cursor()
    filter_result = ""
    for i, v in enumerate(filter):
        if i+1 == len(filter):
            filter_result += f"'{v}'"
        else:
            filter_result += f"'{v}', "

    cursor.execute(f"""SELECT * FROM drinksdb.recipes_ingredients
		LEFT JOIN drinksdb.ingredients ON drinksdb.recipes_ingredients.ingredients_id = drinksdb.ingredients.id
		LEFT JOIN drinksdb.recipes ON drinksdb.recipes_ingredients.recipes_id = drinksdb.recipes.id
        WHERE ingredients.name IN ({filter_result})
        """)
    return cursor.fetchall()

