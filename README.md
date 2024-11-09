# Karl_treasure_hunt
Tic80 port of old Amstrad CPC game

To do this i need first to get data from existing Amstrad CPC Z80 assembly. 

Someone disassembled the whole game and commented the file. So the data (graphics, level data).
The python scripts here extract the data from the assembly file (or at least just an extract).

For the level data, it's very simple: one byte gives two backgrounds sprites.
For the sprites, the assembly file stores the data in a bit more complicated way. This is due to the way the CPC displays pixels on the screen: one byte stores the colors for two consecutives pixels but the bits are mangled together.
