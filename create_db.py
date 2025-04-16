import pandas as pd
import sqlite3
import os

# Create or connect to SQLite DB
conn = sqlite3.connect('chinook.db')

# Path to CSVs
data_folder = 'data'

for csv_file in os.listdir(data_folder):
    if csv_file.endswith('.csv'):
        table_name = csv_file.replace('.csv', '')
        df = pd.read_csv(os.path.join(data_folder, csv_file))
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Table {table_name} created.")

conn.close()
