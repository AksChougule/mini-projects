# Import the package  
import pymysql  

# Create database connection  
conn = pymysql.connect(host='127.0.0.1', user='akshay', passwd='password', db='mydb')  

# Create cursor (connection variable)  
cur = conn.cursor()  

# Execute query  
cur.execute("SELECT * FROM mytable")  

# Get results in python variable  
results = cur.fetchall()  

# Display results  
print results  

# Close the the cursor  
cur.close()  

# Close the connection  
conn.close() 
