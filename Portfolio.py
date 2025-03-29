#Problem One Task One

import pandas as pd
data = pd.read_csv('C:/Python/anscombe.csv')
df1 = pd.DataFrame(data, columns = ['x1','y1'])
print(df1)

df2= pd.DataFrame(data, columns = ['x2', 'y2'])
print(df2)

df3= pd.DataFrame(data, columns = ['x3', 'y3'])
print(df3)

df4= pd.DataFrame(data, columns = ['x4', 'y4'])
print(df4)


#Problem One Task Two

import pandas as pd
data = pd.read_csv('C:/Python/anscombe.csv')
df1 = pd.DataFrame(data, columns = ['x1','y1'])
print(df1.describe())
print(df2.describe())
print(df3.describe())
print(df4.describe())


#Problem One Task Three

import matplotlib.pyplot as plt
#a scatter plot to show the dataset
plt.scatter(df1['x1'], df1['y1'], color='blue')
plt.title('Dataset I scatter plot')
plt.show()

plt.scatter(df2['x2'], df2['y2'], color='magenta')
plt.title('Dataset II scatter plot')
plt.show()

plt.scatter(df3['x3'], df3['y3'], color= 'green')
plt.title('Dataset III scatter plot')
plt.show()

plt.scatter(df4['x4'], df4['y4'], color='orange')
plt.title('Dataset IV scatter plot')
plt.show()


#Problem Two Question One 

import pandas as pd
import matplotlib.pyplot as plt

#a scatter plot to identify a correlation between earnings and unemployment.
df= pd.read_csv('C:/Python/recent-grads.csv')
data2= pd.DataFrame(df,columns= ['Median', 'Unemployment_rate'])
soviet_union= ['Red']
data2.plot(kind='scatter', x='Median', y='Unemployment_rate', color= soviet_union)

plt.title('Scatter plot')
plt.show()


#Problem Two Question Two

india= df[df["Median"]>60000]

ax=plt.gca()
#gca stands for 'get current axis'

colombia = ['red', 'blue', 'orange']

india.plot(kind='bar', x='Major', y=['P25th','Median','P75th'], stacked=True, color= colombia, ax=ax)
plt.title('Bar chart')
plt.show()


#Problem Three Number 1 
#Reload user_reviews.csv into a DataFrame 

import pandas as pd 
df= pd.read_csv('C:/Python/user_reviews.csv')
print(df)


#Problem Three Number 2
df["len_text"] = df["text"].apply(len)


#Problem Three Number 3
#Create a function to determine the super category of a review

def get_super_category(row):
    if row["grade"] >= 9 or row["len_text"] > 1000:
        return "expert reviewer"
    elif row["grade"] <= 1 and row["len_text"] > 1000:
        return "opposed-reviewer"
    else:
        return "neutral reviewer"

# Implement the super category feature using a for loop
super_category_for = []
for i in range(len(df)):
    row = df.iloc[i]
    super_category_for.append(get_super_category(row))
df["super category for loop"] = super_category_for

# Implement the super category feature using a while loop
super_category_while = []
i = 0
while i < len(df):
    row = df.iloc[i]
    super_category_while.append(get_super_category(row))
    i += 1
df["super category while loop"] = super_category_while

# Implement the super category feature using vectorisation
df["super category vectorisation"] = df.apply(get_super_category, axis=1)

# Output the resulting DataFrame
print(df.head())


#Problem Four 

import sqlite3
# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('b.db')
cursor = conn.cursor()
print('Database created.')


# Question 1a) Create the listed tables (locations, departments)
cursor.execute('''CREATE TABLE IF NOT EXISTS locations (
                    location_id INT(3),
                    street_address VARCHAR(50) UNIQUE NOT NULL,
                    postal_code VARCHAR(10) NOT NULL,
                    city VARCHAR(50) NOT NULL,
                    state_province VARCHAR(50) NOT NULL,
                    country VARCHAR(50) NOT NULL,
                    CONSTRAINT lid_pk PRIMARY KEY (location_id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
                    department_id INT(4),
                    department_name VARCHAR(20) UNIQUE NOT NULL,
                    location_id INT(3),
                    CONSTRAINT d_did_pk PRIMARY KEY (department_id),
                    CONSTRAINT d_lid_fk FOREIGN KEY (location_id) REFERENCES locations (location_id)
                )''')

