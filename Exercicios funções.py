
'''
1.Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma de três argumentos.
'''
'''
def soma():
    n1 = input('Digite o 1° valor: ')
    n2 = input('Digite o 2° valor: ')
    n3 = input('Digite o 3° valor: ')
    try:
        soma = float(n1)+float(n2)+float(n3)
        print(soma)
    except ValueError as e:
        print(f'Erro: O tipo do dado informado está incorreto. \n Detalhes: {e}')
'''
#soma()

'''
2. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127->721.
'''
'''
def reverso():
    n = input('Digite um valor: ')
    try:
        n = int(n)
        n_rev = ''
        n = str(n)
        for x in n:
            n_rev += n[-1]
            n = n[:-1]
        print(n_rev)
    except ValueError as e:
        print(f'Erro: O tipo do dado informado está incorreto. \n Detalhes: {e}')
'''
#reverso()

'''
3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa.
Para cada opção, crie uma função.
'''
'''
def converter():
    comando_temp = input('Digite F para converter uma temperatura de Graus Celsius para Graus Fahrenheit \n Ou ' 
                       'Digite C para converter uma temperatura de Graus Fahrenheit para Graus Celsius: ')
    temp = float(input(f'Digite a temperatura em °{comando_temp.upper()} que deseja converter? '))
    try:
        if comando_temp.lower() == 'f':
            f = (5/9)*temp+32
            print(f'A temperatura de {temp:.1f}°C equivale a {f:.1f}°F') 
        elif comando_temp.lower() == 'c':
            c = (9/5)*(temp-32)
            print(f'A temperatura de {temp:.1f}°F equivale a {c:.1f}°C')
        else:
            print('Erro: O tipo de comando informado não existe!')
    except ValueError as e:
        print(f'Erro: O tipo do dado informado está incorreto. \n Detalhes: {e}')
'''
#converter()

'''
Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.
'''

'''
def converte_para_celsius(temp):
    c = (9/5)*(temp-32)
    print(f'A temperatura de {temp:.1f}°F equivale a {c:.1f}°C')

def converte_para_fahrenheit(temp):
    f = (5/9)*temp+32
    print(f'A temperatura de {temp:.1f}°C equivale a {f:.1f}°F') 

comando_temp = input('Digite F para converter uma temperatura de Graus Celsius para Graus Fahrenheit \n Ou ' 
                       'Digite C para converter uma temperatura de Graus Fahrenheit para Graus Celsius: ')
temp = float(input(f'Digite a temperatura em °{comando_temp.upper()} que deseja converter? '))
try:
    if comando_temp.lower() == 'f':
        converte_para_fahrenheit(temp)
    elif comando_temp.lower() == 'c':
        converte_para_celsius(temp)
    else:
        print('Erro: O tipo de comando informado não existe!')
except ValueError as e:
    print(f'Erro: O tipo do dado informado está incorreto. \n Detalhes: {e}')
'''

'''
4.Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano:vR$4,91
Peso Argentino: R$0,02
Dólar Australiano: R$3,18
Dólar Canadense: R$3,64
Franco Suiço: R$0,42
Euro: R$5,36
Libra esterlina: R$6,21
'''

'''
dinheiro = float(input('Digite quanto em R$ você possui na carteira para descobrir quanto teria em outras moedas: '))

try:
    print('O valor de R${dinheiro} é correspondente em outras moedas a: ')
    dolar_americano = dinheiro*4.91
    print(f'{dolar_americano} dolares americanos.')
    peso_argentino = dinheiro*0.02
    print(f'{peso_argentino} pesos argentinos.')
    dolar_australiano = dinheiro*3.18
    print(f'{dolar_australiano} dolares australianos.')
    dolar_canadense = dinheiro*3.64
    print(f'{dolar_canadense} dolares canadenses.')
    franco_suico = dinheiro*0.42
    print(f'{franco_suico} francos suíços.')
    euro = dinheiro*5.36
    print(f'{euro} euros.')
    libra_esterlina = dinheiro*6.21
    print(f'{libra_esterlina} libras esterlinas.')
except ValueError as e:
    print(f'Erro: O tipo do dado informado está incorreto. \n Detalhes: {e}')
'''

'''
5. Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais na 
string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.
'''
'''
def conta_vogais(frase):
    lista_vogais = ['a','e','i','o','u']
    n = 0
    for letra in frase:
        if letra.lower() in lista_vogais:
            n+=1
    print(f'O número de vogais na "{frase}" é {n}.')
'''
#frase = input('Digite um frase para descobrir quantas vogais existem na frase: ')
#conta_vogais(frase)

'''
6. Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. A palavra secreta
será representada por espaços em branco, um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. Em cada 
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posiçõe
 correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador
 perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
 Dica: Você precisará importar uma biblioteca para resolver esse exercício
'''
import random

lista = ['morango','carro','vento','helicoptero','salto','laranja','vaca','boi']

palavra_secreta = random.choice(lista)

descubra = '_' * len(palavra_secreta)

print(f'A palavra secreta tem {len(palavra_secreta)} letras.')

tentativas = 0

while tentativas <= 6 and palavra_secreta != descubra:
    letra = input('Digite uma letra: ')

    if letra in palavra_secreta:
        for x, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                descubra = descubra[:x] + letra + descubra[x+1:]
    else:
        print(f'Errou! A letra {letra} não existe na palavra secreta')
        tentativas += 1

    print(descubra)

if palavra_secreta == descubra:
    print(f'Você acertou! A palavra secreta é: {palavra_secreta}')
else:
    print(f'Você errou! A palavra secreta era: {palavra_secreta}')

