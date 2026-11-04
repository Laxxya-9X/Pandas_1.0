import numpy as np
import pandas as pd
# 2.1 Create a DataFrame from a dictionary
data = {
    "Name": ["Amit", "Riya", "Karan", "Sneha"],
    "Age": [25, 30, 22, 28],
    "City": ["Jaipur", "Delhi", "Mumbai", "Pune"],
    "Salary": [50000, 65000, 40000, 58000],
}
df = pd.DataFrame(data)
print("\n--- DataFrame from dict ---")
print(df)
 
# 2.2 Create a DataFrame from a list of lists
df2 = pd.DataFrame(
    [["Amit", 25], ["Riya", 30], ["Karan", 22]],
    columns=["Name", "Age"],
)
print("\n--- DataFrame from list of lists ---")
print(df2)
 
# 2.3 Create a DataFrame from a list of dictionaries (each dict = one row)
df3 = pd.DataFrame([
    {"Name": "Amit", "Age": 25},
    {"Name": "Riya", "Age": 30},
])
print("\n--- DataFrame from list of dicts ---")
print(df3)
 
# 2.4 Create a DataFrame from a NumPy array
df4 = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=["A", "B", "C"])
print("\n--- DataFrame from NumPy array ---")
print(df4)
 
# 2.5 Custom row index
df5 = pd.DataFrame(data, index=["a", "b", "c", "d"])
print("\n--- Custom index ---")
print(df5)
 
# =====================================================
# PART 3: BASIC DATAFRAME ATTRIBUTES
# =====================================================
print("\n--- Attributes ---")
print("Shape   :", df.shape)       # (rows, columns)
print("Columns :", list(df.columns))
print("Index   :", df.index)
print("Dtypes  :\n", df.dtypes)
print("Size    :", df.size)        # total number of cells
print("Ndim    :", df.ndim)
 
# =====================================================
# PART 4: SELECTING A COLUMN (preview of Lesson 4)
# =====================================================
print("\n--- Selecting columns ---")
print(df["Name"])                  # one column -> Series
print(type(df["Name"]))
print(df[["Name", "Salary"]])      # multiple columns -> DataFrame