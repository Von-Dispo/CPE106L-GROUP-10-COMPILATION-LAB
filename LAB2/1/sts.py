def median(numList):

    list_length = len(numList)
    numList= sorted(numList)
    
    if(list_length%2 == 0):
        
        return (numList[list_length/2]+numList[list_length/2 + 1])//2
    else:
        return numList[(list_length)//2]

def mean(numList):

    summedTotal = 0
    list_length = len(numList)
    
    for item in numList:
        summedTotal += item
    
    average = summedTotal/list_length
    
    return average

def mode(numlist):

    frequency={}
    for number in numlist:
        if number in frequency:
            frequency[number] +=1
        else:
            frequency[number] = 1
            
    return [key for key in frequency.keys() if frequency[key] == max(frequency.values())]
