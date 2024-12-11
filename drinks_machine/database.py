import mysql.connector


class Database:
    def __init__(self):
        pass
    
    def filter_sql_output(self, rows):
        self.rows = rows
        result = {} #laver en tom variable
        for row in self.rows: #segmentere dataen i navnende, i row 2
            result[row[2]] = [] #ligger de forskellige navne ind i variablen

        for row in self.rows: #segmentere dataen for hver navn til den ingrediens
            for recipe_name in result: #laver et nyt loop for at gå igennem alle navnene
                if recipe_name != row[2]:# hvis recipe navnet != navnene, da der ikke skal være navne i returværdien
                    continue
                result[recipe_name].append({"ingredient": row[0], "amount": row[1]}) #sætter dataen pænt op, så det er læseligt
        return  result #resultatet af funktionen

    
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
            
            query = """SELECT ingredients.name, recipes_ingredients.amount, recipes.name FROM drinksdb.recipes_ingredients
		            LEFT JOIN drinksdb.ingredients ON drinksdb.recipes_ingredients.ingredients_id = drinksdb.ingredients.id
                    LEFT JOIN drinksdb.recipes ON drinksdb.recipes_ingredients.recipes_id = drinksdb.recipes.id
                    WHERE ingredients.availability = TRUE  """
            cursor.execute(query)
            max_value = 0
            # Hent resultater
            self.result = cursor.fetchall()
            for row in self.rows: #segmentere dataen i navnende, i row 2
                self.result[row[2]] = []
                max_value += 1
            
            
            print(f"this is the max: {max_value}")
            return max_value

    def current_available_drinks(self):
        with self.conn.cursor() as cursor:
            query= """  SELECT ingredients.name, recipes_ingredients.amount, recipes.name FROM drinksdb.recipes_ingredients
		            LEFT JOIN drinksdb.ingredients ON drinksdb.recipes_ingredients.ingredients_id = drinksdb.ingredients.id
                    LEFT JOIN drinksdb.recipes ON drinksdb.recipes_ingredients.recipes_id = drinksdb.recipes.id
                    WHERE ingredients.availability = TRUE   """
            cursor.execute(query)
            # Hent resultater
            self.rows = cursor.fetchall
            
            return self.filter_sql_output(self.rows)




    def subtract_poured_amount(self):
        #skal hente mængden
        #fjerne den mængde fra databasen
        #sæt flasken til "false" når den er tom
        pass