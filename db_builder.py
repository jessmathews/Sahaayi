import sqlite3

connection = sqlite3.connect('database.db')
 
cursor = connection.cursor()
print("Dropping tables!")
cursor.execute("DROP TABLE IF EXISTS ALERTS")
cursor.execute("DROP TABLE IF EXISTS CONTACTS")
 
table1 = """ CREATE TABLE ALERTS (
            Title TEXT NOT NULL,
            Body TEXT NOT NULL,
            Type TEXT
        );"""

table2 = """ CREATE TABLE CONTACTS (
            Email TEXT NOT NULL,
            Phone TEXT NOT NULL,
            Helper INTEGER NOT NULL
            );"""
cursor.execute(table1)
cursor.execute(table2)
 
print("Database built!")
connection.close()