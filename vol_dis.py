import pyodbc as pdb
import customtkinter as ui
from datetime import datetime

ui.set_appearance_mode("dark")
ui.set_default_color_theme("blue")

app = ui.CTk()
app.geometry("600x400")
app.title("Voluntary Distribution")

####################
def cash():
    try:
        connection = pdb.connect('DRIVER={SQL Server};'+
                                'Server=FX505DY\SQLEXPRESS;'+
                                'Database=Payroll_Management_System;'+
                                'Trusted_Connection=True')
        
        connection.autocommit = True
        cursor = connection.cursor()
        
        query = (f"SELECT ID, FirstName, LastName FROM Registration WHERE ID = {int(enterId.get())}")
        cursor.execute(query)
        proc = ("EXEC spVoluntaryDist @ID = ?, @Cash = ?")
        
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
        
        if result:
            id, first_name, last_name = result
            cursor.execute(proc, (result[0], f"{float(enterCash.get())}"))
            cashWork.configure(text=f"{first_name} {last_name}\n({date} {time})")
        else:
            cashWork.configure(text="Enter a valid ID")
        
        cashWork.after(6000, lambda: cashWork.configure(text=""))
    except pdb.Error as ex:
        print('Connection failed', ex)
        cashWork.configure(text="Error Occured")
        cashWork.after(6000, lambda: cashWork.configure(text=""))

cashWork = ui.CTkLabel(app, text="")
cashWork.place(relx = 0.33, rely = 0.79)

enterCash = ui.CTkEntry(app, placeholder_text="Enter Cash", width=200, height=50, border_width=1, border_color="black")
enterCash.place(relx = 0.34, rely = 0.3)

enterId = ui.CTkEntry(app, placeholder_text="Enter ID", width=200, height=50, border_width=1, border_color="black")
enterId.place(relx = 0.34, rely = 0.5)


submit = ui.CTkButton(app, text="SUBMIT", fg_color="blue", width=100, height=40, command=cash)
submit.place(relx = 0.42, rely = 0.7)

app.mainloop()
