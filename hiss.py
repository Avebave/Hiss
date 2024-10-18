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
    print(loopInt)
    print(subjektArray[loopInt])
    loopInt = loopInt + 1
loopInt = 0
while (loopInt < 5):
    subjektTarget[loopInt] = random.randint(1,10)
    print(loopInt)
    print(subjektTarget[loopInt])
    loopInt = loopInt + 1

subjektArraySort = subjektArray
subjektTargetSort = subjektTarget

print(subjektArray)
print(subjektTarget)
subjektArraySort.sort()
subjektTargetSort.sort()
print(subjektArraySort)
print(subjektTargetSort)


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
            time.sleep(0.5)
    if previousFloor < floor:
        procedure = previousFloor
        while (procedure < floor):
            procedure = procedure + 1
            print (f'|----|\n| 00 | hissen är på våning: {procedure}\n|----|\n')
            time.sleep(0.5)
    time.sleep(0.5)
    previousFloor = floor

while ():
    if previousFloor > floor:
        procedure = previousFloor
        while (procedure > floor):
            procedure = procedure - 1
            print (f'|----|\n| 00 | hissen är på våning: {procedure}\n|----|\n')
            time.sleep(0.5)

if previousFloor < floor:
    procedure = previousFloor
    while (procedure < floor):
        procedure = procedure + 1
        print (f'|----|\n| 00 | hissen är på våning: {procedure}\n|----|\n')
        time.sleep(0.5)
time.sleep(0.5)
previousFloor = floor