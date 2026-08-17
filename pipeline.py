import pandas as pd
from sqlalchemy import create_engine

# 1. Load data
df = pd.read_csv('walmart.csv')

# 2. Standardize column names to lowercase with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 3. Clean Unit Price: remove dollar sign ($)
if df['unit_price'].dtype == 'object':
  df['unit_price'] = (
      df['unit_price'].astype(str).str.replace('$', '').astype(float)
  )

# 4. Handle Missing Values
df.dropna(inplace=True)

# 5. Feature Engineering: Total and Profit
df['total'] = df['unit_price'] * df['quantity']
df['profit'] = df['total'] * df['profit_margin']

# 6. Date & Time Transformation (Shifts)
df['date'] = pd.to_datetime(df['date'])
df['hour'] = pd.to_datetime(
    df['time'].astype(str), format='%H:%M:%S'
).dt.hour
df['shift'] = pd.cut(
    df['hour'],
    bins=[-1, 11, 16, 24],
    labels=['Morning', 'Afternoon', 'Evening'],
)

print('Data preprocessing complete!')
print(df.head())

import urllib.parse
from sqlalchemy import create_engine

# Database Configuration
DB_USER = 'root'
DB_PASSWORD = urllib.parse.quote_plus(
    'Saloni@123'
)  # Encodes '@' safely as '%40'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'walmart_db'

engine = create_engine(
    f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

# Export to MySQL Table
df.to_sql(name='walmart_sales', con=engine, if_exists='replace', index=False)
print('Successfully exported dataset into MySQL table: walmart_sales')