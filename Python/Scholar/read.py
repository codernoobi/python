#Read excel and display
#pip install xlrd

import xlrd 

#read file from specified path
loc = (r"C:\Users\I353296\Documents\me\Python\Scholar\Excel\small_data\food.xls") #path of the file  
# To open Workbook 
wb = xlrd.open_workbook(loc) 

#input spread sheet number to be read
num = input("enter the excel spread sheet number")
index = int(num) - 1
sheet = wb.sheet_by_index(index)  

#print(sheet.cell_value(0,0))

print(sheet.nrows)      #number of rows
print(sheet.ncols)      #number of columns

for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i))   #column headers

for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 0))   #first column

print(sheet.row_values(1))