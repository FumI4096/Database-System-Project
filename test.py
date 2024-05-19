import pyodbc as pdb
import customtkinter as ui


def test_connection():
    try:
        connection = pdb.connect('DRIVER={SQL Server};' +
                                 'Server=FX505DY\\SQLEXPRESS;' +
                                 'Database=Payroll_Management_System;' +
                                 'Trusted_Connection=True')
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print("Test query result:", result)
    except pdb.Error as ex:
        print('Connection failed', ex)

test_connection()