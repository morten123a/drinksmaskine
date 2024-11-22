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

def default_display (conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ingredients.name, recipes_ingredients.amount, recipes.name FROM recipes_ingredients 
        JOIN ingredients ON ingredients.id = recipes_ingredients.ingredients_id
        JOIN recipes ON recipes.id = recipes_ingredients.recipes_id
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

def seach (conn, drink_name):
    edited_drink_name = drink_name.replace('"', '')
    corrected_drink_name = "%" + edited_drink_name + "%"
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT ingredients.name, recipes_ingredients.amount, recipes.name FROM drinksdb.recipes_ingredients
		LEFT JOIN drinksdb.ingredients ON drinksdb.recipes_ingredients.ingredients_id = drinksdb.ingredients.id
		LEFT JOIN drinksdb.recipes ON drinksdb.recipes_ingredients.recipes_id = drinksdb.recipes.id
		WHERE recipes.name LIKE "{corrected_drink_name}"
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