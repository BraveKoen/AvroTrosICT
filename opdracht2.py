
def main():
    avroDiv = 3
    trosDiv = 5
    stopCount = 101
    
    #Begin vanag 1 tot en met stopCount 
    for number in range(1, stopCount): 
        
        #ik heb gebruik gemaakt van de modulus operator
        #op het moment dat het niet 1 is betkend het dat er geen rest is in de deel som en dus in de tafel zit
        if(not (number % avroDiv) and not (number % trosDiv)):
            print("AVROTROS")
            continue
        if(not (number % avroDiv)):
            print("AVRO")
            continue
        if(not (number % trosDiv)):
            print("TROS")
            continue
        
        print(number)
        

    
if __name__ == "__main__":
    main()
        
      
    