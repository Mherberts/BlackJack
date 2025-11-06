import random
from regras import blackjackbanca
from auxiliares import compararbanca

strings = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" , "A"]
cartas_jog = random.choices(strings, k=2)  
cartas_banca = random.choices(strings, k=2)  

def iniciarjogo():

    print(cartas_jog)
    print(cartas_banca[0])
    
    
    if blackjackbanca(cartas_banca):

        print('Você perdeu, a banca tem um BlackJack!')
        print(cartas_banca)

    else:
        pergunta = input("Você quer outra carta('hit'), parar('stop'), separar('split') ou dobrar('double')?").lower()
        
        if pergunta == 'stop':
            compararbanca(cartas_banca, cartas_jog)