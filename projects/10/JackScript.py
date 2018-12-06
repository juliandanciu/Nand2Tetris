from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine


tok = JackTokenizer('ArrayTest/MainTest.jack')

engine = CompilationEngine(tok,'output_stream')

