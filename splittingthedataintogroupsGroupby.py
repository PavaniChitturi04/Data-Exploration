import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 28, 31, 24],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'Salary': [5000, 6000, 5500, 7000, 4500]
})

#print("Grouping data by 'City' column")
#grouped = df.groupby('City')

# Accessing groups
#for city, group in grouped:
 #   print(f'City: {city}')
 #   print(group)
  #  print('---')

print("\n","Grouping by multiple columns")
grouped = df.groupby(['City', 'Age'])

# Accessing groups with multiple keys
for (city, age), group in grouped:
    print(f'City: {city}, Age: {age}')
    print(group)
    print('---')

# Applying aggregation functions on grouped data
grouped = df.groupby('City')
mean_salary = grouped['Salary'].mean()
median_age = grouped['Age'].median()

print("\n",'Mean Salary by City:')
print(mean_salary)
print("\n",'Median Age by City:')
print(median_age)
