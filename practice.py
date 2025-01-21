import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 30, 35, 40, 45, 50, 150, 32, 28, 22],  # Outlier: 150
    'Salary': [3000, 3500, 4000, 4500, 5000, 5500, 60000, 4200, 3800, 3400],  # Outlier: 60000
    'Hours_Worked': [40, 42, 38, 45, 50, 39, 37, 200, 41, 43],  # Outlier: 200
}


df = pd.DataFrame(data)

df['z_score'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()

outliers = df[abs(df['z_score']) > 1 ]

print(outliers)

 
