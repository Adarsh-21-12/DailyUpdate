#database connectivity

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Adarsh123"   
)

mycursor = connection.cursor()

mycursor.execute('SHOW DATABASES')
for i in mycursor:
    print(i)
mycursor.close()
connection.close()

#pandas

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df = pd.DataFrame(data)

print(df.head(3))

#new example done on google colab

import pandas as pd

#file downloaded from kaggle

ds = pd.read_csv('/indian_food.csv') 

ds.head(10)

#gives overview
ds.info()

#describes 
ds.describe()

few_columns = ds[['prep_time', 'name', 'course']]
print(few_columns)

print(ds.isnull().sum())

#null value
null_value = ds[ds['region'].isnull()]
print(null_value[['name','diet','course','state','region']])

#dropping duplicate values
drop_duplicate = ds.drop_duplicates(subset = ['ingredients'])
print(drop_duplicate)

#multiple methods used together. typo error in writing duplicated
duplicatess = ds[ds.duplicated('ingredients')]
print(duplicatess[['name','ingredients']].head(20))

#different data set with nullvalues
#sorting
#axis 0 means row 1 means column
sorted = ds.sort_values(by ='Severity of Anxiety Attack (1-10)', axis= 0, ascending=True)
print(sorted[['Age', 'Gender', 'Sleep Hours', 'Severity of Anxiety Attack (1-10)', 'Diet Quality (1-10)' ]].head(10))

#drops the null value
ds.dropna()

#how parameter
ds.dropna(how='any') #any/all

#subset
ds.dropna(subset=['Sleep Hours']) #drops all the null value present in SLeep hour column

#thresh parameter
ds.dropna(thresh=2) #the row/column should have 2 or more non null value to survive 

#sorting
ds.isnull().sum().sort_values(ascending=False) #total null value table sorted from column having most null value to least 

#filling the nullvalue data by calculating the mean
ds['Sleep Hours'].fillna(ds['Sleep Hours'].mean())

#unique values
unique_data = ds['Occupation'].unique()
print(unique_data)

unique_data = ds['Occupation'].unique()
number_of_unique_occupation = ds['Occupation'].nunique()

print(number_of_unique_occupation, unique_data)

value_counts = ds['Occupation'].value_counts()
print(value_counts)

#o/p
#Occupation
#Unemployed    2139
#Doctor        2004
#Teacher       1980
#Other         1971
#Student       1953
#Engineer      1953
#Name: count, dtype: int64

gender_count = ds['Gender'].value_counts()
age_duplicates = ds['Age'].mode()[0]
print(age_duplicates, gender_count)

#o/p
#43 Gender
#Female    5809
#Male      5723
#Other      468
#Name: count, dtype: int64 
#By this we can say that more female suffers from anxiety and mostly of age 43




