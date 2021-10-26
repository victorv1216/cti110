    #Calculation of Miles driven and cost
    # 10/28/2021
    # CTI-110 P2HW1 - Miles Per Gallon
    # Victor Villafane
    #




# Taking entry of the "miles driven", "gallons used" and "cost per gallon"
# miles driven
miles_driven = float(input('Enter miles driven: '))

#gallons used
gallons_used = float(input('Enter gallons used: '))

# cost per gallon
cost_per_gallon = float(input('Enter cost per gallon: '))



# Calculating miles per gallon by -> dividing miles driven by gallons used
miles_per_gallon = miles_driven/gallons_used

# Calculating total gas cost by -> dividing cost per gallon by gallons used
total_gas_cost = cost_per_gallon * gallons_used

# Calculating cost per mile by -> dividing total gas cost by miles driven
cost_per_mile = total_gas_cost/miles_driven

# Displaying "miles per gallon", "total gas cost" and "cost per mile" to the user
print('\nMiles Per Gallon: {:.2f}'.format(miles_per_gallon))
print('Total Gas Cost: ${}'.format(total_gas_cost))
print('Cost Per Mile: ${:.1f}'.format(cost_per_mile))
