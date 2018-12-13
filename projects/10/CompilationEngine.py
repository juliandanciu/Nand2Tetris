#Effects the actual compilation output
#the xml tags for compileClass, compile Expression, and compileTerm 
#will be written inside the methods themselves
#it might make sense to do the same for the other compileMethods??
class CompilationEngine:
    

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
        self.output = open(output_stream, 'w')
        self.tokenizer = tokenizer
        #goes to the first token in the stream
        self.tokenizer.advance()
        

    
    #compiles a complete class
    def compileClass(self):
        #class
        self.output.write('<class>\n')

        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() == self.CLASS:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()    
        else:
            raise Exception('EXPEXTED "class"')

        #className
        if self.tokenizer.tokenType() == self.IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected className identifier')
        
        #{
        if self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == '{':
            self.output.write('<symbol> { </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected {')
        
        
        #classVarDec*
        while self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() in {'static', 'field'}:
            self.output.write('<classVarDec>\n')
            self.compileClassVarDec()
            self.output.write('</classVarDec>\n')

        #self.compileSubroutine()
        #subroutineDec*
        while self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() in {'constructor', 'function', 'method'}:
            self.output.write('<subroutineDec>\n')
            self.compileSubroutine()
            self.output.write('</subroutineDec>\n')

        #}
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '}':
            self.output.write('<symbol> } </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected } but found ' +  self.tokenizer.current_token)
        
        self.output.write('</class>\n')
        self.output.close()
        return
    
    def compileVoidOrType(self):
        #type
        if (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'int', 'char', 'boolean', 'void'}):
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        elif (self.tokenizer.tokenType() == 'IDENTIFIER') :
             self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
             print(self.tokenizer.current_token)
             self.tokenizer.advance()
        else:
            raise Exception('expected int, char, boolean, or className')

    def compileType(self):
        #type
        if (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'int', 'char', 'boolean'}):
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        elif (self.tokenizer.tokenType() == 'IDENTIFIER') :
             self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
             print(self.tokenizer.current_token)
             self.tokenizer.advance()
        else:
            raise Exception('expected int, char, boolean, or className')

    def compileClassVarDec(self):
        # ('static' | 'field') 
        if self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'static', 'field'}:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected static or field')
        
        #type
        self.compileType()

        #varName
        if self.tokenizer.tokenType() == 'IDENTIFIER':
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected varName identifier')

        while self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ',':
            self.output.write('<symbol> , </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            if self.tokenizer.tokenType() == 'IDENTIFIER':
                self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
            else:
                raise Exception('expecting identifier varName')

        #;
        if self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ';':
            self.output.write('<symbol> ; </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected ;')

        #this should be handled somewhere else
        #if self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyWord() in {'static', 'field'}:
         #   self.compileClassVarDec()

        return

    def compileSubroutine(self):
        #('constructor' | 'function' | 'method')
        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() in {'constructor', 'function', 'method'}:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected "constructor", "function", or "method"')
        

        #('void' | type)
        self.compileVoidOrType()
        
    
        # subroutineName:identifier
        if self.tokenizer.tokenType() == self.IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected subroutineName identifier')

        


        #(
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ( </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol (')

        
        
        #parameterList:
        self.output.write('<parameterList>\n')
        self.compileParameterList()
        self.output.write('</parameterList>\n')

        #)
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ')':
            self.output.write('<symbol> ) </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol ) but found ' + self.tokenizer.current_token)

        #subroutineBody
        #expect {
        self.output.write('<subroutineBody>\n')
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '{':
            self.output.write('<symbol> { </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol {')
        
        
        #varDec*
        while self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() == 'var':
            self.output.write('<varDec>\n')
            self.compileVarDec()
            self.output.write('</varDec>\n')

        self.output.write('<statements>\n')
        self.compileStatements()
        self.output.write('</statements>\n')

        #expect }
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '}':
            self.output.write('<symbol> } </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol }')

        self.output.write('</subroutineBody>\n')

        return

    def compileParameterList(self):
        #perhaps empty
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ')':
            return
        
        #type
        self.compileType()

        if self.tokenizer.tokenType() == self.IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected varName identifier but found' + self.tokenizer.current_token)

        # comma ,,,,,
        while self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ',':
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            
            self.compileType()

            if self.tokenizer.tokenType() == self.IDENTIFIER:
                self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
            else:
                raise Exception('expected varName identifier but found' + self.tokenizer.current_token)
            
        

        return

    def compileVarDec(self):
        # ('var') 
        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() in {'var'}:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected keyword var')
        
        #type
        self.compileType()

        #varName
        if self.tokenizer.tokenType() == self.IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected varName identifier')

        while self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ',':
            self.output.write('<symbol> , </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            if self.tokenizer.tokenType() == self.IDENTIFIER:
                self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
            else:
                raise Exception('expecting identifier varName')

        #;
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ';':
            self.output.write('<symbol> ; </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected ;')

        
        return
    
    def compileStatements(self):
        
        # statement*

        while self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() in {'let', 'if', 'while', 'do', 'return'}:
            
            if self.tokenizer.keyWord() == 'let':
                self.output.write('<letStatement>\n')
                self.compileLet()
                self.output.write('</letStatement>\n')
            
            if self.tokenizer.keyWord() == 'if':
                self.output.write('<ifStatement>\n')
                self.compileIf()
                self.output.write('</ifStatement>\n')

            if self.tokenizer.keyWord() == 'while':
                self.output.write('<whileStatement>\n')
                self.compileWhile()
                self.output.write('</whileStatement>\n')

            if self.tokenizer.keyWord() == 'do':
                self.output.write('<doStatement>\n')
                self.compileDo()
                self.output.write('</doStatement>\n')

            if self.tokenizer.keyWord() == 'return':
                self.output.write('<returnStatement>\n')
                self.compileReturn()
                self.output.write('</returnStatement>\n')


        return

    def compileDo(self):
        
        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() == 'do':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "do"')

        #subroutineCall

        
        # subroutineName:identifier subroutine name, className or varName
        if self.tokenizer.tokenType() == self.IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected subroutineName, className or varName identifier')

        # .
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '.':
            self.output.write('<symbol> . </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            # subroutineName:identifier
            if self.tokenizer.tokenType() == self.IDENTIFIER:
                self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
            else:
                raise Exception('expected subroutineName identifier')

        elif self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '(':
            #continue
            pass

        else:
            raise Exception('expected symbol ( or .')
        
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol (')

        #expressionList
        self.output.write('<expressionList>\n')
        self.compileExpressionList()
        self.output.write('</expressionList>\n')

        # )
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ')':
            self.output.write('<symbol> ) </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol )')

        #semi-colon ;;;;;;
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ';':
            self.output.write('<symbol> ; </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol ;')
        

        return

    def compileLet(self):
        #let
        
        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() == 'let':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "let"')

        #varName
        if self.tokenizer.tokenType() == self.IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected varName identifier')
        
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '[':
            self.output.write('<symbol> [ </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()

            self.compileExpression()

            if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ']':
                self.output.write('<symbol> ] </symbol>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
            else:
                raise Exception('expected symbol ]')

        # equal sign =
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '=':
            self.output.write('<symbol> = </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol =')
        
        #expression
        self.compileExpression()

        #semi-colon ;;;;;;
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ';':
            self.output.write('<symbol> ; </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol ;')

        return

    def compileWhile(self):
        
        
        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() == 'while':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "while"')

        # (
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ( </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol (')

        #expression
        self.compileExpression()

        # )
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ')':
            self.output.write('<symbol> ) </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol )')

        
        # {
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '{':
            self.output.write('<symbol> { </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol {')

        self.output.write('<statements>\n')    
        self.compileStatements()
        self.output.write('</statements>\n')

        # }
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '}':
            self.output.write('<symbol> } </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol }')
        
        return

    def compileReturn(self):
        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() == 'return':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "return"')

        #TODO how to give reasonable error messagesf???
        # (expression)?
        if self.tokenizer.current_token != ';':
            self.compileExpression()
        
        # ;
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ';':
            self.output.write('<symbol> ; </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol ;')
        
        return

    def compileIf(self):
        
        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() == 'if':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expecting keyword "if"')

        # (
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ( </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol (')

        #expression
        self.compileExpression()

        # )
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ')':
            self.output.write('<symbol> ) </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol )')

        
        # {
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '{':
            self.output.write('<symbol> { </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol {')

        self.output.write('<statements>\n')    
        self.compileStatements()
        self.output.write('</statements>\n')

        # }
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '}':
            self.output.write('<symbol> } </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
        else:
            raise Exception('expected symbol }')

        #maybe else
        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() == 'else':
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            # {
            if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '{':
                self.output.write('<symbol> { </symbol>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
            else:
                raise Exception('expected symbol {')
            
            self.output.write('<statements>\n')    
            self.compileStatements()
            self.output.write('</statements>\n')

            # }
            if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '}':
                self.output.write('<symbol> } </symbol>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
            else:
                raise Exception('expected symbol }')
            
        

        return

    #perhaps make a set above to contain all the operators?
    op_set = {'+', '-', '*', '/', '&', '|', '<', '>', '=', '&lt;', '&gt;', '&amp;'}
    def compileExpression(self):
        self.output.write('<expression>\n')
        self.compileTerm()

        while self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() in self.op_set:
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            self.compileTerm()
        self.output.write('</expression>\n')
        return

    key_const_set = {'true', 'false', 'null', 'this'}
    # integerConstant | stringConstant | keywordConstant | varName  | varName[expression] | subroutineCall | (expression) | unary
    def compileTerm(self):
        self.output.write('<term>\n')
        #integerConstant
        if self.tokenizer.tokenType() == self.INT_CONST:
            self.output.write('<integerConstant> ' + self.tokenizer.intVal() + ' </integerConstant>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            self.output.write('</term>\n')
            return
        
        #stringConstant
        if self.tokenizer.tokenType() == self.STRING_CONST:
            self.output.write('<stringConstant> ' + self.tokenizer.stringVal() + ' </stringConstant>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            self.output.write('</term>\n')
            return

        #keywordConstant
        if self.tokenizer.tokenType() == self.KEYWORD and self.tokenizer.keyWord() in self.key_const_set:
            self.output.write('<keyword> ' + self.tokenizer.keyWord() + ' </keyword>\n')
            self.tokenizer.advance()
            self.output.write('</term>\n')
            return

        #varName | varName[expression] | subroutineCall
        if self.tokenizer.tokenType() == self.IDENTIFIER:
            self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '[':
                self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
                
                self.compileExpression()
                
                if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ']':
                    self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
                    print(self.tokenizer.current_token)
                    self.tokenizer.advance()
                else:
                    raise Exception('expected symbol ]')
            elif self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '(':
                self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()

                self.output.write('<expressionList>\n')
                self.compileExpressionList()
                self.output.write('</expressionList>\n')

                if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ')':
                    self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
                    print(self.tokenizer.current_token)
                    self.tokenizer.advance()
                else:
                    raise Exception('expecting symbol )')
            elif self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '.':
                self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
                
                if self.tokenizer.tokenType() == self.IDENTIFIER:
                    self.output.write('<identifier> ' + self.tokenizer.identifier() + ' </identifier>\n')
                    print(self.tokenizer.current_token)
                    self.tokenizer.advance()
                else:
                    raise Exception('expected an identifer')

                if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '(':
                    self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
                    print(self.tokenizer.current_token)
                    self.tokenizer.advance()

                
                self.output.write('<expressionList>\n')
                self.compileExpressionList()
                self.output.write('</expressionList>\n')

                if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ')':
                    self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
                    print(self.tokenizer.current_token)
                    self.tokenizer.advance()
                else:
                    raise Exception('expecting symbol )')
                


            self.output.write('</term>\n')
            return 

        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == '(':
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()

            self.compileExpression()

            if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ')':
                self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
                print(self.tokenizer.current_token)
                self.tokenizer.advance()
            else:
                raise Exception('expected closing symbol )')
            
            self.output.write('</term>\n')
            return

        
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() in {'-', '~'}:
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()
            
            self.compileTerm()
            
            self.output.write('</term>\n')
            return



            
        #if we got here, raise exception 

    def compileExpressionList(self):
        
        if self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ')':
            return
        
        
        self.compileExpression()

        while self.tokenizer.tokenType() == self.SYMBOL and self.tokenizer.symbol() == ',':
            self.output.write('<symbol> ' + self.tokenizer.symbol() + ' </symbol>\n')
            print(self.tokenizer.current_token)
            self.tokenizer.advance()

            self.compileExpression()

        return
