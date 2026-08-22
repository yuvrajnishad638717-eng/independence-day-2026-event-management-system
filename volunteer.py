import numpy as np
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your_password",
    database = "independance_day"
)
cursor = conn.cursor()

def add_volunteer():
    event_id = input("Enter event_id: ")
    volunteer_name = input("Enter volunteer_name: ")
    age = input("Enter volunteer age: ")
    gender = input("Enter volunteer gender: ")
    phone = input("Enter volunteer phone: ")
    role = input("Enter volunteer role: ")
    joining_date = input("Enter volunteer_date YYYY-MM-DD: ")
    
    query = """
    INSERT INTO volunteers(event_id, volunteer_name, age, gender, phone, role, joining_date)
    values(%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        event_id,
        volunteer_name,
        age,
        gender,
        phone,
        role,
        joining_date
    )
    
    cursor.execute(query, values)
    conn.commit()
    print("VOLUNTEERS ADDED SUCCESSFULLY!")
    
def view_volunteer():
    df = pd.read_sql("SELECT * FROM volunteers", conn)
    print(df)

df = pd.read_sql("SELECT * FROM volunteers", conn)
df.to_csv("Volunteer.csv", index=False)
file = pd.read_csv("Volunteer.csv")
print(file)
