from enum import Enum

class Token:
    
    def __init__(self, token_type, position: int, line: int, length: int):
        self.token_type = token_type
        self.position = position
        self.line = line
        self.length = length

    def __str__(self) -> str:
        return "Token: " + self.token_type + " Line: " + self.line + " Position: " + self.position + " Length: " + self.length 
        
    def get_token_type(self):
        return self.token_type
    
    def get_position(self) -> int:
        return self.position
    
    def get_length(self) -> int:
        return self.length

    class TokenType(Enum):
        BUBBLES = 'bubbles',
        SYRUP = 'syrup',
        FLAVOR = 'flavor',
        DRINK = 'drink',
        CONDITION = 'condition',
        TEA = 'tea',
        WITH_BUBBLES = 'withBubbles',
        WITHOUT_BUBBLES = 'withoutBubbles',
        SEMI_COLON = ';',
        LEFT_BRACKET = '[',
        RIGHT_BRACKET = ']',
        LEFT_CURLY = '{',
        RIGHT_CURLY = '}',
        LEFT_PARENTHESIS = '(',
        RIGHT_PARENTHESIS = ')',
        QUOTATION = '"',
        PLUS = '+',
        MINUS = '-',
        MULTIPLY = '*',
        DIVIDE = '/',
        EQUAL = '=',
        NOT_EQUAL = '!='
        CONDITIONAL_EQUAL = '==',
        GREATER = '>',
        LESS = '<',
        GREATER_OR_EQUAL = '>=',
        LESS_OR_EQUAL = '<=',
        VARIABLE = '[a-zA-Z]'
            
        