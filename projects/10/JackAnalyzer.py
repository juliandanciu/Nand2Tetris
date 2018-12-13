import sys
import os
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine


jack_files = []

if os.path.isdir(sys.argv[1]):
    print('directory alert')
    print(sys.argv[1])
    #for all .jack files in the 
    for file in os.listdir(sys.argv[1]):
        if file.endswith('.jack'):
            jack_files.append(sys.argv[1] + '/' + file)  
else:
    print('single file alert')
    print(sys.argv[1])
    if sys.argv[1].endswith('.jack'):
        jack_files.append(sys.argv[1])
    

print(jack_files)

    
for jack_file in jack_files:
    if jack_file.endswith('.jack'):
        print(jack_file)
        tok = JackTokenizer(jack_file)
        engine = CompilationEngine(tok, jack_file.replace('.jack', '.xml'))
        engine.compileClass()


