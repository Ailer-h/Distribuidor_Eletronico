#Distribuição Eletronica V3 - WIP

from time import sleep

orb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
elecOrder = [0,1,2,3,4,6,5,7,10,8,11,14,9,12,15,17,13,16,18]
camadas = [1,3,6,10,14,17]

#Numero maximo de eletrons seguindo a ordem de cima;
maxElec = [2,2,6,2,6,2,10,6,2,10,6,2,14,10,6,2,14,10,6]

elementos = [None, 'Hidrogênio', 'Hélio', 'Lítio', 'Berílio', 'Boro', 'Carbono', 'Nitrogênio', 'Oxigênio', 'Flúor', 'Neônio', 'Sódio','Magnésio','Alumínio','Silício','Fósforo','Enxofre','Cloro','Argônio','Potássio','Calcio','Escândio','Titânio','Vanádio','Cromo','Maganês','Ferro','Cobalto','Níquel','Cobre','Zinco','Gálio','Germânio','Arsênio','Selênio','Bromo','Criptônio','Rubídio','Estrôncio','Ítrio','Zircônio','Nióbio','Molibdénio','Tecnécio','Rutênio','Ródio','Paládio','Prata','Cádmio','Índio','Estanho','Antimônio','Telúrio','Iodo','Xenônio','Césio','Bário','Lantânio','Cério','Praseodímio','Neodímio','Promécio','Samário','Európio','Gadolínio','Térbio','Disprósio','Hólmio','Érbio','Túlio','Itérbio','Lutécio','Háfnio','Tântalo','Tungstênio','Rênio','Ósmio','Irídio','Platina','Ouro','Mercúrio','Tálio','Chumbo','Bismuto','Polônio','Ástato','Rádon','Frâncio','Rádio','Actínio','Tório','Protactínio','Urânio','netúnio','Plutônio','Amerício','Cúrio','Berquélio','Califórnio','Einsténio','Férmio','Mendelévio','Nobélio','Laurêncio','Rutherfórdio','Dúbnio','Seabórgio','Bóhrio','Hássio','Meitnério','Darmstácio','Roentgénio','Copernício','Nipônio','Fleróvio','Moscóvio','Livermório','Tenesso','Oganésson']

letras = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
finalDist = ""
electronList = []

def getChoice() -> int | None:
    while True:
        ask = '0'

        try:
            ask = int(input("> "))
            return ask

        except ValueError:
            print("ENTRADA INVALIDA! Por favor, insira um número")
        
def getCargas(signal: str) -> int | None:
    while True:
        try:
            atm = int(input(f"Quantas cargas ({signal}) tem sua espécie?"))

            if atm > 0:
                print(f"Otimo, seu atomo tem {signal}{atm} cargas!")
                return atm
            
            return None

        except ValueError:
            print("ENTRADA INVALIDA! Por favor, insira um número")


def getElementType(n: int) -> int | bool:
    print("Seu atomo é:")
    print("1- Neutro\n2- Um cation (+)\n3- Um anion (-)", end="\n\n")

    while True:
        choice = getChoice()

        if choice == 1:
            print("Otimo, um atomo neutro!\n")
            return 0, None
        
        if choice == 2: 
            if n != 1:
                print("Otimo, um cation\n")
                cargas = getCargas("+")

                if cargas != None:
                    return cargas, False #False representa um cation, ou seja, são removidos eletrons
            
            print("Favor escolher Anion ou Neutro! O programa não suporta o cation de Hidrogênio")

        if choice == 3: 
            if n != 118:
                print("Otimo, um anion\n")
                cargas = getCargas("-")

                if cargas != None:
                    return cargas, True #True representa un anion, ou seja, são adicionados eletrons
            print("Favor escolher Cation ou Neutro! O programa não suporta o anion de Oganessônio")


def getAtmNumber():
  while True:
    electrons = int(input("Qual o numero atômico do seu elemento?"))

    if 0 < electrons <= 118:
      print("Certo, estamos fazendo a distribuição eletronica do {}, de numero atomico {}!\n".format(elementos[electrons],electrons))
      return electrons
    
    print("ENTRADA INVALIDA!\n Favor inserir um numero maior que zero e menor que 119!")


def distribute(nElec: int):
    global orb

    while nElec > 0:
        for i in elecOrder:
            if orb[i] < maxElec[i]:
                electrons = maxElec[i] - orb[i]
                orb[i] += electrons
                nElec -= electrons
                break


def operateCation(nIon: int): #Remove eletrons das camadas
    global orb

    while nIon > 0:
        for i in elecOrder[::-1]:
            if orb[i] > 0:
                remove = abs(orb[i] - nIon)
                nIon -= remove
                orb[i] -= remove
                break
    
def operateAnion(nIon: int): #Adiciona eletrons nas camadas
    while nIon > 0:
        for i in camadas:
            if orb[i] == 0:
                pass
                

# Slices work like that [start:end:jump]
# Where the start is inclusive and the end is exclusive

distribute(10)
operateCation(3)
print(orb)