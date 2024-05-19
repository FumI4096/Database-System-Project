import pyodbc as pdb
import customtkinter as ui
from datetime import datetime

ui.set_appearance_mode("dark")
ui.set_default_color_theme("blue")

app = ui.CTk()
app.geometry("600x400")
app.title("Register")

####################
def login():
    try:
        connection = pdb.connect('DRIVER={SQL Server};'+
                                'Server=FX505DY\SQLEXPRESS;'+
                                'Database=Payroll_Management_System;'+
                                'Trusted_Connection=True')
        
        connection.autocommit = True
        cursor = connection.cursor()
        
        query = (f"SELECT ID, FirstName, LastName FROM Registration WHERE ID = {int(enterId.get())}")
        cursor.execute(query)
        proc = ("EXEC spUpdateLogIN @ID = ?")
        
        result = cursor.fetchone()
        
        set = datetime.now()
        M = (set.strftime("%B"))
        D = (set.strftime("%d"))
        Y = (set.strftime("%Y"))
        date = f"{M} {D}, {Y}"
        H = (set.strftime("%I"))
        M = (set.strftime("%M"))
        S = (set.strftime("%S"))
        P = (set.strftime("%p"))
        time = f"{H}:{M}:{S} {P}"

        hello
        if result:
            id, first_name, last_name = result
            print("Result from stored procedure:", id)
            cursor.execute(proc, result[0])
            attendanceOutput.configure(text=f"{first_name} {last_name}\n({date} {time})")
            
        else:
            print("No result returned from stored procedure", result[0])

        # if result:
        #     cond = result[0]
        #     print(cond)
        #     if cond == 1:
        #         attendanceOutput.configure(text="Attendance Done")
        #     elif cond == 0:
        #         attendanceOutput.configure(text="ID not found in LoggingIn")
        #     elif cond == -1:
        #         attendanceOutput.configure(text="ID not found in Registration")
        #     else:
        #         attendanceOutput.configure(text="Unexpected condition value")
        # else:
        #     attendanceOutput.configure(text="No result returned")
        
        attendanceOutput.after(6000, lambda: attendanceOutput.configure(text=""))
    except pdb.Error as ex:
        print('Connection failed', ex)
        attendanceOutput.configure(text="Error Occured")
        attendanceOutput.after(3000, lambda: attendanceOutput.configure(text=""))

attendanceOutput = ui.CTkLabel(app, text="")
attendanceOutput.place(relx = 0.34, rely = 0.6)

enterId = ui.CTkEntry(app, placeholder_text="Enter ID", width=200, height=50, border_width=1, border_color="black")
enterId.place(relx = 0.34, rely = 0.3)

submit = ui.CTkButton(app, text="SUBMIT", fg_color="blue", width=100, height=40, command=login)
submit.place(relx = 0.34, rely = 0.5)

app.mainloop()
