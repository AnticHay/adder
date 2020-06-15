numbers = [4,7,8,3,2]
currentmax = 0
for number in numbers:
    print (number)
    if number > currentmax:
        print ('maxisnow',number)
        currentmax = number