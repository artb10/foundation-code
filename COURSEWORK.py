##INITIALIZING THE LISTS WHICH WILL BE USED IN THE PROGRAM
employees = []
employeeIdList = []
sales = []
comissions = []

rankedSales = []
rankedEmployees = []
rankedEmployeeId = []


newEmployeeAmount = int(input("Enter the amount of new employees: ")) #ASKING IF THERE ARE ANY NEW EMPLOYEES THIS WEEK
for i in range(newEmployeeAmount + 5): # GETTING THE EMPLOYEES' INFORMATION

    employeeName = input("Enter the name of the employee: ")
    employees.append(employeeName)

    employeeId = int(input("Enter the ID of the employee: "))
    employeeIdList.append(employeeId)


    employeeSales = int(input("Enter the number of sales the employee made: "))
    sales.append(employeeSales)


#RANKING THE LISTS AND GETTING THE TOP EMPLOYEE
for n in range(len(sales)):
        max = sales[0]
        indexOfMax = 0
        for i in range(len(sales)):
                if(sales[i] > max):
                        max = sales[i]
                        indexOfMax = i
                else:
                       max = max
                
        rankedEmployees.append(employees[indexOfMax])
        rankedEmployeeId.append(employeeIdList[indexOfMax])
        rankedSales.append(sales[indexOfMax])

        sales.pop(indexOfMax)
        employees.pop(indexOfMax)
        employeeIdList.pop(indexOfMax)

#TURNING THE NORMAL LISTS INTO THE RANKED LISTS
employees = rankedEmployees
sales = rankedSales
employeeIdList = rankedEmployeeId


#CALCULATING THE COMISSION FOR EACH EMPLOYEE
for i in range(len(sales)):
    comission = sales[i] * 500
    comissions.append(comission)

#CALCULATING AND APPLYING THE BONUS TO THE TOP EMPLOYEE'S COMISSION
comissionBonus = comissions[0] * 0.15
topComission = comissions[0] + comissionBonus
comissions[0] =round(topComission, 2)

#CALCULATING THE TOTAL VALUE OF COMISSIONS
totalComission = 0
for i in range(len(comissions)):
    totalComission += comissions[i]

#CALCULATING THE TOTAL AMOUNT OF PROPERTIES SOLD
totalSales = 0
for i in range(len(sales)):
    totalSales += sales[i]    



####  MENU ####


def menuPrint():
       
    #PRINTING THE EMPLOYEE LIST IN ORDER OF SALES
    for i in range(len(employees)):
                print(f'\nEmployee name: {employees[i]}\nEmployee ID: {employeeIdList[i]}\nSales: {sales[i]}')

    #PRINTING COMISSION FOR EACH EMPLOYEE
    print('\n*******************************')
    print("\nComissions: ")
    for i in range(len(employees)):
        print(f'\nEmployee: {employees[i]} \nComission: £{comissions[i]}')

    #PRINTING THE TOTAL SALES COMISSION FOR THE WEEK
    print('********************************')
    print(f'\nTotal Comissions for the week: £{totalComission}')

    #PRINTING THE TOTAL NUMBER OF PROPERTIES SOLD THIS WEEK
    print('********************************')
    print(f'\nTotal number of properties sold this week: {totalSales}')

    #PRINTING EMPLOYEE OF THE WEEK'S INFORMATION
    print('********************************')
    print(f'\nEmployee of the week award: \
            \nName: {employees[0]} \
            \nID: {employeeIdList[0]} \
            \nNumber of Sales: {sales[0]}\
            \nBonus amount received by employee of the week: £{comissionBonus}')#
    
    #ASKING IF THE USER WISHES TO USE THE MENU AGAIN
    menuCondition = input("Do you want to use the menu again? Y/N: ")
    menuCondition = menuCondition.lower()

    #IN CASE THE USER WANTS TO USE THE MENU AGAIN
    if menuCondition == 'y':
        menuPrint()

#CALLING THE MENU FUNCTION
menuPrint()