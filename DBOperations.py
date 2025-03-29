def create_Sqlite_connection(location_path, database_name):
    import sqlite3
    global connection
    connection=None
    location=location_path
    dbase=database_name
    conn=location+dbase
    
    #check the location of the database
    print(conn)
    
    #create new database
    connection=sqlite3.connect(conn)
    print('Database Created.')
    connection.commit()
    print('Changes saved.')
    return connection

def readcsv(loca, filename):
    import pandas as pd
    loc=loca
    fname=filename
    locate_file=loc+fname
    print(locate_file)
    df=pd.readcsv(locate_file)
    return df

def writecsv_to_db(dataframe, table_name):
    import pandas as pd
    df1=dataframe
    table=table_name
    print(table)
    df1.to_sql(table, connection, if_exists='replace,' index=False)
    return table_name

def displaydbtable (query_string, dataframe):
    import pandas as pd
    query_str=query_string
    print(query_str)
    dataframe= pd.read_sql(query_str, connection)
    return dataframe