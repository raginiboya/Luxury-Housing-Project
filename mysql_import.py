import pandas as pd
from sqlalchemy import create_engine

# read cleaned csv
df = pd.read_csv("cleaned_luxury_housing.csv")

# MySQL connection
username = "root"
password = "720767"
host = "localhost"
database = "luxury_housing_db"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# import into MySQL
df.to_sql(
    "luxury_housing_data",
    con=engine,
    if_exists="replace",
    index=False
)
print("Data imported successfully into MySQL!")