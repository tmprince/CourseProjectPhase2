#   Torrance Prince
#   CIS261
#   Project Phase 2
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter start date (mm/dd/yyyy): ")
    todate = input("Enter end date (mm/dd/yyyy): ")
    return fromdate,  todate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]


        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print()
        print("Name: ", empname)
        print("From Date: ", fromdate)
        print("To Date: ", todate)
        print("Hours Worked: ", format(hours, '.2f'))
        print("Hourly Rate: ", format(hourlyrate, '.2f'))
        print("Gross Pay: ", format(grosspay, '.2f'))
        print("Tax Rate: ", format(taxrate, '.1%'))
        print("Income Tax: ", format(incometax, '.2f'))
        print("Net Pay: ", format(netpay, '.2f'))
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay 
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHours"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay

def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours: {EmpTotals["TotHours"]}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]}')
    print(f'Total Income Tax: {EmpTotals["TotTax"]}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]}')

if __name__ == "__main__":
  
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        
        EmpDetail = [fromdate,
                     todate,
                     empname,
                     hours,
                     hourlyrate,
                      taxrate]
 
        EmpDetailList.append(EmpDetail)

    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)
