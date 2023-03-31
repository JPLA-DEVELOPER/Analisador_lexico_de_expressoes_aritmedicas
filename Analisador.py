import re

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Tipo de Token({self.tipo}, {self.valor})" #saida

class AnalisadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.posicao = 0

    def obter_proximo_token(self):
        if self.posicao >= len(self.codigo):
            return Token('FIM', None)

        # Ignorar espaços em branco
        if self.codigo[self.posicao] == ' ':
            self.posicao += 1
            return self.obter_proximo_token()

        # Token de número
        if re.match('\d', self.codigo[self.posicao]):
            valor = ''
            while self.posicao < len(self.codigo) and re.match('\d', self.codigo[self.posicao]):
                valor += self.codigo[self.posicao]
                self.posicao += 1
            return Token('NÚMERO', int(valor))

        # Tokens de operadores
        if self.codigo[self.posicao] in ['+', '-', '*', '/']:
            token = Token('OPERAÇÃO', self.codigo[self.posicao])
            self.posicao += 1
            return token

        # Tokens de parênteses
        if self.codigo[self.posicao] in ['(', ')']:
            token = Token('PARÊNTESES', self.codigo[self.posicao])
            self.posicao += 1
            return token

        # Erro de token desconhecido
        raise ValueError(f"Caractere inválido: {self.codigo[self.posicao]}")



# Teste do analisador léxico
codigo = '42+(675*31)-20925'
analisador = AnalisadorLexico(codigo)

while True:
    token = analisador.obter_proximo_token()
    if token.tipo == 'FIM':
        break
    print(token)
