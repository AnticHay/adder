words = "red blue blue orange red green blue white red black blue green red orange blue red white".split()
print(len(words))
for i in range (len(words)):
    currentword = words [i]
    print (currentword)
    if currentword == 'red':
        words [i] = 'pink'
    if currentword == 'blue':
        words [i] = 'purple'    
print (words)   