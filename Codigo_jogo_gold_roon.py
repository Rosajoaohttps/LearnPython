import sys

def exit_game():
    sys.exit(0)

def dead(why):
    print(why, "")
    exit_game()

def Sala_inicio():
    print("\nVocê acorda em uma sala escura.")
    print("Há uma porta à sua direita e outra à sua esquerda.")
    print("Faça sua escolha. (Direita, Esquerda, Esperar)")
    choice = input("> ").strip().lower()
    if choice == "direita":
        sala_demonio()
    elif choice == "esquerda":
        sala_ogro()
    elif choice == "esperar":
        dead("O peso das escolhas o sobrecarregam e você morre.")
    else:
        print("Escolha inválida.")
        Sala_inicio()

def sala_demonio():
    print("\nAo entrar na porta, você encontra um demônio colossal que se apresenta como o comissário do rei do submundo.")
    print("Ele te encara com olhos flamejantes e diz: 'Escolha agora, humano: correr ou morrer?'")
    print("O que você faz? (Correr, Lutar)")
    choice = input("> ").strip().lower()
    if choice == "correr":
        dead("Ele consegue te pegar e o mata facilmente sem resistência, pois estava de costas.")
    elif choice == "lutar":
        print("Você tenta lutar, mas é esmagado pelo poder do demônio.")
        dead("Sua alma é condenada eternamente.")
    else:
        print("Escolha inválida.")
        sala_demonio()

def sala_ogro():
    print("\nAo entrar na sala, você encontra um ogro ancião.")
    print("Ele te cumprimenta e diz que, se você acertar a resposta de sua pergunta, ele o deixará passar. Caso contrário, seu fim será trágico.")
    print("A pergunta é: 'O que é que sempre corre, mas nunca anda? Às vezes murmura, mas nunca fala? Possui um leito, mas nunca dorme? Nasce, mas nunca morre?'")
    print("Qual sua escolha? (Vulcão, Rio, Relâmpago, Vento)")
    choice = input("> ").strip().lower()
    if choice == "rio":
        print("O ogro sorri e diz: 'Resposta correta. Você pode escolher entre duas portas agora: Direita ou Esquerda.'")
        print("Qual você escolhe? (Direita, Esquerda)")
        choice = input("> ").strip().lower()
        if choice == "direita":
            sala_ceu()
        elif choice == "esquerda":
            sala_inferno()
        else:
            print("Escolha inválida.")
            sala_ogro()
    else:
        dead("Você errou. O ogro gentilmente te dá uma pancada na cabeça e você morre.")

def sala_ceu():
    print("\nVocê notou que esta porta possui uma enorme escada para cima.")
    print("Após um caminho árduo, você chega a um lugar estranhamente aconchegante, que lembra um local de paz e luz.")
    print("Lá, você encontra uma entidade que lhe faz uma pergunta.")
    print("A pergunta é: 'O que é leve como uma pluma, mas nenhum homem pode segurá-lo por muito tempo?'")
    print("Escolha sua resposta: (Respiracao, Pó, Sombra, Água)")
    choice = input("> ").strip().lower()
    if choice == "respiracao":
        print("Resposta correta! A entidade sorri e uma porta se materializa à sua frente.")
        print("Ao entrar, você encontra uma lança divina sobre um altar.")
        print("Ao tocar nela, você perde a consciência e acorda novamente na sala inicial.")
        sala_inicial_final_ceu()
    else:
        dead("Sua resposta é incorreta. O chão se abre e você cai no abismo.")

