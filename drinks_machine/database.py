import mysql.connector


class Database:
    def __init__(self):
        pass
    
    def connect_db(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",               #host hvor databasen ligger      
            user="drinksmaster",           #username (drinksmaster)
            password="Eux20!",       #Password (Eux20!)
            database="drinksdb"        #database_name (Drinksdb)
        )
        self.conn.commit()
        return self.conn

    def max_value(self, conn):
        cursor = self.conn.cursor()
        
        query = "MIN(id) AS min_price FROM recipes"
        cursor.execute(query)

        # Hent resultater
        result = cursor.fetchone()
        max_price = result

        print(f"Sidste drink: {max_price}")

        # Luk forbindelse
        cursor.close()

