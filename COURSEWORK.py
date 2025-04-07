
employees = []
employeeIdList = []
sales = []
comissions = []

rankedSales = []
rankedEmployees = []
rankedEmployeeId = []


newEmployeeAmount = int(input("Enter the amount of new employees: "))
for i in range(newEmployeeAmount + 5): 

    employeeName = input("Enter the name of the employee: ")
    employees.append(employeeName)

    employeeId = input("Enter the ID of the employee: ")
    employeeIdList.append(employeeId)


    employeeSales = int(input("Enter the number of sales the employee made: "))
    sales.append(employeeSales)

#ranking the lists AND getting the top sales guy
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
employees = rankedEmployees
sales = rankedSales
employeeIdList = rankedEmployeeId



for i in range(len(sales)):
    comission = sales[i] * 500
    comissions.append(comission)

#Applying the 15% bonus to the top sales guys
topComission = comissions[0] * 1.15
comissions[0] =round(topComission, 2)

totalComission = 0
for i in range(len(comissions)):
    totalComission += comissions[i]

totalSales = 0
for i in range(len(sales)):
    totalSales += sales[i]    




####  MENU ####

#printing the employee list in order of sales
for i in range(len(employees)):
    print(f'\nEmployee name: {employees[i]}\nEmployee ID: {employeeIdList[i]}\nSales: {sales[i]}')

#printing comissions for each employee
print('\n*******************************')
print("\nComissions: ")
for i in range(len(employees)):
    print(f'\nEmployee: {employees[i]} \nComission: £{comissions[i]}')



      




