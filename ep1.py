# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Juan Greco Ruiz, juangr@al.insper.edu.br
# - aluno B: Giovanni Augustho Rozatti, giovanniar@al.insper.edu.br

import random

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "fablab": "Mudar de prédio e ir até o FabLab",
                #"sala 404": "Tomar o elevador para o 4 andar e procurar pela Sala 404"# ----- SALA SECRETA----
                
            }
        },
        "sala misteriosa": {
                "titulo": "Sala teleportadora",
                               "descricao": "Voce entra em uma sala pequena com nada alem de uma maquina com um portal no centro",
                               "opcoes": { 
                                       "keypad": "Arriscar e digitar o nome da sala no keypad antes de entrar no portal",
                                       "biblioteca": "Retornar a biblioteca"
           }
       },
            
            
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "sala misteriosa": "Abrir uma porta sombria em um canto obscuro da biblioteca" 

            }
        },
        'fablab': {
            'titulo': 'Oficina de milagres',
            'descricao': 'Um lugar para a criação de objetos poderosos, nela podem ser aperfeiçoados os conhecimentos de Dym ("Introdução à engenharia", de NatDes)',
            'opcoes': {
                'inicio': 'Sai da oficina e retorna ao inicio'
                    }
                },
        'Limbo': {
            'titulo': 'sala 404',
            'descricao': 'Apenas a entrada foi encontrada, mas supostamente é o laboratório de computação',
            'opcoes': {
                'entrar sala 404': 'você entra na sala', 
                'inicio': 'Voce ignora a sala e volta para o saguao'
                    }
                },
            
        "entrar sala 404": {
            "titulo": "Great White",
            "descricao": "Ao entrar na sala tudo se transforma em branco e a porta desaparece em um piscar de olhos. "
                        "Voce se perdeu no Limbo e ficara flutuando no 'Great White' para os restos de seus dias.",
            "opcoes": {}
       },
            
            
        'aquários': {
            'titulo': 'Aquarium',
            'descricao': 'Lugar isolado do espaço-tempo, microcosmo dotado de suas próprias regras',
            'opçoes': {
                    'trabalhar': 'Trabalhar no EP furiosamente ate 23:59:59',
                    'inicio': 'Sair do aquarium e voltar para o inicio'
                    }
                    }
            }
            
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        if nome_cenario_atual != 'inicio': #impossivel ser atacado indo para o saguao, pois ele funciona como uma "safe zone"
            chance_batalha = random.randint(1,100)
            if chance_batalha > 70:
                print("\n----------Um veterano selvagem apareceu! Prepare-se para batlha!----------\n")
                
        

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
        titulo_cenario= cenario_atual["titulo"]
        print('\n',titulo_cenario)
        
        num_de_traco = "-" * len(titulo_cenario)
        print(num_de_traco)
        
        descricao_cenario= cenario_atual["descricao"]
        print(descricao_cenario)
        
        print("Escolha sua opção:\n")

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
           
            print('\n'.join("{}: {}".format(k, v) for k, v in opcoes.items()))
        
            escolha = input("O que você quer fazer?: ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
                if escolha == 'keypad':
                    escolha2 = input("Digite o nome da sala em que quer teleportar: ")
                    encontrou_titulo=True
                    for dic1, dic2 in cenarios.items():
                        if escolha2 == dic2["titulo"]:      
                            print("----------Deu certo! Se segure!----------")
                            nome_cenario_atual = dic1
                            encontrou_titulo = False

                    if encontrou_titulo == True:
                        print("Errou o nome da sala e foi teleportado para o espaco!")
                        game_over = True
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
