import mysql.connector
from datetime import datetime



# Databaseforbindelse
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",               #host hvor databasen ligger      
        user="your_username",           #username (drinksmaster)
        password="your_password",       #Password (Eux20!)
        database="drink_machine"        #database_name (Drinksdb)
    )
    cursor = conn.cursor()

    # Opret tabeller, hvis de ikke findes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ingredients (
            ingredient_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255),
            quantity_in_stock FLOAT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Drinks (
            drink_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255),
            description TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Recipes (
            recipe_id INT PRIMARY KEY AUTO_INCREMENT,
            drink_id INT,
            ingredient_id INT,
            quantity FLOAT,
            FOREIGN KEY (drink_id) REFERENCES Drinks(drink_id),
            FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INT PRIMARY KEY AUTO_INCREMENT,
            drink_id INT,
            timestamp DATETIME,
            status VARCHAR(50),
            FOREIGN KEY (drink_id) REFERENCES Drinks(drink_id)
        )
    """)

    conn.commit()
    return conn

# Håndtering af ingredienser
def get_ingredient_stock(conn, ingredient_id):
    cursor = conn.cursor()
    cursor.execute("SELECT quantity_in_stock FROM Ingredients WHERE ingredient_id=%s", (ingredient_id,))
    return cursor.fetchone()[0]

def update_ingredient_stock(conn, ingredient_id, used_quantity):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Ingredients 
        SET quantity_in_stock = quantity_in_stock - %s
        WHERE ingredient_id = %s
    """, (used_quantity, ingredient_id))
    conn.commit()

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
def main():
    conn = connect_db()
    drink_id = add_drink(conn, "Example Drink", "A sample drink description")
    add_ingredient_to_drink(conn, drink_id, 1, 50.0)  # Eksempel: Tilføj en ingrediens
    order_id = create_order(conn, drink_id)
    update_order_status(conn, order_id, "in progress")
    if prepare_drink(conn, drink_id):
        update_order_status(conn, order_id, "complete")
    else:
        update_order_status(conn, order_id, "failed")
    conn.close()

#if __name__ == "__main__":
#    main()
