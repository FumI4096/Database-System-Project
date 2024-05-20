import pyodbc as pdb
import customtkinter as ui
from datetime import datetime

ui.set_appearance_mode("dark")
ui.set_default_color_theme("blue")

app = ui.CTk()
app.geometry("600x800")
app.title("File a Leave")

####################
def message():
    try:
        connection = pdb.connect('DRIVER={SQL Server};'+
                                'Server=FX505DY\SQLEXPRESS;'+
                                'Database=Payroll_Management_System;'+
                                'Trusted_Connection=True')
        
        connection.autocommit = True
        cursor = connection.cursor()
        
        query = (f"SELECT ID, FirstName, LastName FROM Registration WHERE ID = {int(enterId.get())}")
        cursor.execute(query)
        proc = ("EXEC spUpdateLeaves @ID = ?, @Message = ?")
        
        result = cursor.fetchone()
        
        message = enterMessage.get("1.0", "end-1c")
        
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
            print("Result from stored procedure:", id)
            cursor.execute(proc, (result[0], f"{message}"))
            messageSuccess.configure(text=f"{first_name} {last_name}\n({date} {time})")
            
        else:
            messageSuccess.configure(text="Enter a valid ID")
        
        messageSuccess.after(6000, lambda: messageSuccess.configure(text=""))
    except pdb.Error as ex:
        print('Connection failed', ex)
        messageSuccess.configure(text="Error Occured")
        messageSuccess.after(6000, lambda: messageSuccess.configure(text=""))

messageSuccess = ui.CTkLabel(app, text="")
messageSuccess.place(relx = 0.33, rely = 0.79)

messageText = ui.CTkLabel(app, text="Enter a Message")
messageText.place(relx = 0.42, rely= 0.14)

enterId = ui.CTkEntry(app, placeholder_text="Enter ID", width=200, height=50, border_width=1, border_color="black")
enterId.place(relx = 0.34, rely = 0.5)

enterMessage = ui.CTkTextbox(app, width=400)
enterMessage.place(relx = 0.167, rely=0.2)

submit = ui.CTkButton(app, text="SUBMIT", fg_color="blue", width=100, height=40, command=message)
submit.place(relx = 0.42, rely = 0.6)

app.mainloop()
