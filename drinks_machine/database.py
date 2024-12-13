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
            
            self.query = """SELECT 
                    i.name AS ingredient_name, 
                    ri.amount AS amount, 
                    r.name AS recipe_name
                FROM 
                    recipes r
                LEFT JOIN 
                    recipes_ingredients ri ON r.id = ri.recipes_id
                LEFT JOIN 
                    ingredients i ON ri.ingredients_id = i.id
                WHERE 
                    i.availability = TRUE
                AND 
                    r.id IN (
                        SELECT 
                            ri2.recipes_id
                        FROM 
                            recipes_ingredients ri2
                        JOIN 
                            ingredients i2 ON ri2.ingredients_id = i2.id
                        WHERE 
                            i2.availability = TRUE
                        GROUP BY 
                            ri2.recipes_id
                        HAVING 
                            COUNT(ri2.ingredients_id) = (
                                SELECT COUNT(ri3.ingredients_id)
                                FROM recipes_ingredients ri3
                                WHERE ri3.recipes_id = ri2.recipes_id
                            )
                    )
                ORDER BY 
                    r.name, i.name;

                """
            cursor.execute(self.query)
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
            cursor.execute(self.query)
            # Hent resultater
            rows = cursor.fetchall()
            recipe_components = self.build_recipe_components_dict(rows)

            recipe_list = []
            for name in recipe_components:
                recipe_list.append({"name": name, "ingredients": recipe_components[name]})
            return recipe_list 


    def get_total_amount(self,input):
        with self.conn.cursor() as cursor:
            query=f"""
                SELECT ingredients.amount FROM ingredients
                WHERE ingredients.name = '{input}';
                """
            cursor.execute(query)
            total_amount = cursor.fetchone()[0]
            return total_amount



    def subtract_poured_amount(self, ingredient_name, amount):
        with self.conn.cursor() as cursor:
            total_amount = self.get_total_amount(ingredient_name) 
            query= f""" 
                UPDATE ingredients
                SET amount = {total_amount - amount}
                WHERE NAME = '{ingredient_name}';   
                """
            cursor.execute(query)
            self.conn.commit()

            if total_amount <=0 :
                query= f""" 
                    UPDATE ingredients
                    SET availability = 0
                    WHERE NAME = '{ingredient_name}';   
                    """
                cursor.execute(query)
                self.conn.commit()
            print("Database succesfully changed")
        # Hent resultater
        #skal hente mængden
        #fjerne den mængde fra databasen
        #sæt flasken til "false" når den er tom
        pass