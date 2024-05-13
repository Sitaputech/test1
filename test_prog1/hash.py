from collections import Counter
testFile=open('input.data','r')
hashFile=open('hash.txt','w')
lines=0
matchDict={}
for line in testFile:
    
    lines += 1

    myString = line.lower()
    mystringLen = len(myString)

    possMatches = []
  
    for startIndex in range(0, mystringLen-1):
        
        for endIndex in range(startIndex+1, mystringLen):
            currentString = myString[startIndex:endIndex]
            if(len(currentString)==2): possMatches.append(myString[startIndex:endIndex])
            else :continue
            
    myDict = {}

    for possMatch, count in Counter(possMatches).most_common():
        myDict.update({possMatch:count})
   
 
    for i in range(1, mystringLen - 1):
        pair = myString[i - 1] + myString[i]
        if pair in matchDict:
            matchDict[pair] = [matchDict[pair][0] + 1]
        else:
            matchDict[pair] = [1]
    
    
    maxVal = max(myDict.values())
    finalDict = {k:v for k, v in myDict.items() if v == maxVal}
    hashFile.write(str(finalDict)+'\n')
    max_val_all = max(matchDict.values())
    final_max_all = {k:v for k, v in matchDict.items() if v == max_val_all}

hashFile.write('the most common combination of characters in a file'+str(final_max_all))
testFile.close()