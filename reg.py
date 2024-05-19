import pyodbc as pdb
import customtkinter as ui


#db connection
def insert():
    try:
        global ids
        
        connection = pdb.connect('DRIVER={SQL Server};'+
                                'Server=FX505DY\SQLEXPRESS;'+
                                'Database=Payroll_Management_System;'+
                                'Trusted_Connection=True')
        
        connection.autocommit = True
        cursor = connection.cursor()
        
        query = ("EXEC spInsertUsersReg @ID = ?, @FirstName = ?, @LastName = ?, @Age = ?, @Bday = ?, @Role = ?, @Dep = ?")
        
        cursor.execute(query, (
            int(idenNumber.get()), 
            firstName.get(), 
            lastName.get(), 
            int(age.get()), 
            birthday.get(), 
            int(dropDown.get()[0]),
            int(department.get()[0])
        ))
        
        
        form_success.configure(text="Form Submitted")
        form_success.after(2000, lambda: form_success.configure(text=""))
    except pdb.Error as ex:
        print('Connection failed', ex)
        form_success.configure(text="Error Occured")
        form_success.after(2000, lambda: form_success.configure(text=""))


####################################################################

#variables, lists
positions = {
    "1 - Employee": 1,
    "2 - IT Administrator": 2, 
    "3 - Network Administrator": 3, 
    "4 - Research Scientist": 4,
    "5 - Research Manager": 5, 
    "6 - Financial Officer": 6, 
    "7 - Accountant": 7,
    "8 - Account Executive": 8, 
    "9 - Chief Marketing Officer": 9, 
    "10 - Chief Executive Officer": 10
}

departments = {
    "1 - Company Administrative Function": 1,
    "2 - Administration" : 2,
    "3 - Human Resource Department" : 3,
    "4 - Finance and Accounts Department" : 4,
    "5 - Marketing Department" : 5,
    "6 - Sales" : 6,
    "7 - IT Department" : 7,
    "8 - Research and Development" : 8,
    "9 - Customer Service Department" : 9,
    "10 - Legal Department" : 10
    
}

position_nums = list(positions.keys())
dep_nums = list(departments.keys())

#functions
def positions_option(choice):
    value = positions[choice]

def dep_option(choice):
    value = departments[choice]
    


##################################################################

ui.set_appearance_mode("dark")
ui.set_default_color_theme("blue")

app = ui.CTk()
app.geometry("600x400")
app.title("Register")

form_success = ui.CTkLabel(app, text="")
form_success.place(relx=0.33, rely=0.9)

idenNumber = ui.CTkEntry(app, placeholder_text="Enter your ID", width=200, text_color="black",fg_color="white", border_width=1, border_color="black")
idenNumber.place(relx=0.15, rely=0.2)

firstName = ui.CTkEntry(app, placeholder_text="First Name", width=200, text_color="black" ,fg_color="white", border_width=1, border_color="black")
firstName.place(relx=0.15, rely=0.3)

lastName = ui.CTkEntry(app, placeholder_text="Last Name", width=200, fg_color="white", text_color="black", border_width=1, border_color="black")
lastName.place(relx=0.51, rely=0.3)

age = ui.CTkEntry(app, placeholder_text="Age", width=200, fg_color="white", text_color="black", border_width=1, border_color="black")
age.place(relx=0.51, rely=0.4)

birthday = ui.CTkEntry(app, placeholder_text="Birthday MM/DD/YYYY", width=200, fg_color="white", text_color="black", border_width=1, border_color="black")
birthday.place(relx=0.15, rely=0.4)

dropDown = ui.CTkOptionMenu(app, values=position_nums, width=200, fg_color="white", text_color= "black", command=positions_option) 
dropDown.place(relx=0.51, rely=0.2)

department = ui.CTkOptionMenu(app,values=dep_nums, width=417, text_color="black", fg_color="white", command=dep_option)
department.place(relx=0.15, rely=0.5)

submit = ui.CTkButton(app, text="SUBMIT FORM", fg_color="blue", width=200, height=50, command=insert)
submit.place(relx=0.33, rely=0.7)


app.mainloop()

