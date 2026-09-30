# code-orbit-
# Data Cleaning in Excel/Python

## Internship
CodeOrbit Tech - Data Analyst Internship

## Task 1: Data Cleaning in Excel/Python

### Objective
The main objective of this task is to clean a small dataset by handling missing values, removing duplicate records, and improving the data format using Python and Pandas.

## Tools Used

- Python
- Pandas
- Excel
- OpenPyXL
- Pydroid 3

## Dataset

The dataset contains the following columns:

- Name
- Age
- Salary

## Data Cleaning Process

The following steps were performed:

1. Loaded the Excel file using Pandas.
2. Checked the original dataset.
3. Removed duplicate rows.
4. Handled missing values.
5. Replaced the missing Age with the average Age.
6. Replaced missing Salary values with the average Salary.
7. Removed extra spaces from the Name column.
8. Saved the cleaned data into a new Excel file.

## Python Code

```python
import pandas as pd

# Read Excel file
df = pd.read_excel("sales_data.xlsx")

print("Original Data:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Age with average
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Salary with average
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Remove extra spaces
df["Name"] = df["Name"].str.strip()

print("\nCleaned Data:")
print(df)

# Save cleaned data
df.to_excel("cleaned_sales_data.xlsx", index=False)

print("\nData cleaning completed successfully!")