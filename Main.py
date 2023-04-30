from Lexer import Lexer
from Interpreter import Interpreter

line_num = 0
with open('boba-example.txt') as f:
    all_tokens = []
    while True:
        lexer = Lexer()
        line_num += 1
        line = f.readline()
        if not line:
            break
        else:
            #print("line",line)
            print()
            print("Line Number: ", line_num)
            tokens = lexer.analyzeLine(line, line_num)
            all_tokens += tokens
            
            for token in tokens:
                print(token)
    # for t in all_tokens:
    #     print(t.value)
    Interpreter.interpret(all_tokens)
