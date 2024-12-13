import random
import time
import customtkinter

app = customtkinter.CTk()
app.title("my app")
app.geometry("800x600")





def button_callback():
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
    maxPoint = 0
    minPoint = 0

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





    #hiss skit
    while (run == 1):
        try:
            if direction == True:
                if max(subjektTarget) > max(subjektArray):
                    maxPoint = max(subjektTarget)
                else:
                    maxPoint = max(subjektArray)
                if min(subjektTarget) < min(subjektArray):
                    minPoint = min(subjektTarget)
                elif min(subjektArray) != 0:
                    minPoint = min(subjektArray)
                floor = maxPoint
                direction = False
            elif direction == False:
                floor = minPoint
                direction = True
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
                        print(f"grabb {loopInt} hoppar på")
                        subjektArray[loopInt] = 0
                    if (subjektTarget[loopInt] == procedure and subjektArray[loopInt] == 0):
                        print(f"grabb {loopInt} hoppar av")
                        subjektTarget[loopInt] = 0
                    loopInt = loopInt + 1
                loopInt = 0
                button.grid(row=1, column=0, padx=20, pady=20)
                time.sleep(0.5)
        if previousFloor < floor:
            procedure = previousFloor
            while (procedure < floor):
                procedure = procedure + 1
                print (f'|----|\n| 00 | hissen är på våning: {procedure}\n|----|\n')
                while (loopInt < 5):
                    if procedure == subjektArray[loopInt] and subjektArray[loopInt] <= subjektTarget[loopInt] or (subjektArray[loopInt] == maxPoint and procedure == maxPoint):
                        print(f"grabb {loopInt} hoppar på")
                        subjektArray[loopInt] = 0
                    if (subjektTarget[loopInt] == procedure and subjektArray[loopInt] == 0):
                        print(f"grabb {loopInt} hoppar av")
                        subjektTarget[loopInt] = 0
                    loopInt = loopInt + 1
                loopInt = 0
                button.grid(row=procedure, column=0, padx=20, pady=20)
                time.sleep(0.5)
        time.sleep(0.5)
        while (loopInt < 5):
            if procedure == subjektArray[loopInt] and subjektArray[loopInt] <= subjektTarget[loopInt] or (subjektArray[loopInt] == maxPoint and procedure == maxPoint):
                print(f"grabb {loopInt} hoppar på")
                subjektArray[loopInt] = 0
            if (subjektTarget[loopInt] == procedure and subjektArray[loopInt] == 0):  
                print(f"grabb {loopInt} hoppar av")
                subjektTarget[loopInt] = 0     
            loopInt = loopInt + 1
        loopInt = 0
        previousFloor = floor  
        if max(subjektTarget) == 0:
            while (loopInt < 5):
                subjektArray[loopInt] = random.randint(1,10)
                loopInt = loopInt + 1
                subjektArray[0] = 1
            loopInt = 0
            while (loopInt < 5):
                subjektTarget[loopInt] = random.randint(1,10)
                loopInt = loopInt + 1
            loopInt = 0
        print (subjektArray)
        print (subjektTarget)
    
        print("blatte")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=1, column=0, padx=20, pady=20)

app.mainloop()

