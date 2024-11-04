#backend drinks database
import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="172.21.112.152",        # MariaDB server adresse (fx localhost) (mortens pc)
        user="drinkmaster",       # MariaDB brugernavn
        password="Eux20!", # MariaDB kodeord
        database="drinkdb" # Navnet på din database
    )
    cursor = conn.cursor()
    
    # Opret tabeller, hvis de ikke allerede findes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ingredients (
            ingredient_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255),
            quantity_in_stock FLOAT,
            unit VARCHAR(50)
        )
    """)
    # Tilføj andre tabeloprettelser her (Drinks, Recipes, Orders)
    conn.commit()
    return conn
