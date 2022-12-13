#This applications will calculate the commission of car sales

#Ask the user to enter the value of the car that they have sold
CarCost = input("How much did the car cost? £")

#print the value
print("The car sold for £" + str(CarCost))
print()

#calculate the commission based on sale value
#Less than £1000 = 1.5%
#less than £2000 = 2.5%
#Less than £3000 = 5%
#Greater than £3000 = 7.5%

#create an IF ELSE to calculate ommission
if(float(CarCost) <= 1000.00):
    print("The commission rate is 1.5%")
    CommissionRate = 1.5
elif(float(CarCost) <= 2000.00):
    print("The commission rate is 2.5%")
    CommissionRate = 2.5
elif(float(CarCost) <=3000.00):
    print("The commission rate is 5%")
    CommissionRate = 5
else:
  print("The commission rate is 7.5%")
  CommissionRate = 7.5

CommissionValue = float(CommissionRate) / 100 * float(CarCost)

print("The commission rate is " + str(CommissionRate) + "%")
print("The commission value is £" + str(CommissionValue))