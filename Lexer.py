from Token import Token
# A dictionary object is used to determine if a token is a reserved word

class Lexer:


    def __init__(self):
        self.tokens = []
        self.input = "" 
        self.index = 0
        self.line_number = 0
        self.current_char = input[self.index]
        self.reserved_words = {
            "bubbles": Token.TokenType.BUBBLES,
            "syrup": Token.TokenType.SYRUP,
            "flavor": Token.TokenType.FLAVOR,
            "drink": Token.TokenType.DRINK,
            "condition": Token.TokenType.CONDITION,
            "tea": Token.TokenType.TEA,
            "withBubbles": Token.TokenType.WITH_BUBBLES,
            "withoutBubbles": Token.TokenType.WITHOUT_BUBBLES,
            ";": Token.TokenType.SEMI_COLON,
            "[": Token.TokenType.LEFT_BRACKET,
            "]": Token.TokenType.RIGHT_BRACKET,
            "{": Token.TokenType.LEFT_CURLY,
            "}": Token.TokenType.RIGHT_CURLY,
            "(": Token.TokenType.LEFT_PARENTHESIS,
            ")": Token.TokenType.RIGHT_PARENTHESIS,
            "\"": Token.TokenType.QUOTATION,
            "+": Token.TokenType.PLUS,
            "-": Token.TokenType.MINUS,
            "*": Token.TokenType.MULTIPLY,
            "/": Token.TokenType.DIVIDE,
            "=": Token.TokenType.EQUAL,
            "!-": Token.TokenType.NOT_EQUAL,
            "==": Token.TokenType.CONDITIONAL_EQUAL,
            ">": Token.TokenType.GREATER,
            "<": Token.TokenType.LESS,
            ">=": Token.TokenType.GREATER_OR_EQUAL,
            "<=": Token.TokenType.LESS_OR_EQUAL,
            "variable": Token.TokenType.VARIABLE
        }

    def analyzeLine(self, input_line, line_number):
        self.getNextToken()
        return self.tokens


    # advances to the next position of a character in the input stream
    def advance(self):
        self.index += 1
        if self.index >= len(self.input):
            self.current_char = 0
        else:
            self.current_char = self.input[sself.index]

    # method that jumps through the white spaces in the input stream
    def skipWhiteSpace(self):
        while self.current_char != 0 and self.current_char.isspace():
            self.advance()

    def isOperator(self, char):
        if char == '+':
            self.advance()
            return Token(Token.TokenType.PLUS, self.line_number, (self.current_char - len(char)), len(char))
        if char == '-':
            self.advance()
            return Token(Token.TokenType.MINUS, self.line_number, (self.current_char - len(char)), len(char))
        if char == '*':
            self.advance()
            return Token(Token.TokenType.MULTIPLY, self.line_number, (self.current_char - len(char)), len(char))
        if char == '/':
            self.advance()
            return Token(Token.TokenType.DIVIDE, self.line_number, (self.current_char - len(char)), len(char))
        if char == '(':
            self.advance()
            return Token(Token.TokenType.LEFT_PARENTHESIS, self.line_number, (self.current_char - len(char)), len(char))
        if char == ')':
            self.advance()
            return Token(Token.TokenType.RIGHT_PARENTHESIS, self.line_number, (self.current_char - len(char)), len(char))
        if char == '{':
            self.advance()
            return Token(Token.TokenType.LEFT_CURLY, self.line_number, (self.current_char - len(char)), len(char))
        if char == '}':
            self.advance()
            return Token(Token.TokenType.RIGHT_CURLY, self.line_number, (self.current_char - len(char)), len(char))
        if char == '[':
            self.advance()
            return Token(Token.TokenType.LEFT_BRACKET, self.line_number, (self.current_char - len(char)), len(char))
        if char == ']':
            self.advance()
            return Token(Token.TokenType.RIGHT_BRACKET, self.line_number, (self.current_char - len(char)), len(char))
        if char == '\"':
            self.advance()
            return Token(Token.TokenType.QUOTATION, self.line_number, (self.current_char - len(char)), len(char))
        if char == ";":
            self.advance()
            return Token(Token.TokenType.SEMI_COLON, self.line_number, (self.current_char - len(char)), len(char))

    def isNotQuote(self):
        if self.current_char == "\"":
            return False
        else:
            return True
        
    def getNextToken(self):
        while self.current_char != 0:
            if self.current_char.isspace():
                self.skipWhiteSpace()
                continue
            if self.current_char.isalpha():
                cur = ""
                while self.current_char.isalnum():
                    cur += self.current_char
                    self.advance()
                if cur in self.reserved_words:
                    self.tokens.append(Token(self.reserved_words[cur], self.line_number, (self.current_char - len(cur)), len(cur)))
                else:
                    self.tokens.append(Token(self.reserved_words["variable"], self.line_number, (self.current_char - len(cur)), len(cur)))
            else:
                self.tokens.append(self.current_char)
                if(input[self.index - 1] == "\""):
                    while self.isNotQuote():
                        cur = ""
                        while self.current_char.isalnum():
                            cur += self.current_char
                            self.advance()
                        self.tokens.append(Token(Token.TokenType.STRING_LITERAL, (self.current_char - len(cur)), len(cur)))

            print("Error: unexpected character '" + self.current_char + "' at index " + str(self.index))
            return Token(Token.TokenType.EOF, "")
        return Token(Token.TokenType.EOF, "")