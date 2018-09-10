#Julian Danciu
#7/14/2018
import sys

from myparser import Parser
from symbol_table import SymbolTable
from code import Code

file_path = sys.argv[1]
print('#######')
print(file_path)

#should accept a command line arguments specifying the path to the file you want to assemble
print('Running the assembler...')

#open the .asm file for reading
asm = Parser(file_path + '.asm')

#open another file for writing
hack = open(file_path + '.hack', 'w')

#advance all the way through the file once and collect all the symbols (only the psudo symbols?)

symbol_table = SymbolTable()

l_command_address = 0

#a_command_set = set()
a_command_list = []


while asm.hasMoreCommands():
    
    asm.advance()
    current_command = asm.currentCommand
    current_command_type = asm.commandType()

    

    if current_command_type == 'L_COMMAND':
        #get the symbol and 
        symbol = asm.symbol()
        #add the symbol into the table only if it does not already exist
        if not symbol_table.contains(symbol):
            #add the symbol
            symbol_table.addEntry(symbol, l_command_address)

        continue
    

    if current_command_type == 'A_COMMAND':
        
        #get the symbol
        symbol = asm.symbol()
        #check to see if it really is a symbol or just a number 
        if not symbol.isdigit(): 
            if symbol not in a_command_list:
                a_command_list.append(symbol)
        
        l_command_address += 1
        continue
    
    
    l_command_address += 1
    
        
#as long as the symbols refer to the same memory address throughout the entire program, you do not need to keep them in order
a_command_address = 16

for symbol in a_command_list:
    if not symbol_table.contains(symbol):
        symbol_table.addEntry(symbol, a_command_address)
        a_command_address += 1



#now we go through the commands for the second time
print(symbol_table.hash_table)



asm.fileObject.seek(0)

while asm.hasMoreCommands():

    asm.advance()
    current_command = asm.currentCommand
    current_command_type = asm.commandType()

    #only do stuff if it is a A_COMMAND or an C_COMMAND 

    if current_command_type == 'A_COMMAND':
        symbol = asm.symbol()
        if symbol.isdigit():
            #convert the symbol to binary and call 
            address = int(symbol)
            hack_command = format(address, '016b') + '\n'
            hack.write(hack_command)
        else:
            #resolve symbol to address
            address = symbol_table.getAddress(symbol)
            hack_command = format(address, '016b') + '\n'
            hack.write(hack_command)

    if current_command_type == 'C_COMMAND':
        dest_bin = Code.dest(asm.dest())
        comp_bin = Code.comp(asm.comp())
        jump_bin = Code.jump(asm.jump())

        hack_command = '111' + comp_bin + dest_bin + jump_bin + '\n'
        hack.write(hack_command)


asm.fileObject.close()
hack.close()

