from JackTokenizer import JackTokenizer
#from CompilationEngine import CompilationEngine



'''
public api of tokenizer:
hasMoreTokens()
advance()
tokenType()
keyWord()
symbol()
identifier()
intVal
stringVal()
'''
tokenizer = JackTokenizer('ArrayTest/MainTest.jack')

tokenTypeTagMap = {
    'KEYWORD' : "keyword",
    'SYMBOL' : 'symbol',
    'INT_CONST' : 'integerConstant',
    'STRING_CONST' : 'stringConstant',
    'IDENTIFIER': 'identifier'
}

f = open('McTest.xml', 'w')
f.write('<tokens>\n')
tokenizer.advance()
while tokenizer.hasMoreTokens():
    
    f.write('<' + tokenTypeTagMap.get(tokenizer.tokenType()) + '> ')
    f.write(tokenizer.current_token)
    f.write(' </' + tokenTypeTagMap.get(tokenizer.tokenType()) + '>\n')
    tokenizer.advance()

f.write('</tokens>')
f.close()

