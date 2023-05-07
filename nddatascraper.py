import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import numpy as np

URL = "https://www.dmr.nd.gov/oilgas/riglist.asp"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#Find out table based on summary
results = soup.find(summary="Active drilling rig list results table")

#Find our HTML table from 'results'
tbody_table = results.findChild("tbody")

#Find table elements rows from 'tbody_table'
table_rows = tbody_table.find_all("tr")

#Where we will store our data
list = ["Rig", "Operator", "Well Name and Number", "Current Location", "County", "File No", "API", "Start Date", "** Next Location"]

for row in table_rows:
    #List holding all 'td' html data from row
    td_data = row.find_all("td")
    
    #Placeholder table to insert under 'list' using 'np.vstack'
    singlerow = []

    for element in td_data:
        singlerow.append(element.text.strip())
    
    list = np.vstack([list, singlerow])

#Create data frame from list and convert to csv file
data_frame_table = pd.DataFrame(list)
data_frame_table.to_csv(r"FILELOCATION.csv")