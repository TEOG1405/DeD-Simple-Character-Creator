import random


racas = ["Humano", "Elfo", "Anão", "Halfling", "Tiefling", "Meio-Orc", "Meio-Elfo"]
classes = ["Guerreiro", "Mago", "Ladino", "Clérigo","Druida","Bárbaro", "Bardo", "Bruxo", "Feiticeiro", "Monge", "Paladino", "Patrulheiro"]
atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]


def escolher_raca():
    print("Escolha a raça do personagem:")
    for numero_raca, raca in enumerate(racas, start=1):
        print(f"{numero_raca}. {raca}")
    escolha = int(input("Digite o número da sua raça: ")) - 1
    return racas[escolha]


def escolher_classe():
    print("\nEscolha qual classe você quer:")
    for numero_classes, classe in enumerate(classes, start=1):
        print(f"{numero_classes}. {classe}")
    escolha = int(input("Digite o número da sua classe: ")) - 1
    return classes[escolha]


def distribuir_atributos():
    pontos = 27  
    valores_atributos = {atributo: 8 for atributo in atributos}  
    print("\nDistribua seus pontos entre os atributos. Você tem 27 pontos para a distribuição.")
    
    while pontos > 0:
        print(f"Pontos restantes: {pontos}")
        for numero_atributos, atributo in enumerate(atributos, start=1):
            print(f"{numero_atributos}. {atributo}: {valores_atributos[atributo]}")
        escolha = int(input("Escolha o número do atributo para aumentar em +1 (ou 0 para finalizar): "))
        
        if escolha == 0:
            break
        atributo_escolhido = atributos[escolha - 1]
        if valores_atributos[atributo_escolhido] < 15:  
            valores_atributos[atributo_escolhido] += 1
            pontos -= 1
        else:
            print(f"{atributo_escolhido} já está no máximo (15).")
    return valores_atributos


def calcular_modificador(valor):
    return (valor - 10) // 2


def criar_personagem():
    print("Bem-vindo ao mini criador de personagem do Teog ^-^")
    nome = input("Escreva o nome do seu personagem: ")
    raca = escolher_raca()
    classe = escolher_classe()
    atributos = distribuir_atributos()
    
    
    modificadores = {atributo: calcular_modificador(valor) for atributo, valor in atributos.items()}
    
    
    print("\n╔════════ Resumo do Personagem ════════╗")
    print(f"           Nome: {nome}               ")
    print(f"           Raça: {raca}               ")
    print(f"           Classe: {classe}           ")
    print("╚════════════════════════════════════╝")
    print("\n         Atributos:   ")
    for atributo, valor in atributos.items():
        print(f"{atributo}: {valor} (Modificador: {modificadores[atributo]})")
        
        
if __name__ == "__main__":
    criar_personagem()


