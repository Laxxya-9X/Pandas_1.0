import numpy as np
import pandas as pd

data  = pd.read_csv("Pandas/laptops.csv" , encoding="latin1")
# print(data.head())             #first five rows
# print(data.tail())                #last five rows
# print(data.iloc[:5, 0:])           #number indexing

# informationi lene k liye

print(data.info())
# one method to print columns
print(data.columns)
#2 method to print particular columns


# columns name cleaning (RIght Format)
cols = data.columns
print(cols)    # Incorrect col name
def cleancol(list1):            # cleaning function cration 
    new = []
    for ele in list1:
        ele = ele.strip()      # aage pichhe ka space hta dega
        ele = ele.replace(" ","_")         # beech se space ko htana
        ele = ele.replace("(","")          #  kahi se  ( isko htana
        ele = ele.replace(")","")           # kahi se  ) isko htana
        ele = ele.capitalize()             #capitalize krna 
        new.append(ele)                    # ele ko new me append krna
    return new
col2 = cleancol(cols)  

print(col2)     # correct col name 

data.columns = col2

print(data.columns)      #Correct col printing


#=========================================================
# Screen_size ko string se float me convert kiya hai kyuki pandas me sare elements object default hote hai.


print(data['Screen_size'].unique())         # unique value printing

data["Screen_size"] = data['Screen_size'].str.replace('"',"").astype("float")      

print(data["Screen_size"])

print(data.info())


#==============================================
#Weight str to float

print(data['Weight'].unique())
data["Weight"] = data["Weight"].str.replace("kg","").str.replace("s","").astype("float")
print(data["Weight"])

     

#Ram to GB only =========================================================
 
print(data["Ram"].unique())
data["Ram"] = data["Ram"].str.replace("GB","").astype("int")
print(data["Ram"])


# print(data.select_dtypes("int"))
# print(data.select_dtypes("float"))
# print(data.select_dtypes("object"))


#===========================================================================
# Storage col. cleaning tb to gb 

print(data["Storage"].unique())


