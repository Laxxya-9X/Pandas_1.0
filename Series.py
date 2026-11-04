import pandas as pd
import numpy as np
 
print("Pandas version:", pd.__version__)
 
# =====================================================
# PART 1: SERIES  (a 1-dimensional labeled array)
# =====================================================
 
# 1.1 Create a Series from a list
s1 = pd.Series([10, 20, 30, 40])
print("\n--- Series from list ---")
print(s1)

 
# 1.2 Series with a custom index
s2 = pd.Series([85, 90, 78], index=["Maths", "Science", "English"])
print("\n--- Series with custom index ---")
print(s2)
 
# 1.3 Series from a dictionary (keys become the index)
s3 = pd.Series({"Amit": 25, "Riya": 30, "Karan": 22})
print("\n--- Series from dict ---")
print(s3)
 
# 1.4 Accessing data
print("\n--- Accessing ---")
print("Maths score:", s2["Maths"])        # by label
print("First item :", s2.iloc[0])         # by position
print("Values     :", s2.values)          # numpy array
print("Index      :", s2.index)
 
# 1.5 Vectorized operations (no loops needed!)
print("\n--- Operations ---")
print(s2 + 5)          # add 5 to every element
print(s2 * 2)
print(s2[s2 > 80])     # filter: only scores above 80
 
# 1.6 Useful Series methods
print("\n--- Methods ---")
print("Sum :", s2.sum())
print("Mean:", s2.mean())
print("Max :", s2.max())
print("Min :", s2.min())
print(s2.describe())