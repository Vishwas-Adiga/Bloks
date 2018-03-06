import headers

exampleCode = ["print 'heelo'", "clearScreen 1", "leftMargin 3", "exit 0"]



funcsAndTheirKeys = {   "print": [1, 1],   "exit": [2 , 3]  , "leftMargin": [3, 4] ,     "clearScreen": [4, 2]    }

headersToBeIncluded = []

for i in exampleCode:
    keyword =  i.partition(' ')
    keyword = keyword[0]

    headersToBeIncluded.append(headers.headersAndTheirKeys[str(funcsAndTheirKeys[keyword][0])])  #Needs documentation...




origFile = file("PittuTest", 'w')



for i in headersToBeIncluded:
    if(headersToBeIncluded.index(i) == len(headersToBeIncluded) - 1):
        origFile.write(i + "#")
    else:
        origFile.write(i + ",")





origFile.close()


origFile = file("PittuTest", 'r')

print origFile.readlines()

origFile.close()