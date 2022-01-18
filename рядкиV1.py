from random import shuffle
word = str(input('Введіте слово для шифрування:'))
lenWord = len(word)
reversWord = word[::-1]
plusStr = 5
fullArr = []
charStep = '---'
for i in range(lenWord):
    littleArr = []
    for z in range (plusStr):
        littleArr.append('-')
    for z in range (i):
        littleArr.append(charStep)
    littleArr.append(reversWord[i])
    fullArr.append(littleArr)

shuffle(fullArr)
for part in fullArr:
    mystr = ''
    for part2 in part:
        mystr += part2
    print (mystr)

input()
    
