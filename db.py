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
    edited_drink_name = drink_name.replace('"', '') #fjerner "" så det passer med syntaksen til databasen
    cursor = conn.cursor() #sætter vores database forbindelse til at vi kan kører ting igennem den
    cursor.execute(f"""
        SELECT ingredients.name, recipes_ingredients.amount, recipes.name FROM drinksdb.recipes_ingredients
		LEFT JOIN drinksdb.ingredients ON drinksdb.recipes_ingredients.ingredients_id = drinksdb.ingredients.id
		LEFT JOIN drinksdb.recipes ON drinksdb.recipes_ingredients.recipes_id = drinksdb.recipes.id
		WHERE recipes.name LIKE "%{edited_drink_name}%"
        """) # sender en query til databasen med det søgte navn
    rows = cursor.fetchall() #henter alt dataen fra query'en
    result = {} #laver en tom variable

    for row in rows: #segmentere dataen i navnende, i row 2
        result[row[2]] = [] #ligger de forskellige navne ind i variablen

    for row in rows: #segmentere dataen for hver navn til den ingredienser
        for recipe_name in result: #
            if recipe_name != row[2]:
                continue
            result[recipe_name].append({"ingredient": row[0], "amount": row[1]})
    return  result


def array_to_sql_array(array):
    result = ""
    for i, v in enumerate(array):
        if i+1 == len(array):
            result += f"'{v}'"
        else:
            result += f"'{v}', "
    return result

def get_recipe_names_with_ingredients(conn, ingredients):
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT recipes.id FROM ingredients JOIN recipes_ingredients ON recipes_ingredients.ingredients_id = ingredients.id 
        AND ingredients.name IN ({array_to_sql_array(ingredients)})
        JOIN recipes ON recipes.id = recipes_ingredients.recipes_id
        """)
    return list(map(lambda v: v[0], cursor.fetchall()))

def get_recipes_by_included_ingredients(conn, included_ingredients):
    cursor = conn.cursor()
    recipe_ids = get_recipe_names_with_ingredients(conn,included_ingredients)
    cursor.execute(f"""
        SELECT ingredients.name, recipes_ingredients.amount, recipes.name FROM recipes_ingredients 
        JOIN ingredients ON ingredients.id = recipes_ingredients.ingredients_id
        JOIN recipes ON recipes.id = recipes_ingredients.recipes_id
        WHERE recipes_ingredients.recipes_id IN ({array_to_sql_array(recipe_ids)})
        """)
    rows = cursor.fetchall()
    result = {}

    for row in rows:
        result[row[2]] = []

    for row in rows:
        for recipe_name in result:
            if recipe_name != row[2]:
                continue
            result[recipe_name].append({"ingredient": row[0], "amount": row[1]})
    
    return  result