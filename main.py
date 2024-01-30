player = input("Qual você escolhe? 0 Pedra, 1 Papel ou 2 Tesoura\n")

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

list_random = [pedra, papel, tesoura]
num_items = len(list_random)

machine_random = random.randint(0, 2)

if player == "0":
    print(f"Você escolheu\n{pedra}")
    if machine_random == 0:
        print(f"Maquina Escolheu \n\n{pedra}\n\nvocê empatou ")
    elif machine_random == 1:
        print(f"Maquina Escolheu \n\n{papel}\n\nvocê perdeu")
    else:
        print(f"Maquina Escolheu \n\n{tesoura}\n\nvocê ganhou")
if player == "1":
    print(f"Você escolheu\n{papel}")
    if machine_random == 0:
        print(f"Maquina Escolheu \n\n{pedra}\n\nvocê ganhou ")
    elif machine_random == 1:
        print(f"Maquina Escolheu \n\n{papel}\n\nvocê empatou")
    else:
        print(f"Maquina Escolheu \n\n{tesoura}\n\nvocê perdeu")
if player == "2":
    print(f"Você escolheu\n{tesoura}")
    if machine_random == 0:
        print(f"Maquina Escolheu \n\n{pedra}\n\nvocê perdeu ")
    elif machine_random == 1:
        print(f"Maquina Escolheu \n\n{papel}\n\nvocê ganhou")
    else:
        print(f"Maquina Escolheu \n\n{tesoura}\n\nvocê empatou")





