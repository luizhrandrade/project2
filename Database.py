import os
import json
import sqlalchemy as db
import pandas as pd
from datetime import datetime

def deleteExistingDatabase():
    myfile = "food_saver.db"
    if os.path.isfile(myfile):
        os.remove(myfile)


def setupDatabase():
    """Creates a database with necessary structure for program"""
    engine = db.create_engine('sqlite:///food_saver.db')
    engine.execute( "CREATE TABLE food_items(" + 
                    " id INTEGER PRIMARY KEY AUTOINCREMENT," + 
                    " purchase_date DATE," + 
                    " expiration_date DATE," + 
                    " item_name VARCHAR(100)," + 
                    " item_category VARCHAR(40));")
    return engine


def addFoodItem(engine, name, category, purchase_date, expiration_date):
    """Adds a food item to the database"""
    time_difference =   (datetime.strptime(expiration_date, '%Y-%m-%d') - 
                        datetime.strptime(purchase_date, '%Y-%m-%d')).days
    engine.execute( "INSERT INTO food_items(purchase_date, " +
                    "expiration_date, item_name, item_category) " + 
                    f"VALUES(\'{purchase_date}\', \'{expiration_date}\'," +
                    f"\"{name}\",\"{category}\");")


# def sortTable(engine, table_name):
#     """Sorts the table based on food duration"""
#     engine.execute( f"SELECT duration " +
#                     f"FROM {table_name} " +
#                     "ORDER BY duration DESC;")


def printDatabase(engine, query):
    """Prints the query table from the database"""
    query_result = engine.execute(f"SELECT * FROM {query};").fetchall()
    print(pd.DataFrame(query_result))


def getFoodToExpire():
    current_date = datetime.datetime.now()
    


def main():
    deleteExistingDatabase()
    data = setupDatabase();
    addFoodItem(data, "Broccoli", "Vegetables", "2020-04-12", "2020-05-10")
    addFoodItem(data, "Strawberry", "Fruits", "2020-08-12", "2020-08-20")
    # sortTable(data, "food_items")
    printDatabase(data, "food_items")

if __name__ == "__main__":
    main()