# Question 1b) Insert data to listed tables (locations, departments)
NULL=None

locations_data = [
    (100, '2 Nice Road', 'NZ 7TH', 'London', 'Greater London', 'UK'),
    (200, '23 Pretty Road', 'BS1 8FD', 'Bristol', 'Bristol County', 'UK'),
    (300, '26 Great Street', 'BN1 4BF', 'Brighton', 'Sussex', 'UK'),
    (400, '143 Lovely Road', 'CB1 2NV', 'Cambridge', 'Cambridgeshire', 'UK')
]

departments_data = [
    (10, 'IT', 100),
    (20, 'Operations', 200),
    (30, 'Sales', 300),
    (40, 'Marketing', 200),
    (50, 'Management', NULL)
]

cursor.executemany('INSERT INTO locations VALUES (?, ?, ?, ?, ?, ?)', locations_data)
cursor.executemany('INSERT INTO departments VALUES (?, ?, ?)', departments_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Question 2) Display all departments and their locations, as well as the locations with no departments

conn = sqlite3.connect('b.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT d.department_name, l.street_address, l.city, l.state_province, l.country
    FROM departments d
    LEFT JOIN locations l ON d.location_id = l.location_id
''')

departments_with_locations = cursor.fetchall()

cursor.execute('''
    SELECT l.street_address, l.city, l.state_province, l.country
    FROM locations l
    WHERE l.location_id NOT IN (SELECT location_id FROM departments)
''')

locations_with_no_departments = cursor.fetchall()

print("Departments with locations:")
for row in departments_with_locations:
    print(row)

print("\nLocations with no departments:")
for row in locations_with_no_departments:
    print(row)

# Close the connection
conn.close()


#Problem Five Task 1

def create_Sqlite_connection(location_path, database_name):
    import sqlite3
    global connection
    connection = None
    location=location_path
    dbase= database_name
    conn=location+dbase

    #check the location of the database
    print(conn)

    #create new database
    connection= sqlite3.connect(conn)
    print('Database created.')
    connection.commit()
    print('Changes saved.')
    return connection


def readcsv(loca, filename):
    import pandas as pd
    loc=loca
    fname=filename
    locate_file=loc+fname
    print(locate_file)
    df=pd.read_csv(locate_file)
    return df

def writecsv_to_db(dataframe, table_name):
    import pandas as pd
    df1=dataframe
    table=table_name
    print(table)
    df1.to_sql(table, connection, if_exists='replace', index=False)
    return table_name

def displaydbtable (query_string, dataframe):
    import pandas as pd
    query_str=query_string
    print(query_str)
    dataframe=pd.read_sql(query_str, connection)
    return dataframe

#Problem Five Task 2

import DBOperations as dbo
import pandas as pd
import sqlite3

#Import all functions from DBOperations 
from DBOperations import *

#Provide the location of the database and its sample name
path= "C:/Users/kabir/"
database_name="DMomDB"

#Create the DMomDB using the function, create_Sqlite_connection under "C:/Users/kabir/"
connection=create_Sqlite_connection(path,database_name)

#Iris.csv is read from its current location and stored in dataframe df
path= "C:/Python/"
filename= "Iris.csv"

#Read the Iris.csv using the function, readcsv
df=readcsv(path,filename)

#Table Iris is created under DMomDB database space and populated with data from dataframe df using the function write csv_to_db
tablename='Iris'

table_name=writecsv_to_db(df,tablename)

#Run a query on the Iris table
query_string='SELECT * FROM Iris where Id>9 and PetalLengthCm<1.4'
displaydbtable(query_string,'dataframe')