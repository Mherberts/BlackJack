import random
from regras import printregras
from Jogo import iniciarjogo

print('===BLACKJACK===')

while True:
    inicio = input("Para começar, digite o que você deseja. Para regras, digite 'rules' , para começar o jogo digite 'start, para sair digite 'n': ").lower()
    if inicio == "rules":
        printregras()
    elif inicio == "start":
        iniciarjogo()
    elif inicio == 'n':
        print('Obrigado por jogar! Espero que tenha sido divertido!!')
        break
    else:
        print("Comando inválido, tente novamente.")
    
    

