import mysql.connector
import json

class Database:
    def __init__(self):
        pass
    
    def build_recipe_components_dict(self, rows):
        self.rows = rows
        result = {} #laver en tom variable
        for row in self.rows: #segmentere dataen i navnende, i row 2
            result[row[2]] = [] #ligger de forskellige navne ind i variablen

        for row in self.rows: #segmentere dataen for hver navn til den ingrediens
            for recipe_name in result: #laver et nyt loop for at gå igennem alle navnene
                if recipe_name != row[2]:# hvis recipe navnet != navnene, da der ikke skal være navne i returværdien
                    continue
                result[recipe_name].append({"ingredient": row[0], "amount": row[1]}) #sætter dataen pænt op, så det er læseligt
        # print(json.dumps(result))
        # print(json.dumps(result2))
        # print(json.dumps(result2[0]["name"]))
        # print(json.dumps(result2[0]["ingredients"]))
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
            rows = cursor.fetchall()
            max_value = 0
            # Hent resultater

            rows_filtered = self.build_recipe_components_dict(rows)
            for i in rows_filtered:
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
            rows = cursor.fetchall()
            recipe_components = self.build_recipe_components_dict(rows)

            recipe_list = []
            for name in recipe_components:
                recipe_list.append({"name": name, "ingredients": recipe_components[name]})

            # print(json.dumps(recipe_components))
            # print(json.dumps(recipe_list[0]["name"]))
            # print(json.dumps(recipe_list[0]["ingredients"]))

            return recipe_list 


    def get_total_amount(self,input):
        with self.conn.cursor() as cursor:
            query=f"""
                SELECT ingredients.amount FROM ingredients
                WHERE ingredients.name = '{input}';
                """
            cursor.execute(query)
            total_amount = cursor.fetchone()[0]
            print(total_amount)
            return total_amount



    def subtract_poured_amount(self, input, amount):
        with self.conn.cursor() as cursor:
            print(input)
            print(amount)
            total_amount = self.get_total_amount(input) 
            query= f""" 
                UPDATE ingredients
                SET amount = {total_amount - amount}
                WHERE NAME = ' {input} ';   
                """
            print(query)
            cursor.execute(query)

            if self.total_amount >=0 :
                query= f""" 
                    UPDATE ingredients
                    SET availability = 0
                    WHERE NAME = ' {input} ';   
                    """
                cursor.execute(query)
            print("Database succesfully changed")
        # Hent resultater
        #skal hente mængden
        #fjerne den mængde fra databasen
        #sæt flasken til "false" når den er tom
        pass