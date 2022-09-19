import math

def sortList(array:list, target:int, returnLenght: int) -> list:
    returnList = []
    if(returnLenght > len(array)):
        raise ValueError("Expected return list is bigger then original list")
    array.sort()
    
    targetIndex = 0
    
    
    #als het target getal kleiner is dan het eerste nummber van de array word het altijd op index 0 gezet
    if(target < array[0]):
        targetIndex = 0
    #getal is groter is dan het laatste getal word die op de laatste index gezet
    elif(target > array[len(array)-1]):
        targetIndex = len(array)-1 
    else:
        #loop door de lijst om de index te bepalen 
        for index in range(len(array)):
            #is True wanneer de target ook in de lijst staat
            if(target == array[index]):
                targetIndex = index-1
                break 
            #is True wanneer het getal tussen een kleiner en groter getal zit
            elif(target > array[index] and target < array[index+1]):
                targetIndex = index
                break
      

    #startIndex word gebruikt om daarna de lijst in 1 keer goed er in te zetten zonder daarna weer .sort() te gebruiken
    startIndex = targetIndex + 1 - math.ceil(returnLenght/2)
  
    #index mag niet niet groter worden dan de laaste index
    #als dit het geval is word de start index steeds kleiner
    if((startIndex+ len(array)) > (len(array))):
        startIndex -= (startIndex + returnLenght) - len(array)
        
    #index mag niet negatief zijn
    if(startIndex < 0 ):
        startIndex = 0
    
    
    for i in range(returnLenght):
        returnList.append(array[startIndex + i])
    
    return returnList

    
def main():
    array =  [1, 2, 4, 4, 6, 7]
    print(sortList(array, 4, 4))

if __name__ == "__main__":
    main()
        
