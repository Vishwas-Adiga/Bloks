import headers

exampleCode = ["print 'heelo'", "clearScreen 1", "leftMargin 10", "exit 0"]

def printTheList(list):
    for i in list:
        if (list.index(i) == len(list) - 1):
            origFile.write(i + "#\n")
        else:
            origFile.write(i + ",")




funcsAndTheirKeys = {   "print": [1, 1],   "exit": [2 , 3]  , "leftMargin": [3, 4] ,     "clearScreen": [4, 2]    }

headersToBeIncluded = []
codeList = []

for i in exampleCode:

    main =  i.partition(' ')
    keyword = main[0]
    finalKey = str(funcsAndTheirKeys[keyword][0])


    finalHeadKey = str(funcsAndTheirKeys[keyword][1])

    finalHead = headers.headersAndTheirKeys[finalHeadKey]
    print finalHead
    headersToBeIncluded.append(finalHead)  #Needs documentation...

    finalCode = [finalKey, main[2]]

    print finalCode



    codeList.append(finalCode)








origFile = file("PittuTest", 'w')


printTheList(headersToBeIncluded)


for j in codeList:
    printTheList(codeList[codeList.index(j)])




origFile.close()


origFile = file("PittuTest", 'r')

print origFile.readlines()

origFile.close()