'''
Function 1
- create a function that collects employee info
- the function should have a dictionary with keys: employee name, pay rate, hours worked
- collect user input values: employee name, pay rate, hours worked and assign to the keys above
- store dictionary in a list

function 2
- define a function that calculates the rates and pay,
'''

def empInput():
    empList = []
    i = 1
    while(i <= 10):
        name = input("enter employee name: ")

        # make sure the hours input is an integer or float
        while True:
            try:
                hours = float(input(f"enter number of hours {name} worked: "))
                break
            except ValueError:
                print("Input was not a valid number")

        # make sure the pay rate input is an integer or float
        while True:
            try:
                rate = float(input(f"enter {name}'s pay rate: "))
                print("\n")
                break
            except ValueError:
                print("Input was not a valid number")

        empDict = {"Employee Name": name.capitalize(),
                   "Hrs Worked": hours,
                   "Pay Rate": rate,
                   "Regular Pay": 0.0,
                   "OT Pay": 0.0,
                   "Gross Pay": 0.0,
                   "Fed Tax": 0.0,
                   "State Tax": 0.0,
                   "FICA": 0.0,
                   "Net Pay": 0.0
                   }
        empList.append(empDict)
        i += 1
    return empList



def calcPay(emp_List):
    for emp in emp_List:
        rate = emp["Pay Rate"]
        hrs = emp["Hrs Worked"]

        # calc pay for different hours worked
        if hrs <= 40:
            emp["Regular Pay"] = round(rate * hrs, 2)
        else:
            emp["Regular Pay"] = round(rate * 40, 2)
            emp["OT Pay"] = round((hrs - 40) * rate * 1.5, 2)


        # calc rates for remaining columns
        emp["Gross Pay"] = emp["Regular Pay"] + emp["OT Pay"]
        emp["Fed Tax"] = round(emp["Gross Pay"] * 0.1, 2)
        emp["State Tax"] = round(emp["Gross Pay"] * 0.06, 2)
        emp["FICA"] = round(emp["Gross Pay"] * 0.03, 2)
        emp["Net Pay"] = emp["Gross Pay"] - emp["Fed Tax"] - emp["State Tax"] - emp["FICA"]

    return emp_List



