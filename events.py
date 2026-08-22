import numpy as np
import pandas as pd
from events import *
from participants import *
from volunteer import *
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your_password",
    database = "independance_day"
)

cursor = conn.cursor()
print("DATA SUCCESSFULLY CONNECTED")

def add_event():
    event_name = input("Enter event name: ")
    event_date = input("Enter event date YYYY-MM-DD: ")
    city = input("Enter city name: ")
    state = input("Enter state name: ")
    event_type = input("Enter event type: ")
    capacity = input("Enter event capacity: ")
    budget = int(input("Enter event budget: "))
    status = input("Enter event status: ")
    
    query = """
    INSERT INTO events(event_name, event_date, city, state, event_type, capacity, budget, status)
    VALUES(%s, %s, %s ,%s, %s, %s, %s, %s)
    """
    values = (
        event_name,
        event_date,
        city,
        state,
        event_type,
        capacity,
        budget,
        status
    )
    cursor.execute(query, values)
    conn.commit()
    print("EVENT ADDED SUCCESSFULLY!")
    
def update_event():
    event_id = int(input("Enter event id: "))
    event_name = input("Enter update event_name: ")
    event_date = input("Enter new event date: ")
    city = input("Enter city name: ")
    state = input("Enter state name: ")
    event_type = input("Enter event type: ")
    capacity = input("Enter event capacity: ")
    budget = int(input("Enter event budget: "))
    status = input("Enter event status: ")
    
    query = """
    UPDATE events 
    SET event_name = %s, event_date = %s, city = %s, state = %s, event_type = %s, capacity = %s, budget = %s, status = %s
    WHERE event_id = %s
    """
    values = (
        event_name,
        event_date,
        city,
        state,
        event_type,
        capacity,
        budget,
        status,
        event_id
)
    cursor.execute(query, values)
    conn.commit()
    print("EVENT UPDATED SUCCESSFULLY!")
    
def delete_event():
    event_id = int(input("Enter event_id: "))
    
    query = """
    DELETE FROM events
    WHERE event_id = %s
    """
    cursor.execute(query, (event_id,))
    conn.commit()
        
    print("EVENT DELETED SUCCESSFULLY!")
        
def view_event():
    df = pd.read_sql("SELECT * FROM events", conn)
    print(df)
    
def search_event():
    event_id = int(input("Enter event_id: "))
    
    query = """
    SELECT * FROM events
    WHERE event_id = %s
    """
    cursor.execute(query, (event_id,))
    result = cursor.fetchone()
    if result is None:
        print("Event id not found!")
    else:
        print("Event id found!")
        print(result)  
        conn.commit()  
        
def check_capacity():
    event_id = int(input("Enter event_id: "))
    
    query = """
    SELECT capacity
    FROM events
    WHERE event_id = %s
    """
    cursor.execute(query, (event_id,))
    result = cursor.fetchone()
    if result is None:
        print("CAPACITY NOT FOUND!")
    else:
        print("CAPACITY RESULT FOUND")
        print(result)
        conn.commit()
 
df = pd.read_sql("SELECT * FROM events", conn)
df.to_csv("event.csv")
file = pd.read_csv("event.csv")
print(file)
