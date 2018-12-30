import sys
import os
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine
from VMWriter import VMWriter


jack_files = []

if os.path.isdir(sys.argv[1]):
    #for all .jack files in the 
    for file in os.listdir(sys.argv[1]):
        if file.endswith('.jack'):
            jack_files.append(sys.argv[1] + '/' + file)  
else:
    if sys.argv[1].endswith('.jack'):
        jack_files.append(sys.argv[1])
    

    
for jack_file in jack_files:
    tok = JackTokenizer(jack_file)
    jack_file_base = jack_file.replace('.jack', '')
    vm_writer = VMWriter(jack_file.replace('.jack', '.vm'))
    engine = CompilationEngine(tok, jack_file.replace('.jack', '.xml'), vm_writer)
    engine.compileClass()


