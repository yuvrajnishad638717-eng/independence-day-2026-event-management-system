import pandas as pd
import cv2
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "yuvr@j123",
    database = "independance_day"
)

cursor = conn.cursor()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_Frontalface_default.xml")

def add_attendance():
    participant_id = int(input("Enter participant_id: "))
    event_id = int(input("Enter event_id: "))
    
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("camera not working!")
        return
        
        face_detection = 0
    while True:
        ret, frame = camera.read()
        if not ret:
            print("webcam not working!")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=8,
            minSize=(80, 80)
        )
        
        for x, y, w, h in faces:
            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                (0, 255, 0),
                2
            )
        if len(faces) > 0:
            face_detection += 1
            
            cv2.putText(
                frame,
                "face detected",
                (20, 40),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                2
            )
            
        else:
            face_detection = 0
        cv2.imshow("photo_captured", frame)
        
        if face_detection >= 10:
            print("FACE DETECTED SUCCESSFULLY!")
            
            attendance_date = datetime.now().date()
            attendance_status = "present"
            
            query = """
            INSERT INTO attendance(participant_id, event_id, attendance_date, attendance_status)
            values(%s, %s, %s, %s)
            """
            values = (
                participant_id,
                event_id,
                attendance_date,
                attendance_status
            )
            
            cursor.execute(query, values)
            conn.commit()
            print("ATTENDANCE MARKED!")
            break
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("ATTENDANCE NOT MARKED")
            break
    camera.release()
    cv2.destroyAllWindows()
            
def view_attendance():
    df = pd.read_sql("SELECT * FROM attendance", conn)
    print("="*50)
    print("ALL ATTENDANCE")
    print("="*50)
    print(df)
    
def attendance_report():
    attendance_id = int(input("Enter attendance_id: "))
    
    query = """
    SELECT * FROM attendance
    WHERE attendance_id = %s
    """
    cursor.execute(query, (attendance_id,))
    result = cursor.fetchall()
    if result is None:
        print("Record not found!")
    else:
        print("REPORT FOUND")
        for row in result:
            print("="*50)
            print("ATTENDANCE REPORT")
            print("="*50)
            print("Attendance_id: ", row[0])
            print("Participant_id: ", row[1])
            print("event_id: ", row[2])
            print("Attendance_date: ", row[3])
            print("Attendance_status: ", row[4])        
        
def delete_attendance():
    query = """
    DELETE FROM attendance
    """
    cursor.execute(query)
    conn.commit()
    print("DELETED SUCCESSFULLY!")
    
df = pd.read_sql("SELECT * from attendance", conn)
df.to_csv("Attendance.csv", index=False)
file = pd.read_csv("Attendance.csv")
print(file)
       
            