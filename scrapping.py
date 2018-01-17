 # Import all packages we need  
from bs4 import BeautifulSoup  
import requests  
import pandas as pd

# Get this week's earning of top 10 movies 
url = "https://www.the-numbers.com/daily-box-office-chart"
print url 

# Table headers    
header = "Movie","Distributor","Gross","Change","Theaters";
data = list()
data.append(header) 

# Request HTTP response using the url     
r = requests.get(url)  
# Use BS4 to format the response
soup = BeautifulSoup(r.text.encode('utf-8','ignore'))  
# Find the div of interest
table1 = soup.findAll("div", {"id" : "page_filling_chart"})[1]  
table1_rows = table1.findAll("tr")  
for i in range(1,10):
  t = table1_rows[i] 
  data.append((t.findAll("td")[2].text,t.findAll("td")[3].text, t.findAll("td")[4].text, t.findAll("td")[5].text, t.findAll("td")[6].text))  
data = pd.DataFrame(data)
print data      