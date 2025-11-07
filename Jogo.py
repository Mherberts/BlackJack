import random
from regras import blackjack
from auxiliares import compararbanca , compracartasjog

strings = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" , "A"]
cartas_jog = random.choices(strings, k=2)  
cartas_banca = random.choices(strings, k=2)  

def iniciarjogo():

    print(cartas_jog)
    print(cartas_banca[0])
    
    
    if blackjack(cartas_banca):

        print('Você perdeu, a banca tem um BlackJack!')
        print(cartas_banca)

    elif blackjack(cartas_banca) and blackjack(cartas_jog):

        print('Empate! A banca e você tem um Blackjack!')
        print(cartas_banca)

    else:

        if cartas_jog[0] == cartas_jog[1]:
            pergunta = input("Você quer outra carta('hit'), parar('stop'), separar('split') ou dobrar('double')?").lower()
        
            if pergunta == 'stop':
                compararbanca(cartas_banca, cartas_jog)
            
            elif pergunta == 'hit':
                compracartasjog(cartas_jog)
                compararbanca(cartas_banca, cartas_jog)

        else: 
            pergunta = input("Você quer outra carta('hit'), parar('stop') ou dobrar('double')?").lower()
        
            if pergunta == 'stop':
                compararbanca(cartas_banca, cartas_jog)

            elif pergunta == 'hit':
                compracartasjog(cartas_jog)
                compararbanca(cartas_banca, cartas_jog)
