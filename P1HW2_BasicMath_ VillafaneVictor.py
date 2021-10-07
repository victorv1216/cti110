    #Calculating Expenses for the month.
    # 10/6/2021
    # CTI-110 P1HW2 - Basic Math
    # Victor Villafane
    #
name = input("Enter the name of the expense: ")  # input name
monthlycharge = float(input("Enter monthly charge: "))  # convert to float and input
monthlytax = 0.060*monthlycharge  # calculate monthly tax
amountmonthly = monthlycharge + monthlytax  # add tax to monthlycharge
amountyearly = amountmonthly*12.00  # calculate yearly charge
print("Bill:  "+name+" --------- Before Tax:  $"+str(monthlycharge))
print("Monthly Tax:\t\t$"+str(round(monthlytax, 2)))  # display the monthly tax after rounding
print("Monthly Charge:\t\t$"+str(round(amountmonthly, 2)))  # display the monthly charge after rounding
print("Annual Charge:\t\t$"+str(round(amountyearly, 3)))  # display the annual charge after rounding
