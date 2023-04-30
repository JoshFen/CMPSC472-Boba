from Token import Token

class Interpreter:
    
    def interpret(token_list: list) -> None:
        index = 0
        while (index < len(token_list)):       
            statement = ''       
            is_executable = False 
            sub_statement = ''       
            while (not is_executable and index < len(token_list)):
                token = token_list[index]          
                match token.token_type:
                    case Token.TokenType.BUBBLES:
                        pass
                    case Token.TokenType.FLAVOR:
                        pass
                    case Token.TokenType.SYRUP:
                        pass
                    case Token.TokenType.LEFT_BRACKET:
                        statement += '['
                    case Token.TokenType.RIGHT_BRACKET:
                        statement += ']'
                    case Token.TokenType.LEFT_PARENTHESIS:
                        statement += '('
                    case Token.TokenType.RIGHT_PARENTHESIS:
                        statement += ')'
                    case Token.TokenType.LEFT_CURLY:
                        statement += ':'
                    case Token.TokenType.RIGHT_CURLY:
                        is_executable = True
                    case Token.TokenType.QUOTATION:
                        statement += '"'
                    case Token.TokenType.PLUS:
                        statement += '+'
                    case Token.TokenType.MINUS:
                        statement += '-'
                    case Token.TokenType.MULTIPLY:
                        statement += '*'
                    case Token.TokenType.DIVIDE:
                        statement += '/'
                    case Token.TokenType.EQUAL:
                        statement += '='
                    case Token.TokenType.NOT_EQUAL:
                        statement += '!='
                    case Token.TokenType.CONDITIONAL_EQUAL:
                        statement += '=='
                    case Token.TokenType.GREATER:
                        statement += '>'
                    case Token.TokenType.LESS:
                        statement += '<'
                    case Token.TokenType.GREATER_OR_EQUAL:
                        statement += '>='
                    case Token.TokenType.LESS_OR_EQUAL:
                        statement += '<='
                    case Token.TokenType.VARIABLE:
                        statement += token.value
                    case Token.TokenType.INTEGER:
                        statement += token.value
                    case Token.TokenType.STRING_LITERAL:
                        statement += token.value
                    case Token.TokenType.WITH_BUBBLES:
                        statement += 'True'
                    case Token.TokenType.WITHOUT_BUBBLES:
                        statement += 'False'
                    case Token.TokenType.CONDITION:
                        statement += 'if'
                    case Token.TokenType.TEA:
                        statement += 'print'
                    case Token.TokenType.EOF:
                        statement += ''
                    case Token.TokenType.SEMI_COLON:
                        if '{'  not in statement:
                          is_executable = True
                index += 1
            exec(statement)
            
                  