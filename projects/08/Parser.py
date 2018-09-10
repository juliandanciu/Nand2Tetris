class Parser:
    def __init__(self, input_file):
        print("Initializing the parser...")
        if not input_file.endswith(".vm"):
            raise Exception("Parser only works with .vm extention files")
        
        self.vm_file = open(input_file, "r")
        

        self.current_command = None
        self.current_command_type = None

        #private properties
        self.current_line = None
        self.current_line_type = 'INIT'

        self.advance()

    def hasMoreCommands(self):
        if self.current_line_type != 'EOF':
            return True
        else:
            return False

    def advance(self):
        while self.current_line_type  != 'EOF':
            self.advance_line()
            if self.current_line_type == 'COMMAND':
                self.current_command = self.current_line
                self.current_command_type = self.commandType()
                return self.current_command
        
        return 'You have advanced to the EOF'           

    
    def advance_line(self):
        
        line = self.vm_file.readline()
        
        if not line:
            self.current_line = None
            self.current_line_type = 'EOF'
            return 'You have advanced to the EOF'
        
        if line.isspace():
            self.current_line = line
            self.current_line_type = 'SPACE'
            return 'You have advanced to a space'

        #remove everything to the right of comment symbol
        comment_index = line.find('//')
        if comment_index != -1:
            line = line[:comment_index]
            if line.isspace() or not line:
                self.current_line = '//'
                self.current_line_type = 'COMMENT'
                return 'You have advanced to a comment line'

        

        self.current_line = line.strip()
        self.current_line_type = 'COMMAND'
        return self.current_line

        

    #this should only be allowed to be called on a command
    def commandType(self):
        command_array = self.current_command.split()
        if len(command_array) == 1:
            if command_array[0] == 'return':
                return 'C_RETURN'
            
            return 'C_ARITHMETIC'
        
        if len(command_array) == 2:
            if command_array[0] == 'label':
                return 'C_LABEL'
            if command_array[0] == 'goto':
                return 'C_GOTO'
            if command_array[0] == 'if-goto':
                return 'C_IF'

        if len(command_array) == 3:
            if command_array[0] == 'push':
                return 'C_PUSH'
            if command_array[0] == 'pop':
                return 'C_POP'
            if command_array[0] == 'function':
                return 'C_FUNCTION'
            if command_array[0] == 'call':
                return 'C_CALL'
            
    
    
    def arg1(self):
        #returns the first arguments of the current command. in the case 
        command_array = self.current_command.split()
        if len(command_array) == 3 or len(command_array) == 2:
            return command_array[1]
        
        

        if len(command_array) == 1:
            return command_array[0]

        return 'arg1'

    def arg2(self):
        #returns the second argument of the current command
        command_array = self.current_command.split()
        if len(command_array) == 3:
            return command_array[2]
        
        
        return 'arg2'
    
        

            
