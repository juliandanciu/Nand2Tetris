class Parser:
    def __init__(self, inputFile):
        print('Constructing the object')
        self.fileObject = open(inputFile, 'r')
        self.currentCommand = 'INIT'
    
    #bug: hasMoreCommands is not hasMoreLines (but it will work for now if you make sure the end of the program is not just a space)
    def hasMoreCommands(self):
        starting_position = self.fileObject.tell()
        next_line = self.fileObject.readline()
        self.fileObject.seek(starting_position)
        if next_line:
            return True
        else:
            return False
        
    
    

    def advance(self):
        if not self.hasMoreCommands():
            print('No more commands: EOF')
            return

        while self.hasMoreCommands():
            
            line = self.fileObject.readline()
            
            #remove comments
            index = line.find('//')
            if index != -1:
                line = line[:index]
                if not line:
                    continue

            if line.isspace():
                continue

            self.currentCommand = line.strip()
            return;

        #in case the last line is a space
        print('No more commands: EOF')
        return

    
    def commandType(self):

        command = self.currentCommand
        if command == 'INIT':
            return 'PARSER_INIT'
        
        if command[0] == '@':
            return 'A_COMMAND'
        
        if command[0] == '(':
            return 'L_COMMAND'
        
        
        return 'C_COMMAND'


    
    def symbol(self):
        if self.commandType() == 'A_COMMAND':
            return self.currentCommand.lstrip('@')
        if self.commandType() == 'L_COMMAND':
            return self.currentCommand.lstrip('(').rstrip(')')

        return 'The current command is not and A or L Command'

    
    def dest(self):
        if self.commandType() == 'C_COMMAND':
            line = self.currentCommand
            equalSignIndex = line.find('=')
            if equalSignIndex == -1:
                return 'null'
            else:
                return line[0:equalSignIndex]
        else:
            return 'not a C command'

    
    def comp(self):
        if self.commandType() == 'C_COMMAND':
            cCommand = self.currentCommand
            
            equalSignIndex = cCommand.find('=')
            
            
            #if the command has equal sign 
            if equalSignIndex != -1:
                startingIndex = equalSignIndex + 1
                
                cCommand = cCommand[startingIndex:]
                #if the command has 
            
            
            
            semicolanIndex = cCommand.find(';')
            if semicolanIndex != -1:
                cCommand = cCommand[:semicolanIndex]
                    
            
            
            return cCommand
        else:
            return 'not a C command'
        
    
    def jump(self):
        if self.commandType() == 'C_COMMAND':
            cCommand = self.currentCommand
            semicolanIndex = cCommand.find(';')
            if semicolanIndex != -1:
                return cCommand[semicolanIndex + 1 :]
            else:
                return 'null'
        else:
            return 'not a C Command'
    

    