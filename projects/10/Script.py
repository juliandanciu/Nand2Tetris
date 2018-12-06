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