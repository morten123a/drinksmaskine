import mysql.connector

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

def filter_sql_output (rows):
    result = {} #laver en tom variable
    for row in rows: #segmentere dataen i navnende, i row 2
        result[row[2]] = [] #ligger de forskellige navne ind i variablen

    for row in rows: #segmentere dataen for hver navn til den ingrediens
        for recipe_name in result: #laver et nyt loop for at gå igennem alle navnene
            if recipe_name != row[2]:# hvis recipe navnet != navnene, da der ikke skal være navne i returværdien
                continue
            result[recipe_name].append({"ingredient": row[0], "amount": row[1]}) #sætter dataen pænt op, så det er læseligt
    return  result #resultatet af funktionen

def array_to_sql_array(array): #konvertere et almindeligt array til et array man kan bruge i database query's
    result = ""
    for i, v in enumerate(array): #laver en "for" løkke med nogle tomme værdier og vores array
        if i+1 == len(array): #hvis vores tomme værdi er 1, skal den tilføje det til variablen
            result += f"'{v}'"
        else: # hvis den er mere end 1 skal den gøre tilføje et komma ekstra, på grund af query
            result += f"'{v}', "
    return result

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
    return filter_sql_output(rows)

def get_recipe_names_with_ingredients(conn, ingredients): #hente opksrift navne med ingredienser
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT recipes.id FROM ingredients JOIN recipes_ingredients ON recipes_ingredients.ingredients_id = ingredients.id 
        AND ingredients.name IN ({array_to_sql_array(ingredients)})
        JOIN recipes ON recipes.id = recipes_ingredients.recipes_id
        """) # spørger databasen efter opskrift navne med vores array af filtre, som indeholder ingredienser 
    return list(map(lambda v: v[0], cursor.fetchall())) #konvertere fra en "tuple" til et almindeligt array

def get_recipes_by_included_ingredients(conn, included_ingredients): #modtager request fra "server.py"
    cursor = conn.cursor()
    recipe_ids = get_recipe_names_with_ingredients(conn,included_ingredients) #finder alle drinks med brugeres filter i sig
    cursor.execute(f"""
        SELECT ingredients.name, recipes_ingredients.amount, recipes.name FROM recipes_ingredients 
        JOIN ingredients ON ingredients.id = recipes_ingredients.ingredients_id
        JOIN recipes ON recipes.id = recipes_ingredients.recipes_id
        WHERE recipes_ingredients.recipes_id IN ({array_to_sql_array(recipe_ids)})
        """) #henter hele drinken, som havde den forespurgte ingrediens
    rows = cursor.fetchall()
    return filter_sql_output(rows)