def sala_inferno():
    print("\nVocê notou que esta porta possui uma enorme escada para baixo.")
    print("Após um caminho árduo, você chega a um lugar aberto, escuro e muito quente, cercado por labaredas de fogo.")
    print("Lá, você encontra um ser humanoide que lhe faz uma pergunta.")
    print("A pergunta é: 'O que é mais poderoso do que Deus, mais maligno do que o Diabo, os pobres têm e os ricos precisam?'")
    print("Escolha sua resposta: (Nada, Dinheiro, Poder, Inveja)")
    choice = input("> ").strip().lower()
    if choice == "nada":
        print("Resposta correta! A entidade se curva e aponta para uma porta com uma capa flamejante atrás dela.")
        sala_capa_flamejante()
    else:
        dead("Sua resposta é incorreta. O ser humanoide ri e o consome nas chamas.")

def sala_capa_flamejante():
    print("\nVocê se aproxima da porta e vê uma capa flamejante pendurada atrás dela.")
    print("A capa emite um calor intenso, mas parece segura de alguma forma.")
    print("O que você faz? (Tocar na capa, Ignorar)")
    choice = input("> ").strip().lower()
    if choice == "tocar na capa":
        print("Ao tocar na capa flamejante, você sente uma energia intensa e é transportado de volta para a sala inicial.")
        sala_inicio_modificada()
    elif choice == "ignorar":
        print("Você decide não tocar na capa e retorna para a sala anterior.")
        sala_inferno()
    else:
        print("Escolha inválida.")
        sala_capa_flamejante()

def sala_inicio_modificada():
    print("\nVocê acorda novamente na sala escura onde tudo começou.")
    print("Desta vez, há apenas uma porta à sua esquerda.")
    print("A porta à esquerda leva ao demônio.")
    print("Faça sua escolha. (Esquerda)")
    choice = input("> ").strip().lower()
    if choice == "esquerda":
        sala_demonio_final_inferno()
    else:
        print("Escolha inválida.")
        sala_inicio_modificada()

def sala_demonio_final_inferno():
    print("\nVocê entra na sala final, que é envolta em escuridão e fogo.")
    print("No centro da sala, há um trono feito de ossos e chamas.")
    print("O ser humanoide que lhe deu a capa flamejante aparece, mas desta vez, ele é mais poderoso.")
    
    print("\nEle diz: 'Você retornou, mas agora está no meu domínio final.'")
    print("O que você faz? (Enfrentar, Subjugar, Usar a capa)")
    choice = input("> ").strip().lower()
    if choice == "enfrentar":
        print("Você tenta usar a capa flamejante para lutar, mas o ser é muito forte.")
        dead("Sua alma é consumida pelo ser, e você se torna parte do submundo para sempre.")
    elif choice == "subjugar":
        print("Você decide usar o poder da capa flamejante para subjugá-lo.")
        print("No entanto, ao subjugá-lo, você sente que o poder da capa está corroendo sua própria essência.")
        print("Você derrota o ser, mas percebe que se tornou um novo governante do inferno.")
        dead("Você venceu, mas ao custo de sua própria alma. Agora, você é o novo senhor das trevas.")
    elif choice == "usar a capa":
        print("Você veste a capa flamejante, sentindo uma energia intensa que protege e fortalece seu corpo.")
        print("Com a capa, você consegue enfrentar o ser humanoide e, após uma batalha épica, derrota-o completamente.")
        print("O trono de ossos e chamas desmorona, e uma porta com a inscrição 'Liberdade' aparece.")
        print("Você caminha até a porta e a atravessa, sentindo que finalmente escapou do inferno.")
        print("Parabéns! Você venceu o jogo e conquistou sua liberdade!")
        exit_game()
    else:
        print("Escolha inválida.")
        sala_demonio_final_inferno()
def sala_inicial_final_ceu():
    print("\nVocê acorda novamente na sala escura onde tudo começou.")
    print("Desta vez, há apenas uma porta à sua esquerda.")
    choice = input("> ").strip().lower()
    if choice == "esquerda":
        sala_demonio_final_ceu()
    else:
        print("Escolha inválida.")
        sala_inicial_final_ceu()

