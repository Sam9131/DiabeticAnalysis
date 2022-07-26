import pyodbc
import pandas as pd
# Trusted Connection to Named Instance


def df_to_row_tuples(df):
    """
    use list comprehension to format df rows as a list of tuples: 
    rows = [('Garfield','Orange','Eat'),('Meowth','White','Scratch')] 
    """
    df = df.fillna('')
    rows = [tuple(cell) for cell in df.values]
    return rows

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HP;DATABASE=Employeedb;Trusted_Connection=yes;')
print(connection)

cursor=connection.cursor()
print(cursor)

df1 = pd.read_csv('DIABETES CLINICAL.csv')
print(df1)

sql = ''' INSERT INTO DCLINICAL (PATIENTID
      ,PREGNANCIES
      ,PLASMAGLUCOSE
      ,DIASTOLICBP
      ,TRICEPSTHICKNESS
      ,SERUMINSULIN
      ,BMI
      ,DIABETESP
      ,AGE
      ,DIABETIC) VALUES(?,?,?,?,?,?,?,?,?,?) '''

rows = df_to_row_tuples(df1) 
for row in rows:
    cursor.execute(sql, row) 
    print("Inserting rows")
connection.commit()
