
import pandas as pd

# Step 1: Read the dataset
df = pd.read_csv("Luxury_Housing_Bangalore.csv")

# Step 2: Display first 5 rows
print(df.head())

# Step 3: Show column names
print("Columns in dataset:")
print(df.columns)

# Step 4: Show dataset info
print(df.info())

# Step 5: Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 6: Handle missing values

# Fill Amenity_Score with median
df["Amenity_Score"] = df["Amenity_Score"].fillna(
    df["Amenity_Score"].median()
)

# Fill Buyer_Comments with text
df["Buyer_Comments"] = df["Buyer_Comments"].fillna(
    "No Comments"
)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 7: Standardize text columns

# Step 7: Standardize text columns

text_columns = [
    "Transaction_Type",
    "Buyer_Type",
    "Purchase_Quarter",
    "Possession_Status",
    "Sales_Channel",
    "NRI_Buyer",
    "Buyer_Comments"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip().str.title()

print("\nText columns standardized successfully.")

# Step 8: Create new feature columns

# Create Quarter_Number column
# Step 8: Create Quarter_Number from date

# Convert Purchase_Quarter to datetime
df["Purchase_Quarter"] = pd.to_datetime(df["Purchase_Quarter"])

# Extract quarter number
df["Quarter_Number"] = df["Purchase_Quarter"].dt.quarter

print("\nQuarter_Number column created successfully.")

# Check output
print(df[["Purchase_Quarter", "Quarter_Number"]].head())

# Step 9: Save cleaned dataset

df.to_csv("cleaned_luxury_housing.csv", index=False)

print("\nCleaned dataset saved successfully as 'cleaned_luxury_housing.csv'")

print("\nFinal columns:")
print(df.columns)

print("\nFirst 5 rows of cleaned data:")
print(df.head())