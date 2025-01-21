import pandas as pd

#UNDERSTANDING APPLY FUNCTION BY SOLVING QUESTIONS

data = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
}

ds = pd.DataFrame(data)

#Count the characters and make a different column of it

def count_char(char) :
    count = 0
    for i  in char :
        count += 1
    return count

ds['characters']= ds['Name'].apply(count_char)

print(ds)

#adding fixed value to data set

import pandas as pd

data = {
    'ID': [1, 2, 3, 4],
    'Sales': [200, 300, 400, 500]
}

ds = pd.DataFrame(data)

#Apply a function that adds 50 to each value in the Sales column.

def add_50(x):
    return x + 50

ds['Sales'] = ds['Sales'].apply(add_50)

print(ds)


# Apply a function to convert the Date column from YYYY-MM-DD format to DD/MM/YYYY format.

import pandas as pd

data = {
    'ID': [1, 2, 3, 4],
    'Date': ['2025-01-20', '2025-01-21', '2025-01-22', '2025-01-23']
}

ds = pd.DataFrame(data)

def format_converter(date):
    return pd.to_datetime(date).strftime('%d / %m / %Y')

ds['Correct_Format'] = ds['Date'].apply(format_converter)

print(ds)

#loc and iloc function
locs = ds.loc[[1,2], ['Date']]
print(locs)

ilocs = ds.iloc[1,2]
print(ilocs)

rename = ds.rename(columns= {'Date' : 'NewDate', 'Name':'NewName'})
print(rename)

rename = ds.rename(index= {1 : 'First', 2:'Second'})
print(rename)


#outliers

data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 30, 35, 40, 45, 50, 150, 32, 28, 22],  # Outlier: 150
    'Salary': [3000, 3500, 4000, 4500, 5000, 5500, 60000, 4200, 3800, 3400],  # Outlier: 60000
    'Hours_Worked': [40, 42, 38, 45, 50, 39, 37, 200, 41, 43],  # Outlier: 200
}


df = pd.DataFrame(data)

df['z_score_age'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()
df['z_score_Salary'] = (df['Salary'] - df['Salary'].mean()) / df['Salary'].std()
df['z_score_Hours_worked'] = (df['Hours_Worked'] - df['Hours_Worked'].mean()) / df['Hours_Worked'].std()

outliers_age = df[abs(df['z_score_age']) > 1 ]
outliers_Salary = df[abs(df['z_score_Salary']) > 1 ]
outliers_hours = df[abs(df['z_score_Hours_worked']) > 1 ]

print(outliers_age)
print(outliers_Salary)
print(outliers_hours)


 

