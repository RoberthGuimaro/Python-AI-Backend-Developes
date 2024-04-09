"""
    Objetivo Geral
        - Conhecer os decoradores e como utiliza-los.

    Pré-requisitos
        - Conhecimento básico em Python.

    Percurso
        - Decoradores em Python
""" 

"""
    Recapitulando
        - Funções em Python são objetos de primeira classe. Isso
        significa que as funções podem ser passada e usadas como
        argumentos.

    Inner Functions
        - É possível definir funções dentro de outras funções. Tais
        funções são chamdas de funções internas.

    Retornando Funções de Funções
        - Python também permite que você use funções como valores
        de retorno.

    Açúcar Sintático
        - O Python permite que você use decorados de maneira mais
        simples com o símbolo @.

    Funções de decoração com argumentos
        - Podemos usar *args e **kwargs na função interna, com isso
        ela aceitará um número arbitrário de argumentos posicionais
        e de palavras-chave.

    Retornando valores de funções decoradas
        - O decorador pode decidir se retorna o valor da função
        decorada ou não. Para que o valor seja retornado a função
        de envelope deve retornar o valor da função decorada.

    Introspecção
        - Introspecção é a capacidade de um objeto saber sobre seus
        próprios atributos em tempo de execução.   
"""

def mensagem(nome):
    print('executando nome ')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá tudo bem com você {nome}?'

def executar(funcao, nome):
    print('Executando a funcao executar')
    return funcao(nome)

#print(executar(mensagem, 'joao'))
#print(executar(mensagem_longa, 'joao'))

def principal():
    print('Executando a funcao principal')

    def funcao_interna():
        print('Executando a funcao interna')

    def funcao_2():
        print('Executando a funcao 2')

    funcao_interna()
    funcao_2()

#principal()

def calculadora(operacao):
    def soma(a, b):
        return a+b
    
    def subtracao(a, b):
        return a-b
    
    def multiplicacao(a, b):
        return a*b
    
    def divisao(a, b):
        return a/b
    
    match operacao:
        case "+":
            return soma
        
        case "-":
            return subtracao
        
        case "*":
            return multiplicacao
        
        case "/":
            return divisao
        
#op = calculadora("+")
#print(op(2,3))
#op = calculadora("-")
#print(op(2,3))
#op = calculadora("*")
#print(op(2,3))
#op = calculadora("/")
#print(op(2,3))

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executara funcao.")
        funcao()
        print("Faz algo apos executar a funcao.")

    return envelope

@meu_decorador
def ola_mundo():
    print('Ola mundo')

#ola_mundo()

#def duplicar(func):
#    def envelope(*args, **kwargs):
#        func(*args, **kwargs)
#        func(*args, **kwargs)
#    return envelope

#@duplicar
#def aprender(tecnologia):
#    print(f"Estou aprendendo {tecnologia}")

#aprender("Python")
import functools
def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender('Python')
print(tecnologia)

