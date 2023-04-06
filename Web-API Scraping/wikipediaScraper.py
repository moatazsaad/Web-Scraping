from bs4 import BeautifulSoup 
import pandas as pd 
import requests 
    
## main structure 
response = requests.get("https://en.wikipedia.org/wiki/List_of_Nobel_laureates").content 
soup = BeautifulSoup(response,'html.parser')
table = soup.find('table',class_= "wikitable sortable")

## Data Storage
Data = {
    "Year":[],
    "Physics":[],
    "Chemistry":[],
    "Physiology":[],
    "Literature":[],
    "Peace":[],
    "Economics":[]
}

## Find rows 
rows = table.findAll("tr")

## Playing with each row 
for row_index in range(len(rows)-2) : 
    row_data = rows[row_index+1].findAll("td")
    Data['Year'].append(row_data[0].text)
    try :
        Data['Physics'].append(row_data[1].text)
    except:
        Data['Physics'].append('-')  
    try:
        Data['Chemistry'].append(row_data[2].text)
    except: 
        Data['Chemistry'].append('-')
    try : 
        Data['Physiology'].append(row_data[3].text)
    except :
        Data['Physiology'].append('-')
    try: 
        Data['Literature'].append(row_data[4].text)
    except:
        Data['Literature'].append('-')
    try:
        Data['Peace'].append(row_data[5].text)
    except:
        Data['Peace'].append('-')
    try : 
        Data['Economics'].append(row_data[6].text)
    except:
        Data['Economics'].append('-')



df = pd.DataFrame(Data)
df.to_csv("dd.csv")











