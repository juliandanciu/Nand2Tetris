import sys
import os

from Parser import Parser
from CodeWriter import CodeWriter



if os.path.isdir(sys.argv[1]):
    print('directory alert>>>', end='')
    print(sys.argv[1])
    writ = CodeWriter(sys.argv[1] + '/' + os.path.basename(sys.argv[1]) + '.asm')
    vm_files = os.listdir(sys.argv[1])
    writ.writeInit()
else:
    print('single file alert')
    writ = CodeWriter(sys.argv[1].replace('.vm', '.asm'))
    vm_files = {os.path.basename(sys.argv[1])}
    print(vm_files)


for vm_file in vm_files:
    
    if not vm_file.endswith('.vm') :
        continue

    #this is for a directory
    parser_parameter = sys.argv[1] + '/' + vm_file
    
    
    writ.setFileName(vm_file.replace('.vm', ''))
    
    
    if not os.path.isdir(sys.argv[1]):
        parser_parameter = sys.argv[1]
    
    parser = Parser(parser_parameter)
    while parser.hasMoreCommands():
    
        command_type = parser.commandType()
        if command_type == 'C_ARITHMETIC':
            writ.writeArithmetic(parser.arg1())
        if command_type == 'C_PUSH':
            writ.writePushPop('push', parser.arg1(), parser.arg2())
        if command_type == 'C_POP':
            writ.writePushPop('pop', parser.arg1(), parser.arg2())
        if command_type == 'C_LABEL':
            writ.writeLabel(parser.arg1())
        if command_type == 'C_GOTO':
            writ.writeGoto(parser.arg1())
        if command_type == 'C_IF':
            writ.writeIf(parser.arg1())
        if command_type == 'C_FUNCTION':
            writ.writeFunction(parser.arg1(), parser.arg2())
        if command_type == 'C_RETURN':
            writ.writeReturn()
        if command_type == 'C_CALL':
            writ.writeCall(parser.arg1(), parser.arg2())    
    
        parser.advance()


writ.asm_file.close()



