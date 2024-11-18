import mysql.connector
from datetime import datetime



# Databaseforbindelse
def connect_db():
    conn = mysql.connector.connect(
        host="172.21.114.226",               #host hvor databasen ligger      
        user="drinksmaster",           #username (drinksmaster)
        password="Eux20!",       #Password (Eux20!)
        database="drinksdb"        #database_name (Drinksdb)
    )
    conn.commit()
    return conn




# Håndtering af drinks og opskrifter
def add_drink(conn, name, description):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Drinks (name, description) 
        VALUES (%s, %s)
    """, (name, description))
    conn.commit()
    return cursor.lastrowid  # Returnerer drink_id

def add_ingredient_to_drink(conn, drink_id, ingredient_id, quantity):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Recipes (drink_id, ingredient_id, quantity)
        VALUES (%s, %s, %s)
    """, (drink_id, ingredient_id, quantity))
    conn.commit()

def seach (conn, drink_name):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM drinksdb.recipes_ingredients
		LEFT JOIN drinksdb.ingredients ON drinksdb.recipes_ingredients.ingredients_id = drinksdb.ingredients.id
		LEFT JOIN drinksdb.recipes ON drinksdb.recipes_ingredients.recipes_id = drinksdb.recipes.id
		WHERE recipes.name = %s
        """, (drink_name))
    return cursor.fetchall()

def filter(conn, filter, seach_filter):
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
    seach_filter = None
    if (seach_filter != None):
            cursor.execute("""SELECT * FROM drinksdb.recipes_ingredients
		    LEFT JOIN drinksdb.ingredients ON drinksdb.recipes_ingredients.ingredients_id = drinksdb.ingredients.id
		    LEFT JOIN drinksdb.recipes ON drinksdb.recipes_ingredients.recipes_id = drinksdb.recipes.id
		    WHERE ingredients.name IN ({filter_result})
            WHERE recipes.name = %s
             """, (seach_filter))
    return cursor.fetchall()

def get_recipe(conn, drink_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ingredient_id, quantity
        FROM Recipes
        WHERE drink_id=%s
    """, (drink_id,))
    return cursor.fetchall()

# Håndtering af ordrer
def create_order(conn, drink_id):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Orders (drink_id, timestamp, status) 
        VALUES (%s, %s, %s)
    """, (drink_id, datetime.now(), "pending"))
    conn.commit()
    return cursor.lastrowid

def update_order_status(conn, order_id, status):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Orders 
        SET status = %s 
        WHERE order_id = %s
    """, (status, order_id))
    conn.commit()

# Tilberedning af drink
def prepare_drink(conn, drink_id):
    recipe = get_recipe(conn, drink_id)
    
    for ingredient_id, quantity in recipe:
        stock = get_ingredient_stock(conn, ingredient_id)
        
        if stock < quantity:
            print(f"Not enough ingredient {ingredient_id} in stock!")
            return False
        # Kontroller til ventiler/pumper kunne indsættes her
        update_ingredient_stock(conn, ingredient_id, quantity)
    print("Drink is ready!")
    return True

# Hovedfunktion
#def main():
    # conn = connect_db()
    # drink_id = add_drink(conn, "Example Drink", "A sample drink description")
    # add_ingredient_to_drink(conn, drink_id, 1, 50.0)  # Eksempel: Tilføj en ingrediens
    # order_id = create_order(conn, drink_id)
    # update_order_status(conn, order_id, "in progress")
    # if prepare_drink(conn, drink_id):
    #     update_order_status(conn, order_id, "complete")
    # else:
    #     update_order_status(conn, order_id, "failed")
    # conn.close()
conn = connect_db()
print(filter(conn, ['vodka', 'gin']))
#if __name__ == "__main__":
#    main()
