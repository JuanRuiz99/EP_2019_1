# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:54:18 2019

@author: User
"""
from random import randint

Player_HP=30
Enemy_HP = 30
print ("Você encontra seu professor")
print ("Ele te faz uma proposta: se voce derrotar ele a entrega do EP vai ser adiada")
print ("Se isso não acontecer você morre")
Batalha = input("Você quer batalhar contra seu professor? s/n: ")

if Batalha != "s" and Batalha !="n":
    print ("Comando Inválido")
    Batalha = input("Você quer batalhar? s/n")
while Batalha == "s":
    Player_Damage=randint(10,15)
    Enemy_Damage=randint(10,15)

    if Player_HP<0 and Enemy_HP>0:
        print ("Você perdeu")
        Batalha = "over"
        Game_Over=True    
    elif Player_HP>0 and Enemy_HP<=0:
        print ("Você venceu")
        Batalha = "Over"
    elif Player_HP>0 and Enemy_HP>0:
            Player_HP -= Enemy_Damage
            Enemy_HP -= Player_Damage
            print ("Seu HP é {0} pontos de vida".format(Player_HP))
            print ("O HP do inimigo é {0} pontos de vida".format(Enemy_HP))
            Batalha = input("Continuar Batalhando? s/n")
    elif Player_HP<=0 and Enemy_HP<=0:
        print("Bem, você morreu. Mas não é legal que você tenha levado alguem pra te fazer companhia?")
        Game_Over= True
        Batalha = "over"
    else:
        Batalha ="s"

if Batalha == "Over" :
    print("A batalha acabou, seu professor foi derrotado")
    print("Infelizmente, ele não viveu para atualizar a nova data de entrega do EP no Blackboard")
    print("E ainda mais infelizmente, como você o matou, você está sendo preso por assassinato.")
    print("Parabéns!! Você foi capaz de fazer tudo do pior jeito possivel")
    Game_Over=True
if Batalha == "n":
    print ("Você decide conversar ao invés de lutar")
    print("É super efetivo")
    print("O professor apresenta um argumento lógico sobre o motivo de não poder adiar a entrega do EP")
    print("Mas ao observar que voce optou por não violencia em sua jornada, ele faz uma correção menos criteriosa")
