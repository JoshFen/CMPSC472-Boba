from Lexer import Lexer

line_num = 0
with open('boba-example.txt') as f:
    while True:
        lexer = Lexer()
        line_num += 1
        line = f.readline()
        if not line:
            break
        else:
            print("line",line)
            tokens = lexer.analyzeLine(line, line_num)
            for token in tokens:
                print(token)
