import random
from regras import printregras
from Jogo import iniciarjogo

print('===BLACKJACK===')

while True:
    inicio = input("Para começar, digite o que você deseja. Para regras, digite 'rules' , para começar o jogo digite 'start': ").lower()
    if inicio == "rules":
        printregras()
    elif inicio == "start":
        iniciarjogo()
        break
    else:
        print("Comando inválido, tente novamente.")
    
    

