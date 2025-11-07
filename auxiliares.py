import random

strings = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" , "A"] 

def somajog(cartas_jog):

    nj=cartas_jog.count('J')
    nq=cartas_jog.count('Q')
    na=cartas_jog.count('A')
    nk=cartas_jog.count('K')

    somajoga = nj*10 + nq*10 + na*11 + nk*10
    
    for carta in cartas_jog:
        # ...verifique se ela NÃO é uma figura ou Ás
        if carta not in ['J', 'Q', 'K', 'A']:
            # Se não for, é um número. Converta e some.
            somajoga += int(carta)
    return(somajoga)

def somaban(cartas_banca):

    nj=cartas_banca.count('J')
    nq=cartas_banca.count('Q')
    na=cartas_banca.count('A')
    nk=cartas_banca.count('K')

    somabanca = nj*10 + nq*10 + na*11 + nk*10    


    for carta in cartas_banca:
        # ...verifique se ela NÃO é uma figura ou Ás
        if carta not in ['J', 'Q', 'K', 'A']:
            # Se não for, é um número. Converta e some.
            somabanca += int(carta)
    return(somabanca)
    
def compararbanca(cartas_banca, cartas_jog):

    somabanca = somaban(cartas_banca)
    somajoga = somajog(cartas_jog)

    while somabanca <= 16:
            
            carta_nova = random.choice(strings)
            cartas_banca.append(carta_nova)
            somabanca = somaban(cartas_banca)
    
    if somabanca > 21:

        print('Você ganhou! A banca estourou')
        print("Suas cartas: {}".format(cartas_jog))
        print("Cartas da banca: {}".format(cartas_banca))
    
    elif (somabanca < somajoga) and (somajoga > 21):

        print("Você perdeu")

    else:

        if somabanca > somajoga:
            print("Você perdeu, a banca tem {} pontos.".format(somabanca))
            print("Suas cartas: {}".format(cartas_jog))
            print("Cartas da banca: {}".format(cartas_banca))

        elif somabanca == somajoga:
            print("Empate!")
            print(somabanca, somajoga)
            print("Suas cartas: {}".format(cartas_jog))
            print("Cartas da banca: {}".format(cartas_banca))
        
        else: 
            print("Você venceu, sua pontuação foi: {} pontos!".format(somajoga))
            print("Cartas da banca: {}".format(cartas_banca))


def compracartasjog(cartas_jog):
    
    somajoga = somajog(cartas_jog)
    
    while somajoga <= 20:
        carta_nova = random.choice(strings)
        cartas_jog.append(carta_nova)
        somajoga = somajog(cartas_jog)

        if somajoga < 21:
        
            compra = input('Você possui as seguintes cartas: {} e {} pontos, gostaria de comprar outra carta(Y/N)? '.format(cartas_jog, somajoga)).lower()

            if compra == 'n':
                break
        elif somajoga == 21:

            print('Você ja fez 21!') 
            print(cartas_jog)
            break

        else:
            print('Você comprou cartas demais, passou dos 21 pontos. Sua pontuação foi: {} com as cartas: {}'.format(somajoga, cartas_jog))

            break
    
    return(cartas_jog)
