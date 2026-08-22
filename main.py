from events import *
from participants import *
from volunteer import *
from attendance import *

while True:
    print("=" * 50)
    print("      INDEPENDENCE DAY 2026")
    print("      EVENT MANAGEMENT SYSTEM")
    print("=" * 50)
    
    print("\n EVENT MENU")
    print("1 Add event")
    print("2 update event")
    print("3 delete event")
    print("4 view event")
    print("5 search event")
    print("6 check capacity")
    
    print("\n PARTICIPANT MENU")
    print("7 add participant")
    print("8 update participant")
    print("9 delete participant")
    print("10 view participant")
    print("11 search participant")
    
    print("\n VOLUNTEERS MENU")
    print("12 add volunteer")
    print("13 view volunteer")
    
    print("\n ATTENDANCE SYSTEM")
    print("14 add attendance")
    print("15 view attendance")
    print("16 attendance report")
    print("17 delete attendance")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_event()
    elif choice == 2:
        update_event()
    elif choice == 3:
        delete_event()
    elif choice == 4:
        view_event()
    elif choice == 5:
        search_event()
    elif choice == 6:
        check_capacity()
    
#participants

    elif choice == 7:
        add_participant()
    elif choice == 8:
        update_participant()
    elif choice == 9:
        delete_participant()
    elif choice == 10:
        view_participant()
    elif choice == 11:
        search_participant()
    
#volunteers
    
    elif choice == 12:
        add_volunteer()
    elif choice == 13:
        view_volunteer()
        
#ATTENDANCES
    elif choice == 14:
        add_attendance()
    elif choice == 15:
        view_attendance()
    elif choice == 16:
        attendance_report()
    elif choice == 17:
        delete_attendance()
    elif choice == 0:
        print("code is ended!")
        break
    else:
        print("\n INVALID CHOICE!")