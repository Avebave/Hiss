import random
import time

direction = True #true = upp, false = neråt
elevatorButtons = [10]
run = 1

floor = 1
previousFloor = 0
procedure = 1
targetFloor = 1
loopInt = 0

print (f'hissen är på våning: {floor}')


#Subjekt nedan här

subjektArray = [1,2,3,4,5]
subjektTarget =[1,2,3,4,5]
subjektArraySort = [1,2,3,4,5]
subjektTargetSort =[1,2,3,4,5]

while (loopInt < 5):
    subjektArray[loopInt] = random.randint(1,10)
    loopInt = loopInt + 1
    subjektArray[0] = 1
loopInt = 0
while (loopInt < 5):
    subjektTarget[loopInt] = random.randint(1,10)
    loopInt = loopInt + 1
loopInt = 0


print(subjektArray)
print(subjektTarget)



print(loopInt)
# GÖR EN COPY AV ARRAY OK

#hiss skit
while (run == 1):
    try:
        floor = int(input(""))
    except ValueError:
        print("Skriv rätt din idiot")
    if floor == 500:
        print("välkommen till secret våning")
    if floor != 500:
        if floor > 10 or floor < 1:
            print("Det finns endast 10 våningar")
            floor = previousFloor
    
    if previousFloor > floor:
        procedure = previousFloor
        while (procedure > floor):
            procedure = procedure - 1
            print (f'|----|\n| 00 | hissen är på våning: {procedure}\n|----|\n')
            while (loopInt < 5):
                if procedure == subjektArray[loopInt] and subjektArray[loopInt] >= subjektTarget[loopInt]:
                    print("Finns en grabb här")
                    subjektArray[loopInt] = 0
                if (subjektTarget[loopInt] == procedure and subjektArray[loopInt] == 0):
                    print("fuck this guy!!")
                    subjektTarget[loopInt] = 0
                loopInt = loopInt + 1
            loopInt = 0
            time.sleep(0.5)
    if previousFloor < floor:
        procedure = previousFloor
        while (procedure < floor):
            procedure = procedure + 1
            print (f'|----|\n| 00 | hissen är på våning: {procedure}\n|----|\n')
            while (loopInt < 5):
                if procedure == subjektArray[loopInt] and subjektArray[loopInt] <= subjektTarget[loopInt]:
                    print("Finns en grabb här")
                    subjektArray[loopInt] = 0
                if (subjektTarget[loopInt] == procedure and subjektArray[loopInt] == 0):
                    print("fuck this guy!!")
                    subjektTarget[loopInt] = 0
                loopInt = loopInt + 1
            loopInt = 0
            time.sleep(0.5)
    print (loopInt)
    time.sleep(0.5)
    previousFloor = floor  