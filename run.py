import csv
import mysql.connector
from datetime import datetime


db_config = {
    "host": "localhost",
    "database": "financial_db",
    "user": "root",
    "password": "",
    'port':'3306'
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

   
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_data (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            ticker VARCHAR(10) NOT NULL,
            date DATE,  # Store date in desired format
            revenue DECIMAL(20, 8) DEFAULT NULL,
            gp DECIMAL(20, 8) DEFAULT NULL,
            fcf DECIMAL(20, 8) DEFAULT NULL,
            capex DECIMAL(20, 8) DEFAULT NULL
        );
    """)

    
    with open("./finance.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
       
        next(reader, None)

       
        for row in reader:
          
            date_str = row[1]
            date_obj = datetime.strptime(date_str, "%m/%d/%Y")
            formatted_date = date_obj.strftime("%Y-%m-%d")

            
            numerical_columns = [float(val) if val.strip() else None for val in row[2:]]
            converted_row = [row[0], formatted_date] + numerical_columns
            sql = "INSERT INTO stock_data (ticker, date, revenue, gp, fcf, capex) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, converted_row)

    conn.commit()
    print("Data imported successfully!")
except Exception as e:
    print(f"Error importing data: {e}")
finally:
    if conn:
        conn.close()
