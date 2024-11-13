#!/usr/bin/python3

# Karl Treasure Hunt sprites decoding.
# It takes a file that contains the Amstrad CPC Z80 ASM format for sprites.
# In mode 0, one byte contains two pixels mixed together.
# This script decyphers the two colors contained in single bytes.

# Pour afficher les 7 char d'une ligne: line[:7]
# Pour afficher a partir du char 3 d'une ligne: line[3:]
# line[3:].split(",")
# line[3:].split(",")
#  hex(int(c,16)&0b1111) ==> '0xf'


# if set to true, the colors will be transformed to Tic80 default palette (Sweetie16)
adaptToTic80Palette = False


def splitColors(h):
    px1bit1=(int(h,16)&0b10000000)
    px1bit2=(int(h,16)&0b00100000)
    px1bit3=(int(h,16)&0b00001000)
    px1bit4=(int(h,16)&0b00000010)
    px2bit1=(int(h,16)&0b01000000)
    px2bit2=(int(h,16)&0b00010000)
    px2bit3=(int(h,16)&0b00000100)
    px2bit4=(int(h,16)&0b00000001)
    pix1=px1bit1>>4 | px1bit2>>3 | px1bit3>>2 | px1bit4>>1
    pix2=px2bit1>>3 | px2bit2>>2 | px2bit3>>1 | px2bit4
    if adaptToTic80Palette == True:
        print ("need adaptation to TIC80 palette")
    #DBG print("pix1="+bin(int(pix1))+" (soit "+hex(pix1)+"," + str("%02d" % pix1)+")")
    #DBG print("pix2="+bin(int(pix2))+" (soit "+hex(pix2)+"," + str("%02d" % pix2)+")")
    # following line returns two *hex* value (for 2 consecutive pixels)
    #return hex(pix1)[-1:]+","+hex(pix2)[-1:]
    # Following line returns two *int* values (for 2 consecutive pixels)
    return str("%02d" %pix1)+","+str("%02d" % pix2)

def processLine2(line):
    if line.startswith("db"):
        finalLine=""
        myHexLine=line[3:]
        #print(myHexLine)
        myArray=myHexLine.split(",")
        #print(myArray)
        #for i in range(0,len(myHexLine)):
        for i in range(0,len(myArray)):
            #extractHexChars=myArray[i][1]+myArray[i][2]
            h=myArray[i][1]+myArray[i][2]
            #print("h="+h)
            #px1bit1=(int(h,16)&0b10000000)
            #px1bit2=(int(h,16)&0b00100000)
            #px1bit3=(int(h,16)&0b00001000)
            #px1bit4=(int(h,16)&0b00000010)
            #px2bit1=(int(h,16)&0b01000000)
            #px2bit2=(int(h,16)&0b00010000)
            #px2bit3=(int(h,16)&0b00000100)
            #px2bit4=(int(h,16)&0b00000001)
            #pix1=px1bit1>>4 | px1bit2>>3 | px1bit3>>2 | px1bit4>>1
            #pix2=px2bit1>>3 | px2bit2>>2 | px2bit3>>1 | px2bit4
            #print("pix1="+bin(int(pix1))+" (soit "+hex(pix1)+")")
            #print("pix2="+bin(int(pix2))+" (soit "+hex(pix2)+")")
            colors1And2=splitColors(h)
            finalLine+=colors1And2
            finalLine+=","
        return finalLine # or finalLine[:-1] to get rid of last char (',') on line.


file=open("karl_sprites.asm", mode="r")

with open("karl_sprites.asm") as file:
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
        if item.__contains__(" x "):
            print("-- "+item[:-1])
            continue
        if item.__contains__(" ;"):
            print("-- "+item[:-1])
            continue
        if item.startswith("db"):
            itemProcessed =processLine2(item)
            print(itemProcessed)
            continue
        #else:
        #    print("ligne autre")
