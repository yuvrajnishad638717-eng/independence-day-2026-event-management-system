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
print("PRINT DATA SUCCESSFULLY CONNECTED")

def add_participant():
    event_id  =int(input("Enter event_id: "))
    participant_name = input("Enter participant_name: ")
    age = input("Enter participant age: ")
    gender = input("Enter participant gender: ")
    phone = input("Enter participant number: ")
    email = input("Enter participant email: ")
    registration_date = input("Enter registration date YYYY-MM-DD: ")
    
    query = """
    INSERT INTO participants(event_id, participant_name, age, gender, phone, email, registration_date)
    values(%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        event_id,
        participant_name, 
        age,
        gender,
        phone,
        email,
        registration_date
    )
    
    cursor.execute(query, values)
    conn.commit()
    print("data successfully added")

def update_participant():
    participant_id = int(input("Enter participant_id: "))
    participant_name = input("Enter participant_name: ")
    age = input("Enter participant age: ")
    gender = input("Enter participant gender: ")
    phone = input("Enter participant phone number: ")
    email = input("Enter email: ")
    registration_date = input("Enter registration_date YYYY-MM-DD: ")
    
    query = """
    UPDATE participants
    SET participant_name = %s,
    age = %s,
    gender  =%s,
    phone = %s,
    email  =%s,
    registration_date = %s
    WHERE participant_id = %s
    """
    values = (
        participant_name,
        age,
        gender,
        phone,
        email,
        registration_date,
        participant_id
    )
    cursor.execute(query, values)
    conn.commit()
    print("DATA SUCCESSFULLY UPDATED")
    
def delete_participant():
    participant_id = int(input("Enter participant_id: "))
    
    query = """
    DELETE FROM participants
    WHERE participant_id = %s
    """
    cursor.execute(query, (participant_id,))
    result = cursor.fetchone()
    if result is None:
        print("ID NOT FOUND!")
    else:
        print("DELETED SUCCESSFULLY!")
        print(result)
    
def view_participant():
    df = pd.read_sql("SELECT * FROM participants", conn)
    print(df)
    
def search_participant():
    participant_id = int(input("Enter participant_id: "))
    query = """
    SELECT * FROM participants
    WHERE participant_id  = %s
    """
    cursor.execute(query, (participant_id,))
    result = cursor.fetchone()
    if result is None:
        print("\n ID NOT FOUND!")
    else:
        print("ID FOUND SUCCESSFULLY!")
        print(result)
 
df = pd.read_sql("SELECT * FROM participants", conn)
df.to_csv("Participant.csv", index=False)
file = pd.read_csv("participant.csv")
print(file)
