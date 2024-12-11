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

    def max_value(self):
        with self.conn.cursor() as cursor:
            
            query = """select MAX(id) AS min_price FROM recipes"""
            cursor.execute(query)

            # Hent resultater
            result = cursor.fetchone()
            max_value = result
            max_value = int(max_value[0])
            print(f"Sidste drink: {max_value}")

            return max_value

