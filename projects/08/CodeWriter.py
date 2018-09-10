class CodeWriter:
    def __init__(self, output_file):
        print('Initializing the Code Writer...')
        self.asm_file = open(output_file, "w")
        self.end_hash = 0
        self.return_hash = 0
        self.current_vm_file = 'init_vm_file'
        #self.vm_function_stack = [];
        #self.vm_function_stack.append('init_vm_function')
        self.current_vm_function = 'init_vm_function'
    
    #informs the CodeWriter that the translation of a new VM file is started 
    def setFileName(self, fileName):
        self.current_vm_file = fileName
    
    #we need to make sure that there are items on the stack to manipluate, otherwise we risk moving out of the virtual stack space
    def writeArithmetic(self, command):
        #TODOS make sure that you add an endhash for gt lt eq
        self.asm_file.write('//' + command + '\n')
        if command == 'add':
            self.asm_file.write('@SP\nA=M-1\nD=M\nA=A-1\nM=M+D\n@SP\nM=M-1\n')
        if command == 'sub':
            self.asm_file.write('@SP\nA=M-1\nD=M\nA=A-1\nM=M-D\n@SP\nM=M-1\n')
        if command == 'neg':
            self.asm_file.write('@SP\nA=M-1\nM=-M\n')
        if command == 'eq':
            self.asm_file.write('@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@END_' + str(self.end_hash) + '\nD;JEQ\n@SP\nA=M-1\nM=0\n(END_' + str(self.end_hash) + ')\n')
            self.end_hash += 1
        if command == 'gt':
            self.asm_file.write('@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@END_' + str(self.end_hash) + '\nD;JGT\n@SP\nA=M-1\nM=0\n(END_' + str(self.end_hash) + ')\n')
            self.end_hash += 1
        if command == 'lt':
            self.asm_file.write('@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@END_' + str(self.end_hash) + '\nD;JLT\n@SP\nA=M-1\nM=0\n(END_' + str(self.end_hash) + ')\n')
            self.end_hash += 1
        if command == 'and':
            self.asm_file.write('@SP\nA=M-1\nD=M\nA=A-1\nM=M&D\n@SP\nM=M-1\n')
        if command == 'or':
            self.asm_file.write('@SP\nA=M-1\nD=M\nA=A-1\nM=M|D\n@SP\nM=M-1\n')
        if command == 'not':
            self.asm_file.write('@SP\nA=M-1\nM=!M\n')

    #TODO only allowed to call for C_PUSH and C_POP  
    def writePushPop(self, command, segment, index):
        #what are the valid segments
        self.asm_file.write('//' + command + ' ' + segment + ' ' + index + '\n')
        
        
        if command == 'push':
            if segment == 'argument':
                #push argument index
                self.asm_file.write('@' + index + '\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

            if segment == 'local':
                #push local index
                self.asm_file.write('@' + index + '\nD=A\n@LCL\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            
            if segment == 'static':
                #push static index
                self.asm_file.write('@' + self.current_vm_file + '.' + index + '\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            
            if segment == 'constant':
                #push constant index
                self.asm_file.write('@' + index + '\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            
            if segment == 'this':
                #push this index
                self.asm_file.write('@' + index + '\nD=A\n@THIS\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            
            if segment == 'that':
                #push that index
                self.asm_file.write('@' + index + '\nD=A\n@THAT\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            
            if segment == 'pointer':
                #push pointer index
                self.asm_file.write('@' + index + '\nD=A\n@3\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            
            if segment == 'temp':
                #push temp index
                self.asm_file.write('@' + index + '\nD=A\n@5\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
        
        if command == 'pop':
            if segment == 'argument':
                #pop argument index
                self.asm_file.write('@' + index + '\nD=A\n@ARG\nD=D+M\n@R15\nM=D\n@SP\nAM=M-1\nD=M\n@R15\nA=M\nM=D\n')
                
            
            if segment == 'local':
                #pop local index
                self.asm_file.write('@' + index + '\nD=A\n@LCL\nD=D+M\n@R15\nM=D\n@SP\nAM=M-1\nD=M\n@R15\nA=M\nM=D\n')
            
            if segment == 'static':
                #pop static index
                self.asm_file.write('@SP\nAM=M-1\nD=M\n@' + self.current_vm_file + '.' + index + '\nM=D\n')
            
            if segment == 'this':
                #pop this index
                self.asm_file.write('@' + index + '\nD=A\n@THIS\nD=D+M\n@R15\nM=D\n@SP\nAM=M-1\nD=M\n@R15\nA=M\nM=D\n')
            
            if segment == 'that':
                #pop that index
                self.asm_file.write('@' + index + '\nD=A\n@THAT\nD=D+M\n@R15\nM=D\n@SP\nAM=M-1\nD=M\n@R15\nA=M\nM=D\n')
            
            if segment == 'pointer':
                #pop pointer index
                self.asm_file.write('@' + index + '\nD=A\n@3\nD=D+A\n@R15\nM=D\n@SP\nAM=M-1\nD=M\n@R15\nA=M\nM=D\n')
            
            if segment == 'temp':
                #pop temp index
                self.asm_file.write('@' + index + '\nD=A\n@5\nD=D+A\n@R15\nM=D\n@SP\nAM=M-1\nD=M\n@R15\nA=M\nM=D\n')
        return 

    #writes assemby code that effects the VM 
    #initialization, also called bootstrap code. this code must be placed at the begining of the output file
    def writeInit(self):
        self.asm_file.write('//bootstrap code\n')
        self.asm_file.write('@256\nD=A\n@SP\nM=D\n')
        #self.asm_file.write('@Sys.init\n0;JMP\n')
        #now we need to call Sys.init
        #self.vm_function_stack.append('Sys.init')
        self.writeCall('Sys.init', '0')

    
    #writes assemby code that effects the label command
    def writeLabel(self, label):
        self.asm_file.write('//label ' + label + '\n')
        self.asm_file.write('(' + self.current_vm_function + '$' + label + ')\n')
    
    #writes assembly code that effects the goto command
    def writeGoto(self, label):
        self.asm_file.write('//goto ' + label + '\n')
        self.asm_file.write('@' + self.current_vm_function + '$' + label + '\n0;JMP\n')


    def writeIf(self, label):
        self.asm_file.write('//if-goto ' + label + '\n')
        self.asm_file.write('@SP\nAM=M-1\nD=M\n@' + self.current_vm_function + '$' + label + '\nD;JNE\n')
    
    def writeCall(self, functionName, numArgs):
        self.asm_file.write('//call ' + functionName + ' ' + numArgs + '\n')
        #push return address
        self.asm_file.write(
            '@FUNC_RETURN_' + str(self.return_hash) + '\n' +
            'D=A\n' +
            '@SP\n' +
            'A=M\n' +
            'M=D\n' +
            '@SP\n' +
            'M=M+1\n' +
            #push LCL
            '@LCL\n' +
            'D=M\n' +
            '@SP\n' +
            'A=M\n' +
            'M=D\n' +
            '@SP\n' +
            'M=M+1\n' +
            #push ARG
            '@ARG\n' +
            'D=M\n' +
            '@SP\n' +
            'A=M\n' +
            'M=D\n' +
            '@SP\n' +
            'M=M+1\n' +
            #push THIS
            '@THIS\n' +
            'D=M\n' +
            '@SP\n' +
            'A=M\n' +
            'M=D\n' +
            '@SP\n' +
            'M=M+1\n' +
            #push THAT
            '@THAT\n' +
            'D=M\n' +
            '@SP\n' +
            'A=M\n' +
            'M=D\n' +
            '@SP\n' +
            'M=M+1\n' +
            #LCL = SP
            '@SP\n' +
            'D=M\n' +
            '@LCL\n' +
            'M=D\n' +
            #ARG = SP - n - 5
            'D=D-1\n' +
            'D=D-1\n' +
            'D=D-1\n' +
            'D=D-1\n' +
            'D=D-1\n'
        )

        for i in range(int(numArgs)):
            self.asm_file.write('D=D-1\n')
        
        self.asm_file.write(
            '@ARG\n' +
            'M=D\n' +
            #goto f
            '@' + functionName + '\n' +
            '0;JMP\n' +
            #(return address)
            '(FUNC_RETURN_' + str(self.return_hash) + ')\n'
        )
        
        #increment the hash function to create unique labels
        self.return_hash = self.return_hash + 1
        #self.vm_function_stack.append(functionName)


    
    def writeReturn(self):
        
        self.asm_file.write('//return\n')
        self.asm_file.write(
            # FRAME = LCL
            '@LCL\n' +
            'D=M\n' +
            '@R13\n' + #FRAME variable
            'M=D\n' +
            
            # RET = *(FRAME - 5)
            'D=D-1\n' +
            'D=D-1\n' +
            'D=D-1\n' +
            'D=D-1\n' +
            'D=D-1\n' +
            'A=D\n' +
            'D=M\n' +
            '@R14\n' + #RET variable
            'M=D\n' +

            # *ARG = pop()
            '@SP\n' +
            'AM=M-1\n' +
            'D=M\n' +
            '@ARG\n' +
            'A=M\n' +
            'M=D\n' +

            # SP = ARG+1
            '@ARG\n' +
            'D=M+1\n' +
            '@SP\n' +
            'M=D\n' +
            
            # THAT = *(FRAME - 1)
            '@R13\n' +
            'AM=M-1\n' +
            'D=M\n' +
            '@THAT\n' +
            'M=D\n' +
            
            # THIS = *(FRAME - 2)
            '@R13\n' +
            'AM=M-1\n' +
            'D=M\n' +
            '@THIS\n' +
            'M=D\n' +
            
            # ARG = *(FRAME - 3)
            '@R13\n' +
            'AM=M-1\n' +
            'D=M\n' +
            '@ARG\n' +
            'M=D\n' +
            
            # LCL = *(FRAME - 4)
            '@R13\n' +
            'AM=M-1\n' +
            'D=M\n' +
            '@LCL\n' +
            'M=D\n' +
            
            # goto RET
            '@R14\n' +
            'A=M\n' +
            '0;JMP\n'
        )
        
        #self.vm_function_stack.pop()
    

    def writeFunction(self, functionName, numLocals):
        self.asm_file.write('//function ' + functionName + ' ' + numLocals + '\n')
        self.asm_file.write('(' + functionName + ')\n')
        # push constant 0 numLocals times
        for i in range(int(numLocals)):
            self.asm_file.write('@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

        self.current_vm_function = functionName;
        







    

