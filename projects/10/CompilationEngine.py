#Effects the actual compilation output
class CompilationEngine:
    STRING 
    #creates a new compilation engine with the given input
    #and output. The next routine called must be compileClass()
    def __init__(self, tokenizer, output_stream):
        print('CompilationEngine is initializing')
        self.output = open('mytest.xml', 'w')
        self.tokenizer = tokenizer
        #goes to the first token in the stream
        self.tokenizer.advance()

    
    #compiles a complete class
    def compileClass(self):
        #class
        if self.tokenizer.tokenType() == 'KEYWORD':
            if self.tokenizer.keyWord() == 'class':
                self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
                self.tokenizer.advance()
            else:
                raise Exception('expected keyword class')
        else:
            raise Exception('expected type keyword')

        #className
        if self.tokenizer.tokenType() == 'IDENTIFIER':
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
            self.tokenizer.advance()
        else:
            raise Exception('expected className identifier')
        
        #{
        if self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == '{':
            self.output.write('<symbol> { </symbol>')
            self.tokenizer.advance()
        else:
            raise Exception('expected {')
        
        
        #classVarDec*
        self.compileClassVarDec()

        self.compileSubroutine()

        #}
        if self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == '}':
            self.output.write('<symbol> } </symbol>')
            self.tokenizer.advance()
        else:
            raise Exception('expected }')
        

        return
    
    def compileClassVarDec(self):
        # ('static' | 'field') 
        if self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'static', 'field'}:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
        else:
            raise Exception('expected static or field')
        
        #type
        if (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'int', 'char', 'boolean'}):
            self.output.write('<keyword> ' self.tokenizer.keyWord() + ' </keyword>')
        elif (self.tokenizer.tokenType() == 'IDENTIFIER') :
             self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
        else:
            raise Exception('expected int, char, boolean, or className')

        #varName
        if self.tokenizer.tokenType() == 'IDENTIFIER':
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
        else:
            raise Exception('expected varName identifier')

        while self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ',':
            self.output.write('<symbol> , </symbol>')
            self.tokenizer.advance()
            if self.tokenizer.tokenType() == 'IDENTIFIER':
                self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
                self.tokenizer.advance()
            else:
                raise Exception('expecting identifier varName')

        #;
        if self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ';':
            self.output.write('<symbol> ; </symbol>')
            self.tokenizer.advance()
        else:
            raise Exception('expected ;')

        if self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'static', 'field'}:
            self.compileClassVarDec()

        return

    def compileSubroutine(self):
        #('constructor' | 'function' | 'method')
        if the current token is type keyword and in {'constructor', 'function', 'method'}:
            write <keyword> token </keyword>
        else:
            raise Exception()

        #('void' | type)
        if the current token is type keyword and void or type keyword and int, char, boolean, or type identifier and className:
            write to the output file
        else:
            raise Exception()    
        
        # subroutineName:identifier
        if the current token is an identifier:
            write to the output file

        #(
        
        #parameterList:
        compileParameterList()

        #)

        #subroutineBody
        #expect {
        
        #varDec*
        compileVarDec()

        compileStatements()

        #expect }



        return

    def compileParameterList(self):
        #perhaps empty
        
        #type
        if self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'int', 'char', 'boolean'}:
            write the keyword
        elif:
            self.tokenizer.tokenType() == 'IDENTIFIER' and className:
            write the identifier
        else:
            raise Exception('expected type')
        
        while the token is a ,:
            write the command 
            if the next token is a varName:
                write the varName:
            else:
                raise Exception()
        
        




        return

    def compileVarDec(self):
        # ('var') 
        if self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'var'}:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
        else:
            raise Exception('expected static or field')
        
        #type
        if (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'int', 'char', 'boolean'}):
            self.output.write('<keyword> ' self.tokenizer.keyWord() + ' </keyword>')
        elif (self.tokenizer.tokenType() == 'IDENTIFIER') :
             self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
        else:
            raise Exception('expected int, char, boolean, or className')

        #varName
        if self.tokenizer.tokenType() == 'IDENTIFIER':
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
        else:
            raise Exception('expected varName identifier')

        while self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ',':
            self.output.write('<symbol> , </symbol>')
            self.tokenizer.advance()
            if self.tokenizer.tokenType() == 'IDENTIFIER':
                self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
                self.tokenizer.advance()
            else:
                raise Exception('expecting identifier varName')

        #;
        if self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ';':
            self.output.write('<symbol> ; </symbol>')
            self.tokenizer.advance()
        else:
            raise Exception('expected ;')

        
        return
    
    
    def compileStatements(self):
        
        return

    def compileDo(self):
        
        return

    def compileLet(self):
        return

    def compileWhile(self):
        return

    def compileReturn(self):
        return

    def compileIf(self):
        return

    def compileExpression(self):
        return

    def compileTerm(self):
        return

    def compileExpressionList(self):
        return
