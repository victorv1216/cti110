 # CTI-110
# P2HW2 - List and Sets
# Victor Villafane
# 10/19/21
#



myList = []

#loop to read user input
# append numbers to the list
for i in range(6):
    a = float(input('Enter num '+str(i+1)+': '))
    myList.append(a)
    
#printing list
print('Created list')
print(myList)

print('Smallest number in the list: '+str(min(myList)))
print('Largest number in the list: '+str(max(myList)))
print('Sum of numbers in the list: '+str(sum(myList)))
print('Average of numbers in the list: '+str(sum(myList)/len(myList)))

print(' ')

#creating set from list
mySet = set(myList)

print('Created set')
print(list(mySet))
