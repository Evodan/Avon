Num = int(input("How many scripts do you want to combine? "))
Scripts = [""] * Num
Targets = [""] * Num
botname = input("Enter the name of the bot ")

for loop in range(0,Num):
    Scripts[loop] = input("enter the path of script #" + str(loop+1)+" ")
    Targets[loop] = input("Enter the name of Character you want to target \n "
                   "from this script, exactly as it is in the script. \n"
                   "(If there is a space or anything else before the :, than include it. ")

New = open('Script Transform/NewScript.txt', 'w')
New.close()

index = 0
for script in Scripts:
    script.replace('\\', '/')
    Orignal = open(script, 'r')
    Contents = Orignal.readlines()
    Orignal.close()
    S_Index = 0
    for line in Contents:
        Contents[S_Index] = line.replace(Targets[index], botname)
        S_Index += 1
    print(Contents)
    New = open('Script Transform/NewScript.txt', 'a')
    New.writelines(Contents)
    New.close()
    index +=1
