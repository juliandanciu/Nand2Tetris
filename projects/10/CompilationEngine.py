#Effects the actual compilation output
class CompilationEngine:
    
    className_set = {}
    subroutineName_set = {}
    varName_set = {}

    KEYWORD = 'KEYWORD'
    SYMBOL = 'SYMBOL'
    IDENTIFIER = 'IDENTIFIER'
    INT_CONST = 'INT_CONST'
    STRING_CONST = 'STRING_CONST'

    CLASS = 'class'
    METHOD = 'method'
    FUNCTION = 'function'
    CONSTRUCTOR = 'constructor'
    INT = 'int'
    BOOLEAN = 'boolean'
    CHAR = 'char'
    VOID = 'void'
    VAR = 'var'
    STATIC = 'static'
    FIELD = 'field'
    LET = 'let'
    DO = 'do'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    RETURN = 'return'
    TRUE = 'true'
    FALSE = 'false'
    NULL = 'null'
    THIS = 'this'
    

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
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord == CLASS:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()    
        else:
            raise Exception('EXPEXTED "class"')

        #className
        if self.tokenizer.tokenType() == IDENTIFIER:
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
    
    def compileVoidOrType(self):
        #type
        if (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'int', 'char', 'boolean', 'void'}):
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
        elif (self.tokenizer.tokenType() == 'IDENTIFIER') :
             self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
             self.tokenizer.advance()
        else:
            raise Exception('expected int, char, boolean, or className')

    def compileType(self):
        #type
        if (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'int', 'char', 'boolean'}):
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
        elif (self.tokenizer.tokenType() == 'IDENTIFIER') :
             self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
             self.tokenizer.advance()
        else:
            raise Exception('expected int, char, boolean, or className')

    def compileClassVarDec(self):
        # ('static' | 'field') 
        if self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'static', 'field'}:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
        else:
            raise Exception('expected static or field')
        
        #type
        self.compileType()

        #varName
        if self.tokenizer.tokenType() == 'IDENTIFIER':
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
            self.tokenizer.advance()
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

        #this should be handled somewhere else
        #if self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'static', 'field'}:
         #   self.compileClassVarDec()

        return

    def compileSubroutine(self):
        #('constructor' | 'function' | 'method')
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() in {'constructor', 'function', 'method'}:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword')
            self.tokenizer.advance()
        else:
            raise Exception('expected "constructor", "function", or "method"')
        

        #('void' | type)
        self.compileVoidOrType()
        
    
        # subroutineName:identifier
        if self.tokenizer.tokenType() == IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
            self.tokenizer.advance()
        else:
            raise Exception('expected subroutineName identifier')

        


        #(
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ( </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol (')

        
        
        #parameterList:
        compileParameterList()

        #)
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ')':
            self.output.write('<symbol> ) </symbol>')
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol )')

        #subroutineBody
        #expect {
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '{':
            self.output.write('<symbol> { </symbol>')
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol {')
        
        #varDec*
        while self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() == 'var':
            compileVarDec()


        compileStatements()

        #expect }
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '}':
            self.output.write('<symbol> } </symbol>')
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol }')



        return

    def compileParameterList(self):
        #perhaps empty
        if self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ')':
            return
        
        #type
        self.compileType()


        # comma ,,,,,
        while self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ',':
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>')
            self.tokenizer.advance()
            
            if self.tokenizer.tokenType() == IDENTIFIER:
                self.output.write('<identifier> ' + self.tokenizer.identifer() + ' </identifier>')
                self.tokenizer.advance()
            else:
                raise Exception('expected varName identifier')
            
        

        return

    def compileVarDec(self):
        # ('var') 
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() in {'var'}:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
        else:
            raise Exception('expected keyword var')
        
        #type
        self.compileType()

        #varName
        if self.tokenizer.tokenType() == IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
            self.tokenizer.advance()
        else:
            raise Exception('expected varName identifier')

        while self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ',':
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
        
        # statement*

        while self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() in {'let', 'if', 'while', 'do', 'return'}:
            if self.tokenizer.keyWord() == 'let':
                self.compileLet()
            
            if self.tokenizer.keyWord() == 'if':
                self.compileIf()

            if self.tokenizer.keyWord() == 'while':
                self.compileWhile()

            if self.tokenizer.keyWord() == 'do':
                self.compileDo()

            if self.tokenizer.keyWord() == 'return':
                self.compileReturn()


        return

    def compileDo(self):
        
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() == 'do':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "do"')

        #subroutineCall

        
        # subroutineName:identifier subroutine name, className or varName
        if self.tokenizer.tokenType() == IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
            self.tokenizer.advance()
        else:
            raise Exception('expected subroutineName, className or varName identifier')

        # .
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '.':
            self.output.write('<symbol> . </symbol>')
            self.output.advance()
            # subroutineName:identifier
            if self.tokenizer.tokenType() == IDENTIFIER:
                self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
                self.tokenizer.advance()
            else:
                raise Exception('expected subroutineName identifier')

        elif self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '(':
            #continue
            pass

        else:
            raise Exception('expected symbol ( or .')
        
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>')
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol (')

        #expressionList
        self.compileExpressionList()

        # )
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ')':
            self.output.write('<symbol> ) </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol )')
        


        return

    def compileLet(self):
        #let
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() == 'let':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "let"')

        #varName
        if self.tokenizer.tokenType() == IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
            self.tokenizer.advance()
        else:
            raise Exception('expected varName identifier')
        
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '[':
            self.output.write('<symbol> [ </symbol>')
            self.output.advance()

            self.compileExpression()

            if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ']':
                self.output.write('<symbol> ] </symbol>')
                self.output.advance()
            else:
                raise Exception('expected symbol ]')

        # equal sign =
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '=':
            self.output.write('<symbol> = </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol =')
        
        #expression
        self.compileExpression()

        #semi-colon ;;;;;;
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ';':
            self.output.write('<symbol> ; </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol ;')

        return

    def compileWhile(self):
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() == 'while':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "while"')

        # (
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ( </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol (')

        #expression
        self.compileExpression()

        # )
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ')':
            self.output.write('<symbol> ) </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol )')

        
        # {
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '{':
            self.output.write('<symbol> { </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol {')

        self.compileStatements()

        # }
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '}':
            self.output.write('<symbol> } </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol }')
        
        return

    def compileReturn(self):
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() == 'return':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "return"')

        #TODO how to give reasonable error messagesf???
        # (expression)?
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ';':
            self.compileExpression()
        
        # ;
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ';':
            self.output.write('<symbol> ; </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol ;')
        
        return

    def compileIf(self):
        
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() == 'if':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "if"')

        # (
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ( </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol (')

        #expression
        self.compileExpression()

        # )
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ')':
            self.output.write('<symbol> ) </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol )')

        
        # {
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '{':
            self.output.write('<symbol> { </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol {')

        self.compileStatements()

        # }
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '}':
            self.output.write('<symbol> } </symbol>')
            self.output.advance()
        else:
            raise Exception('expected symbol }')

        #maybe else
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() == 'else':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
            # {
            if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '{':
                self.output.write('<symbol> { </symbol>')
                self.output.advance()
            else:
                raise Exception('expected symbol {')
            
            self.compileStatements()

            # }
            if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '}':
                self.output.write('<symbol> } </symbol>')
                self.output.advance()
            else:
                raise Exception('expected symbol }')
            
        

        
        return

    #perhaps make a set above to contain all the operators?
    op_set = {'+', '-', '*', '/', '&', '|', '<', '>', '='}
    def compileExpression(self):

        self.compileTerm()

        while self.tokenizer.tokenType == SYMBOL and self.tokenizer.symbol() in op_set:
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>')
            self.tokenizer.advance()
            self.compileTerm()

        return

    key_const_set = {'true', 'false', 'null', 'this'}
    # integerConstant | stringConstant | keywordConstant | varName  | varName[expression] | subroutineCall | (expression) | unary
    def compileTerm(self):
        
        #integerConstant
        if self.tokenizer.tokenType() == INT_CONST:
            self.output.write('<integerConstant> ' + self.tokenizer.intVal() + ' </integerConstant>')
            self.tokenizer.advance()
            return
        
        #stringConstant
        if self.tokenizer.tokenType() == STRING_CONST:
            self.output.write('<stringConstant> ' + self.tokenizer.stringVal() + ' </stringConstant>')
            self.tokenizer.advance()
            return

        #keywordConstant
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() in key_const_set:
            self.output('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>')
            self.tokenizer.advance()
            return

        #varName | varName[expression] | subroutineCall
        if self.tokenizer.tokenType() == IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>')
            self.tokenizer.advance()
            if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '[':
                self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>')
                self.tokenizer.advance()
                
                self.compileExpression()
                
                if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ']':
                    self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>')
                    self.tokenizer.advance()
                else:
                    raise Exception('expected symbol ]')

            return 

        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>')
            self.tokenizer.advance()

            self.compileExpression()

            if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ')':
                self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>')
                self.tokenizer.advance()
            else:
                raise Exception('expected closing symbol )')
            
            return

        
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() in {'-', '~'}:
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>')
            self.tokenizer.advance()
            
            self.compileTerm()

            return



            
        #if we got here, raise exception 

    def compileExpressionList(self):
        
        if self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ')':
            return
        
        
        self.compileExpression()

        while self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ',':
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>')
            self.tokenizer.advance()

            self.compileExpression()

        return
