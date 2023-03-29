class Lexer:

    def __init__(self, line) -> None:
        input = line
        index = 0
        curChar = input[0]

    def advance(self):
        self.index += 1
        if (self.index >= len(input)):
            self.curChar = 0
        else:
            self.curChar = input[self.index]

    def skip_whitespace(self):
        while (self.curChar != 0 and self.curChar != ' '):
            self.advance()
        
        

        keywords = {}
        keywords['bubbles'] = {"Type", "bool"}
        keywords['syrup'] = {"Type", ""}
        keywords['flavor'] = {"Type"}
        keywords['condition'] = {"Conditional", ''}
        keywords[]


    def get_next_token():

