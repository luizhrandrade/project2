import os
import json
import sqlalchemy as db
import pandas as pd
from datetime import datetime

def deleteExistingDatabase():
    myfile = "Notifood.db"
    if os.path.isfile(myfile):
        os.remove(myfile)


def setupDatabase():
    """Creates a database with necessary structure for program"""
    engine = db.create_engine('sqlite:///Notifood.db')
    if len(engine.table_names()) < 2:
        engine.execute( 
            """
                CREATE TABLE food_items(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    purchase_date DATE,
                    expiration_date DATE,
                    item_name VARCHAR(100),
                    item_category VARCHAR(40)
                );
            """
        )
    return engine


def addFoodItem(engine, name, category, purchase_date, expiration_date):
    """Adds a food item to the database"""
    engine.execute(
        f"""
            INSERT INTO food_items(
                purchase_date,
                expiration_date,
                item_name,
                item_category)
            VALUES(
                \'{purchase_date}\',
                \'{expiration_date}\',
                \'{name}\',
                \'{category}\'
            );
        """
    )


def printDatabase(engine, query):
    """Prints the query table from the database"""
    query_result = engine.execute(f"SELECT * FROM {query};").fetchall()
    print(pd.DataFrame(query_result))


def getFoodToExpire(engine):
    """Searches database and returns items set to expire within a week"""
    query = engine.execute(
        """
            SELECT item_name, expiration_date FROM food_items
            WHERE julianday(expiration_date) - julianday('now') < 7;
        """
    )
    print(pd.DataFrame(query))
    

def main():
    # deleteExistingDatabase()
    data = setupDatabase();
    addFoodItem(data, "Broccoli", "Vegetables", "2022-07-5", "2022-07-09")
    addFoodItem(data, "Strawberry", "Fruits", "2022-07-5", "2022-07-11")
    addFoodItem(data, "Lettuce", "Vegetables", "2022-07-5", "2022-07-09")
    addFoodItem(data, "Beef", "Meats", "2022-07-5", "2022-07-11")
    getFoodToExpire(data)
    # printDatabase(data, "food_items")

if __name__ == "__main__":
    main()
