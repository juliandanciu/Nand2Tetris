# Removes all comments and white space from the input stream and breaks
# it into Jack-language tokens, as specified by the Jack grammar. 

class JackTokenizer:
    keyword_map = {
        'class': 'CLASS',
        'constructor': 'CONSTRUCTOR',
        'function': 'FUNCTION',
        'method': 'METHOD',
        'field': 'FIELD',
        'static': 'STATIC',
        'var': 'VAR',
        'int': 'INT',
        'char': 'CHAR',
        'boolean': 'BOOLEAN',
        'void': 'VOID',
        'true': 'TRUE',
        'false': 'FALSE',
        'null': 'NULL',
        'this': 'THIS',
        'let': 'LET',
        'do': 'DO',
        'if': 'IF',
        'else': 'ELSE',
        'while': 'WHILE',
        'return': 'RETURN'
    } 

    symbol_set = {
        '{',
        '}',
        '(',
        ')',
        '[',
        ']',
        '.',
        ',',
        ';',
        '+',
        '-',
        '*',
        '/',
        '&',
        '|',
        '<',
        '>',
        '=',
        '~'
    }
    #opens the input file/stream and gets ready to tokenize it.
    def __init__(self, input_file):
        print('Initializing the JackTokenizer')
        self.f = open(input_file, 'r')
        self.current_token = 'still init??'
        self.currentChar = None
        
        
        

    #do we have more tokens in the input?
    def hasMoreTokens(self):

        #Returns Boolean
        return True

    #Gets the next token from the input and makes it the current token
    #This method should only be called if hasMoreTokens() is true
    #Initially there is no current token
    def advance(self):
        buffer = self.f.read(1)
        while buffer == ' ' or buffer == '\n' or buffer == '\t':
            buffer = self.f.read(1)
        #is it a comment??
        if buffer == '/':
            next_char = self.readNextCharacterAndRewind()
            if next_char == '*':
                self.f.read(1)
                self.readUntilEndOfComment()
                self.advance()
                return self.current_token
            if next_char == '/':
                self.f.read(1)
                self.readUntilEndOfLine()
                self.advance()
                return self.current_token

        #is it a string??
        if buffer == '"':
            print('start of a string')
            self.readUntilEndOfString()
            return self.current_token
        
        #is it an integer??
        if buffer.isdigit():
            print('start of an integer')
            self.readUntilEndOfInteger(buffer)
            return self.current_token

        #is it a letter or underscore??
        if self.charIsAlphaOrUnderscore(buffer):
            self.readUntilEndOfKeywordOrIdentifier(buffer)
            return self.current_token

        #is it a symbol??
        if buffer in self.symbol_set:
            print('buffer is in symbol set')
            self.current_token = buffer
            return self.current_token

        
        
        self.current_token = '@EOF@'
        return self.current_token
        

    def readNextCharacterAndRewind(self):
        last_pos = self.f.tell()
        next_char = self.f.read(1)
        self.f.seek(last_pos)
        return next_char    

    def readUntilEndOfLine(self):
        print('read until end of line function')
    
        buffer = self.f.read(1)
        while buffer != '\n':
            buffer = self.f.read(1)

    def readUntilEndOfComment(self):
        print('read until end of comment function')
        
        while True:
            buffer = self.f.read(1)
            while buffer != '*':
                buffer = self.f.read(1)

            last_pos = self.f.tell()
            buffer = self.f.read(1)    
            if buffer == '/':
                break
            else:
                self.f.seek(last_pos)
        
    def readUntilEndOfString(self):
        print('read until end of string function')

        token = ''
        while True:
            buffer = self.f.read(1)
            if buffer == '"':
                break
            else:
                token = token + buffer
        
        self.current_token = token

    def readUntilEndOfInteger(self, startChar):
        print('read until end of integer function')

        token = startChar
        while True:
            buffer = self.f.read(1)
            if not buffer.isdigit():
                position = self.f.tell()
                self.f.seek(position - 1)
                break
            else:
                token = token + buffer
        
        self.current_token = token
    

    def readUntilEndOfKeywordOrIdentifier(self, startChar):
        print('read until end of word function')

        token = startChar
        while True:
            buffer = self.f.read(1)
            if buffer.isdigit() or buffer.isalpha() or buffer == '_':
                token = token + buffer
            else:
                current_position = self.f.tell()
                self.f.seek(current_position - 1)
                break
        
        self.current_token = token
    
    def charIsAlphaOrUnderscore(self, char):
        if char.isalpha() or char == '_':
            return True
        else:
            return False

    #returns the type of the current token
    def tokenType(self):
        tokenTypes = {
            'KEYWORD', 
            'SYMBOL', 
            'IDENTIFIER', 
            'INT_CONST', 
            'STRING_CONST'
        }
        return
    
    #Returns the keyword which is the current token.
    #Should be called only when tokenType() is KEYWORD
    def keyWord(self):
        keyWords = {
            'CLASS',
            'METHOD',
            'FUNCTION',
            'CONSTRUCTOR',
            'INT',
            'BOOLEAN',
            'CHAR',
            'VOID',
            'VAR',
            'STATIC',
            'FIELD',
            'LET',
            'DO',
            'IF',
            'ELSE',
            'WHILE',
            'RETURN',
            'TRUE',
            'FALSE',
            'NULL',
            'THIS'
        }
        return

    #returns the character which is the current token
    #should be called only when tokenType() is SYMBOL
    def symbol(self):
        return

    #Returns the identifier which is the current token
    #should be called only when tokenType() is IDENTIFIER
    def identifier(self):
        return

    #returns the integer value of the current token.    
    #should be called only when tokenType() is INT_CONST
    def intVal(self):
        return
    
    #returns the string value of the current token, without the double quotes
    #should be called only when tokenType() is STRING_CONST
    def stringVal(self):
        return    
        