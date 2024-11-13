#!/usr/bin/python3

# Petit test python pour traitement DB
# Pour me remettre en jambe en python....

# Pour afficher les 7 char d'une ligne: line[:7]
# Pour afficher a partir du char 3 d'une ligne: line[3:]
# line[3:].split(",")
# line[3:].split(",")

def processLine(line):
    if line.startswith("db"):
        #print("on a une ligne a processer")
        finalLine=""
        myArray=line[3:].split(",")
        for i in myArray:
            myCurrentByte=i[1:]
            #print("mycurrentByte="+myCurrentByte)
            #print("mycurrentNibble1="+myCurrentByte[0])
            #print("mycurrentNibble2="+myCurrentByte[1])
            finalLine+=myCurrentByte[1]
            finalLine+=","
            finalLine+=myCurrentByte[0]
            finalLine+=","
        #print(finalLine[:-1])
        return finalLine[:-1]


file=open("karl_levels.asm", mode="r")

with open("karl_levels.asm") as file:
    for item in file:
        if item=="\n":
            print("")
            continue
        if item.startswith("org"):
            print("-- "+item[:-1])
            continue
        if item.startswith(";"):
            print("-- "+item[:-1])
            continue
        if item.startswith("db"):
            itemProcessed = processLine(item)
            print(itemProcessed)
            continue
        #else:
        #    print("ligne autre")
