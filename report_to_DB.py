import pandas as pd
from sqlalchemy import create_engine, inspect

# Replace with your actual file path and database credentials
excel_file_path = 'SOC2_STAGE.xlsx'
database_uri = 'dialect+driver://username:password@host:port/database'
table_name = 'get correct table name from Zuya'

# Create a database engine
engine = create_engine(database_uri)
inspector = inspect(engine)

# Function to check if the table exists and compare headers
def headers_match(table, df):
    if table in inspector.get_table_names():
        columns = [col['name'] for col in inspector.get_columns(table)]
        return columns == list(df.columns)
    return False

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Check and adjust headers
row_index = 0
while headers_match(table_name, df.iloc[row_index:]):
    row_index += 1

# Use the appropriate row for headers and the rest for data
df.columns = df.iloc[row_index]
df = df.iloc[row_index + 1:]

# Write the data to the database
df.to_sql(table_name, engine, index=False, if_exists='append')

print("Data has been successfully written to the database.")
