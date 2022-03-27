import os                           
import pandas as pd                 
import openpyxl

from openpyxl import load_workbook

# Finding path for raw data directory
path = os.getcwd()      
files = os.listdir(path+"/raw_data")
#print(files)

# Remove cell style
def removeFormatting(ws):
    for row in ws.iter_rows():
        for cell in row:
            cell.style = 'Normal'

# Convert excel to list
for f in files:
    print(f)
    data = pd.read_excel(path+"/raw_data/"+f,'sheet 1')
    data_list = data.values.tolist()

    clean_data_list = []
    for dl in data_list:
        clean_data_list.append([x for x in dl if str(x) != 'nan'])  

    print(clean_data_list)
    #df = df.append(data)