def sala_demonio_final_ceu():
    print("\nAo entrar na porta, você percebe que o demônio colossal está lá novamente.")
    print("Desta vez, a lança que você encontrou começa a vibrar em sua mão, ansiosa para atacar.")
    print("Você tem duas escolhas: correr, lutar ou subjulgar o demônio. O que você faz? (Correr, Lutar, Subjugar)")
    choice = input("> ").strip().lower()
    if choice == "correr":
        dead("Ele consegue te pegar e o mata facilmente sem resistência, pois estava de costas.")
    elif choice == "lutar":
        print("A lança brilha intensamente, mas o poder do demônio é avassalador.")
        dead("Apesar de seus esforços, você não consegue derrotar o demônio.")
    elif choice == "subjugar":
        print("Você decide subjulgar o demônio, usando a lança divina para controlar seu poder.")
        print("A lança brilha intensamente e você ganha um enorme poder, subjugando o demônio.")
        print("Uma porta aparece à sua frente com a inscrição 'Saída'.")
        print("Você venceu o jogo e conquistou sua liberdade!")
        exit_game()
    else:
        print("Escolha inválida.")
        sala_demonio_final_ceu()

def sala_ceu_final():
    print("\nVocê se encontra em um reino celestial com uma paisagem deslumbrante.")
    print("À sua frente, há um ser angelical que lhe dá uma missão final.")
    print("O ser angelical explica que você deve enfrentar uma prova final usando a lança divina.")
    print("Você vê duas figuras imponentes à sua frente, representando o bem e o mal.")
    print("Escolha sabiamente como usar a lança: (Bem, Mal)")
    choice = input("> ").strip().lower()
    if choice == "bem":
        print("Você usa a lança divina para combater as forças malignas que ameaçam o reino celestial.")
        print("Sua coragem e justiça são recompensadas, e o reino é restaurado à paz.")
        print("Uma porta dourada se abre, levando você a um lugar de eterna felicidade e realização.")
        print("Parabéns! Você venceu o jogo e conquistou a paz eterna no céu!")
        exit_game()
    elif choice == "mal":
        print("Você usa a lança divina para enfrentar as forças do bem, buscando poder e dominação.")
        print("No entanto, seu coração é corrompido e você acaba traindo seus próprios princípios.")
        print("O reino celestial se desmorona ao seu redor, e você é banido para um destino sombrio.")
        dead("Sua jornada termina em tragédia devido à sua escolha corrompida.")
    else:
        print("Escolha inválida.")
        sala_ceu_final()

def sala_demonio_final_ceu():
    print("\nAo entrar na porta, você percebe que o demônio colossal está lá novamente.")
    print("Desta vez, a lança que você encontrou começa a vibrar em sua mão, ansiosa para atacar.")
    print("Você tem três escolhas: correr, lutar ou subjulgar o demônio. O que você faz? (Correr, Lutar, Subjugar)")
    choice = input("> ").strip().lower()
    if choice == "correr":
        dead("Ele consegue te pegar e o mata facilmente sem resistência, pois estava de costas.")
    elif choice == "lutar":
        print("A lança brilha intensamente, e você usa seu poder para enfrentar o demônio.")
        print("Após uma batalha épica, você derrota o demônio.")
        print("Uma porta se abre com a inscrição 'Liberdade'.")
        print("Você caminha até a porta e a atravessa, sentindo que finalmente escapou do inferno.")
        print("Parabéns! Você venceu o jogo e conquistou sua liberdade!")
        exit_game()
    elif choice == "subjugar":
        print("Você decide subjulgar o demônio, usando a lança divina para controlar seu poder.")
        print("O demônio se submete à sua vontade, e uma nova porta aparece com a inscrição 'Saída'.")
        print("Você atravessa a porta, finalmente escapando do inferno.")
        print("Parabéns! Você venceu o jogo e conquistou sua liberdade!")
        exit_game()
    else:
        print("Escolha inválida.")
        sala_demonio_final_ceu()


Sala_inicio()
# Início do jogo
Sala_inicio()
