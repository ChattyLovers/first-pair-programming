import random

frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']

print('Bem vindo ao jogo de adivinhação')

fruta = random.choice(frutas)
acabou = False

while not acabou:
    print(" _ " * len(fruta))
    letra = input('Digite uma letra: ')
    print(letra in fruta)
    print("errou")