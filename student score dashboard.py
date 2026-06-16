import pandas as pd 
import matplotlib.pyplot as plt 
#Create file if it doesn't exist 
try:
    df = pd.read_csv("scores.csv")
except:
    df = pd.DataFrame(columns=["Rollno","Name","Math","Science","English"])
    df_csv("scores.csv")
   #Function to show all marks 
    def show_marks():
        df = pd.read_csv("scores.csv")
        print("\nStudent Marks")
        print(df)
   #Function to add a new student 
        def add_student():
        rollno = int(input("Enter Roll NUMBER:"))
        name = input("Enter Name:")
        math = int(input("Enter Math Mark:"))
        science = int(input("Enter Science Mark:"))
        english = int(input("Enter English Mark:"))
        columns=["RollNo","Name","Math","Science","English"]
        new_data.to_csv("scores.csv")
        mode='a',header='FALSE',index=FALSE
        print("Student Added Successfully!")
    #Function to show top 3 students
        def top_students():
            df = pd.read_csv("scores.csv")
            df["Total"] = df["Math"] + df["Science"] + df["English"]
            top3 = df.sort_values(by="Total",ascending=False)
            print("\nTop 3 Students")
            print(top3[["RollNo","Name","Total"]])
    #Function to show graph    
        def performance_graph():
            df = pd.read.csv("scores.csv")
            df["Total"] = df["Math"] + df["Science"] + df["English"]
            plt.bar(df["Name"],df["Total"])
            plt.xlabel("Student Name")
            plt.ylabel("Total Marks")
            plt.title("Studens Performance")
            plt.show()
    #Main Menu
    while True:
        print("\n----- STUDENT SCORE DASHBOARD -----")
        print("1. Show all marks")
        print("2. Add new student")
        print("3. Show top 3 performance")
        print("4. Show performance graph")
        print("5. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            show_all_marks()
         elif choice == "2":
            add_student()   
         elif choice == "3":
            top_students()
         elif choice == "4":
            performance_graph()
         elif choice == "5":
            exit_()   
            break 
        else:
            print("Invalid choice")   




                
                
            
