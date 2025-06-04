import random

#Jogo de ADVINHE O NÚMERO!
print("Bem-vindo ao Guess Number do Chel!")
choice_number = input("Digite um número limite para o desafio:")
if choice_number.isdigit():
   choice_number = int(choice_number)
else:
    print("ERRO: valor informado não é númerico. Digite novamente.")

#Variável que armazena o número randômico
random_number = random.randint(0, choice_number)

#Variável que contabiliza o número de tentativas
n_choices = 0

#loop
while True:
    answer_user = input("Advinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("ERRO: valor informado não é um número. Digite novamente.")
        continue
    n_choices = n_choices + 1
    if answer_user == random_number:
        print(f"Parabéns! Você acertou!!\nVocê tentou {n_choices} vezes até acertar")
        break
    elif answer_user > choice_number:
        print("Você digitou um número maior... Tente mais uma vez aí")
    else:
        print("Você digitou um número menor... Tente mais uma vez aí")




