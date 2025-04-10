##INITIALIZING THE LISTS WHICH WILL BE USED IN THE PROGRAM
employees = []
employeeIdList = []
sales = []
comissions = []

rankedSales = []
rankedEmployees = []
rankedEmployeeId = []

#ASKING IF THERE ARE ANY NEW EMPLOYEES THIS WEEK
newEmployeeAmount = int(input("Enter the amount of new employees: ")) 

## Validating the input
while True:
    if newEmployeeAmount < 0:
          print("Amount of new employees has to be bigger than zero.")
          newEmployeeAmount = int(input("Enter the amount of new employees: "))
          continue
    else:
         break


for i in range(newEmployeeAmount + 5): # GETTING THE EMPLOYEES' INFORMATION

    employeeName = input("Enter the name of the employee: ")
    ## Validating the input
    while True:
        if len(employeeName) <= 1:
            print("Name cannot have less than 2 characters.")
            employeeName = input("Enter the name of the employee: ")
            continue
        else:
            employees.append(employeeName)
            break

    employeeId = int(input("Enter the ID of the employee: "))
    ## Validating the input
    while True:
        if employeeId in employeeIdList:
            print("IDs cannot be repeated.")
            employeeId = int(input("Enter the ID of the employee: "))
            continue
        else:
            employeeIdList.append(employeeId)
            break


    employeeSales = int(input("Enter the number of sales the employee made: "))
    ## Validating the input
    while True:
        if employeeSales < 0:
            print("An employee cannot have negative sales.")
            employeeSales = int(input("Enter the number of sales the employee made: "))
            continue
        else:
            sales.append(employeeSales)
            break


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

    print('\n############### MENU ###############\
          \n1- Employee list in order of sales\
          \n2- Sales comission for each employee\
          \n3- Total sales comission for the week\
          \n4- Total number of sales in the week\
          \n5- Employee of the week award\
          \n6- Bonus amount received by employee of the week')
    
    choice = (input("Choose the option to be displayed: "))
    while True:
        try:
              str(choice)
              break
        except:
             print("Invalid input. Try again.")
             choice = (input("Choose the option to be displayed: "))
    


       
    #PRINTING THE EMPLOYEE LIST IN ORDER OF SALES
    if choice == '1':
        print('\n*******************************')
        print("List of employees: ")
        for i in range(len(employees)):
                print(f'\nEmployee name: {employees[i]}\nEmployee ID: {employeeIdList[i]}\nSales: {sales[i]}')

    #PRINTING COMISSION FOR EACH EMPLOYEE
    elif choice == '2':
        print('\n*******************************')
        print("Comissions: ")
        for i in range(len(employees)):
            print(f'\nEmployee: {employees[i]} \nComission: £{comissions[i]}')

    #PRINTING THE TOTAL SALES COMISSION FOR THE WEEK
    elif choice == '3':
        print('\n********************************')
        print(f'Total Comissions for the week: £{totalComission}')

    #PRINTING THE TOTAL NUMBER OF PROPERTIES SOLD THIS WEEK
    elif choice == '4':
        print('\n********************************')
        print(f'Total number of properties sold this week: {totalSales}')

    #PRINTING EMPLOYEE OF THE WEEK'S INFORMATION
    elif choice == '5':
        print('\n********************************')
        print(f'Employee of the week award: \
                \nName: {employees[0]} \
                \nID: {employeeIdList[0]} \
                \nNumber of Sales: {sales[0]}')
    elif choice == '6':
        print('\n********************************')
        print(f'Bonus amount received by employee of the week: £{comissionBonus}')
    
    while(True):
        menuCondition = input("Do you want to use the menu again? Y/N: ")
        menuCondition = menuCondition.lower()

        if(menuCondition == 'y' or menuCondition == 'n'):
            break
        else:
            print("Invalid input.")
            continue
    if menuCondition == 'n':
        return
    else:
        menuPrint()

#CALLING THE MENU FUNCTION
menuPrint()