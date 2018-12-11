from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine


tok = JackTokenizer('Square/Square.jack')

#engine = CompilationEngine(tok,'output_stream.xml')

engine.compileClass()

