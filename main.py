import pandas as pd
from EmployeePayroll import empInput, calcPay
'''
Algorithm Steps
- create a function that collects employee info
- the function should have a dictionary with keys: employee name, pay rate, hours worked
- collect user input values: employee name, pay rate, hours worked and assign to the keys above
- store dictionary in a list

- define a function that calculates the rates and pay,
- output the result in a table format
- pandas table formatting comes in handy. 
- Please install pandas to enable formatted table printing
'''

# get employee data input
empData = empInput()

# calculate employee pay rate
empDataRates = calcPay(empData)

# stop pandas from truncating table
pd.options.display.max_columns = 1000

# stop pandas from inserting new line (\n) when table columns are too long
pd.set_option('display.expand_frame_repr', False)

# format result with pandas
df = pd.DataFrame(data=empDataRates)

# format format table index to start from 1 and not the default 0
df.index = df.index + 1

print(df)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
