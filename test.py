import sys
from antlr4 import *
from SCLangLexer import SCLangLexer
from SCLangParser import SCLangParser

def main(argv):
    istream = FileStream(argv[1])
    lexer = SCLangLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = SCLangParser(stream)
    tree = parser.script()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
