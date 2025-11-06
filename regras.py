def blackjackbanca(mao):
    
    cartas_10 = {"10", "J", "Q", "K"}
    return ("A" in mao) and any(c in cartas_10 for c in mao)

def printregras():

    
    print('''    🎯 REGRAS DO BLACKJACK 🎯
    - O objetivo é chegar o mais próximo possível de 21 pontos.
    - Ás vale 1 ou 11.
    - J, Q e K valem 10.
    - Se passar de 21, você perde.''')