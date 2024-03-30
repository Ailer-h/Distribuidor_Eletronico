#Fazer a distribuíção eletronica de um atômo.

#importando bibliotecas
from time import sleep

#Declarando variáveis
orb1 = 0 #orbital 1
orb2 = {"s" : 0, "p" : 0} #orbital 2
orb3 = {"s" : 0, "p" : 0, "d" : 0} #orbital 3
orb4 = {"s" : 0, "p" : 0, "d" : 0, "f" : 0} #orbital 4
orb5 = {"s" : 0, "p" : 0, "d" : 0, "f" : 0} #orbital 5
orb6 = {"s" : 0, "p" : 0, "d" : 0} #orbital 6
orb7 = {"s" : 0, "p" : 0} #orbital 7
elecList = []
tabelaPeriodica = [None, 'Hidrogênio', 'Hélio', 'Lítio', 'Berílio', 'Boro', 'Carbono', 'Nitrogênio', 'Oxigênio', 'Flúor', 'Neônio', 'Sódio','Magnésio','Alumínio','Silício','Fósforo','Enxofre','Cloro','Argônio','Potássio','Calcio','Escândio','Titânio','Vanádio','Cromo','Maganês','Ferro','Cobalto','Níquel','Cobre','Zinco','Gálio','Germânio','Arsênio','Selênio','Bromo','Criptônio','Rubídio','Estrôncio','Ítrio','Zircônio','Nióbio','Molibdénio','Tecnécio','Rutênio','Ródio','Paládio','Prata','Cádmio','Índio','Estanho','Antimônio','Telúrio','Iodo','Xenônio','Césio','Bário','Lantânio','Cério','Praseodímio','Neodímio','Promécio','Samário','Európio','Gadolínio','Térbio','Disprósio','Hólmio','Érbio','Túlio','Itérbio','Lutécio','Háfnio','Tântalo','Tungstênio','Rênio','Ósmio','Irídio','Platina','Ouro','Mercúrio','Tálio','Chumbo','Bismuto','Polônio','Ástato','Rádon','Frâncio','Rádio','Actínio','Tório','Protactínio','Urânio','netúnio','Plutônio','Amerício','Cúrio','Berquélio','Califórnio','Einsténio','Férmio','Mendelévio','Nobélio','Laurêncio','Rutherfórdio','Dúbnio','Seabórgio','Bóhrio','Hássio','Meitnério','Darmstácio','Roentgénio','Copernício','Nipônio','Fleróvio','Moscóvio','Livermório','Tenesso','Oganésson']
letras = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
nElec = 0

#Definindo funções
def cargas(n):
    print("Seu atomo é:")
    print("1- Neutro\n2- Um cation (+)\n3- Um anion (-)")
    print()
    while True:
        ask = '0'
        ask = int(input())
        if n == 1:
            if ask == 1:
                print("Otimo, um atomo neutro!")
                print()
                return 0, None
            elif ask == 2:
                print('ERRO! Favor escolher Anion ou Neutro, o programa não reconhece o Cation de Hidrogênio ainda!')

            elif ask == 3:
                print("Otimo, um anion")
                print()
                while True:
                    atm = int(input("Quantas cargas negativas tem sua espécie?"))
                    if atm <= 0:
                        print("ENTRADA INVÁLIDA\nFavor inserir um número maior que 0")
                    else:
                        print("Otimo, seu atomo tem +{} cargas negativas!".format(atm))
                        print()
                        break
                return atm, False #False, representa um anion, ou seja, são adicionados eletrons do atomo
            else:
                print("ENTRADA INVÁLIDA\nFavor inserir um número entre 1 e 3")
        elif n == 118:
            if ask == 1:
                print("Otimo, um atomo neutro!")
                print()
                return 0, None
            elif ask == 2:
                print("Otimo, um cation")
                print()
                while True:
                    atm = int(input("Quantas cargas positivas tem sua espécie?"))
                    if atm <= 0:
                        print("ENTRADA INVÁLIDA\nFavor inserir um número maior que 0")
                    else:
                        print("Otimo, seu atomo tem +{} cargas positivas!".format(atm))
                        print()
                        break
                return atm, True #True, representa um cation, ou seja, são removidos eletrons do atomo

            elif ask == 3:
                print("ERRO! Favor escolher Cation ou Neutro, o programa não reconhece o Anion de Oganessonio ainda!")
            else:
                print("ENTRADA INVÁLIDA\nFavor inserir um número entre 1 e 3")
        else:
            if ask == 1:
                print("Otimo, um atomo neutro!")
                print()
                return 0, None
            elif ask == 2:
                print("Otimo, um cation")
                print()
                while True:
                    atm = int(input("Quantas cargas positivas tem sua espécie?"))
                    if atm <= 0:
                        print("ENTRADA INVÁLIDA\nFavor inserir um número maior que 0")
                    else:
                        print("Otimo, seu atomo tem +{} cargas positivas!".format(atm))
                        print()
                        break
                return atm, True #True, representa um cation, ou seja, são removidos eletrons do atomo

            elif ask == 3:
                print("Otimo, um anion")
                print()
                while True:
                    atm = int(input("Quantas cargas negativas tem sua espécie?"))
                    if atm <= 0:
                        print("ENTRADA INVÁLIDA\nFavor inserir um número maior que 0")
                    else:
                        print("Otimo, seu atomo tem +{} cargas negativas!".format(atm))
                        print()
                        break
                return atm, False #False, representa um anion, ou seja, são adicionados eletrons do atomo
            else:
                print("ENTRADA INVÁLIDA\nFavor inserir um número entre 1 e 3")

def electronAsk():
    while True:
        electrons = int(input("Qual o Número atômico do seu elemento?"))
        if 0 < electrons <= 118:
            print("Certo, estamos fazendo a distribuíção eletrônica do {}, de número atômico {}!".format(tabelaPeriodica[electrons],electrons))
            print()
            return electrons
        else:
            print("ENTRADA INVÁLIDA\nFavor inserir um número maior que 0")

def distribute():

    global nElec, orb1
    
    while nElec != 0:
        if orb1 < 2:
            orb1 += 1
            nElec -= 1
        elif orb2['s'] != 2:
            add = orb2['s'] + 1
            orb2.update({'s': add})
            nElec -= 1
        elif orb2['p'] != 6:
            add = orb2['p'] + 1
            orb2.update({'p': add})
            nElec -= 1
        elif orb3['s'] != 2:
            add = orb3['s'] + 1
            orb3.update({'s': add})
            nElec -= 1
        elif orb3['p'] != 6:
            add = orb3['p'] + 1
            orb3.update({'p': add})
            nElec -= 1
        elif orb4['s'] != 2:
            add = orb4['s'] + 1
            orb4.update({'s': add})
            nElec -= 1
        elif orb3['d'] != 10:
            add = orb3['d'] + 1
            orb3.update({'d': add})
            nElec -= 1
        elif orb4['p'] != 6:
            add = orb4['p'] + 1
            orb4.update({'p': add})
            nElec -= 1
        elif orb5['s'] != 2:
            add = orb5['s'] + 1
            orb5.update({'s': add})
            nElec -= 1
        elif orb4['d'] != 10:
            add = orb4['d'] + 1
            orb4.update({'d': add})
            nElec -= 1
        elif orb5['p'] != 6:
            add = orb5['p'] + 1
            orb5.update({'p': add})
            nElec -= 1
        elif orb6['s'] != 2:
            add = orb6['s'] + 1
            orb6.update({'s': add})
            nElec -= 1
        elif orb4['f'] != 14:
            add = orb4['f'] + 1
            orb4.update({'f': add})
            nElec -= 1
        elif orb5['d'] != 10:
            add = orb5['d'] + 1
            orb5.update({'d': add})
            nElec -= 1
        elif orb6['p'] != 6:
            add = orb6['p'] + 1
            orb6.update({'p': add})
            nElec -= 1
        elif orb7['s'] != 2:
            add = orb7['s'] + 1
            orb7.update({'s': add})
            nElec -= 1
        elif orb5['f'] != 14:
            add = orb5['f'] + 1
            orb5.update({'f': add})
            nElec -= 1
        elif orb6['d'] != 10:
            add = orb6['d'] + 1
            orb6.update({'d': add})
            nElec -= 1
        elif orb7['p'] != 6:
            add = orb7['p'] + 1
            orb7.update({'p': add})
            nElec -= 1

def rCargas(cargas, ion):

    global orb1, orb2, orb3, orb4, orb5, orb6, orb7

    if ion == None:
        pass

    elif ion == True:
        while cargas != 0:
            if orb7['p'] > 0:
                add = orb7['p'] - 1
                orb7.update({'p': add})
                cargas -= 1
            elif orb7['s'] > 0:
                add = orb7['s'] - 1
                orb7.update({'s': add})
                cargas -= 1
            elif orb6['d'] > 0:
                add = orb6['d'] - 1
                orb6.update({'d': add})
                cargas -= 1
            elif orb6['p'] > 0:
                add = orb6['p'] - 1
                orb6.update({'p': add})
                cargas -= 1
            elif orb6['s'] > 0:
                add = orb6['s'] - 1
                orb6.update({'s': add})
                cargas -= 1
            elif orb5['f'] > 0:
                add = orb5['f'] - 1
                orb5.update({'f': add})
                cargas -= 1
            elif orb5['d'] > 0:
                add = orb5['d'] - 1
                orb5.update({'d': add})
                cargas -= 1
            elif orb5['p'] > 0:
                add = orb5['p'] - 1
                orb5.update({'p': add})
                cargas -= 1
            elif orb5['s'] > 0:
                add = orb5['s'] - 1
                orb5.update({'s': add})
                cargas -= 1
            elif orb4['f'] > 0:
                add = orb4['f'] - 1
                orb4.update({'f': add})
                cargas -= 1
            elif orb4['d'] > 0:
                add = orb4['d'] - 1
                orb4.update({'d': add})
                cargas -= 1
            elif orb4['p'] > 0:
                add = orb4['p'] - 1
                orb4.update({'p': add})
                cargas -= 1
            elif orb4['s'] > 0:
                add = orb4['s'] - 1
                orb4.update({'s': add})
                cargas -= 1
            elif orb3['d'] > 0:
                add = orb3['d'] - 1
                orb3.update({'d': add})
                cargas -= 1
            elif orb3['s'] > 0:
                add = orb3['s'] - 1
                orb3.update({'s': add})
                cargas -= 1
            elif orb2['p'] > 0:
                add = orb2['p'] - 1
                orb2.update({'p': add})
                cargas -= 1
            elif orb2['s'] > 0:
                add = orb2['s'] - 1
                orb2.update({'s': add})
                cargas -= 1
            elif orb1 > 0:
                orb1 -= 1
                cargas -= 1
            else:
                print("ERRO!") #Para debuging

    elif ion == False:
        while cargas != 0:
            if orb2['s'] == 0:
                if orb1 < 2:
                    orb1 += 1
                    cargas -= 1
                else:
                    pass
            elif orb3['s'] == 0:
                if orb2['s'] < 2:
                    add = orb2['s'] + 1
                    orb2.update({'s': add})
                    cargas -= 1
                elif orb2['p'] < 6:
                    add == orb2['p'] + 1
                    orb2.update({'p': add})
                    cargas -= 1
                else:
                    pass
            elif orb4['s'] == 0:
                if orb3['s'] < 2:
                    add = orb3['s'] + 1
                    orb3.update({'s': add})
                    cargas -= 1
                elif orb3['p'] < 6:
                    add = orb3['p'] + 1
                    orb3.update({'p': add})
                    cargas -= 1
                elif orb3['d'] < 10:
                    add = orb3['d'] + 1
                    orb3.update({'d': add})
                    cargas -= 1
                else:
                    pass
            elif orb5['s'] == 0:
                if orb4['s'] < 2:
                    add = orb4['s'] + 1
                    orb4.update({'s': add})
                    cargas -= 1
                elif orb4['p'] < 6:
                    add = orb4['p'] + 1
                    orb4.update({'p': add})
                    cargas -= 1
                elif orb4['d'] < 10:
                    add = orb4['d'] + 1
                    orb4.update({'d': add})
                    cargas -= 1
                elif orb4['f'] < 14:
                    add = orb4['f'] + 1
                    orb4.update({'f': add})
                    cargas -= 1
                else:
                    pass
            elif orb6['s'] == 0:
                if orb5['s'] < 2:
                    add = orb5['s'] + 1
                    orb5.update({'s': add})
                    cargas -= 1
                elif orb5['p'] < 6:
                    add = orb5['p'] + 1
                    orb5.update({'p': add})
                    cargas -= 1
                elif orb5['d'] < 10:
                    add = orb5['d'] + 1
                    orb5.update({'d': add})
                    cargas -= 1
                elif orb5['f'] < 14:
                    add = orb5['f'] + 1
                    orb5.update({'f': add})
                    cargas -= 1
                else:
                    pass
            elif orb7['s'] == 0:
                if orb6['s'] < 2:
                    add = orb6['s'] + 1
                    orb6.update({'s': add})
                    cargas -= 1
                elif orb6['p'] < 6:
                    add = orb6['p'] + 1
                    orb6.update({'p': add})
                    cargas -= 1
                elif orb6['d'] < 10:
                    add = orb6['d'] + 1
                    orb6.update({'d': add})
                    cargas -= 1
                else:
                    pass
            else:
                if orb7['s'] < 2:
                    add = orb7['s'] + 1
                    orb7.update({'s': add})
                    cargas -= 1
                elif orb7['p'] < 6:
                    add = orb7['p'] + 1
                    orb7.update({'p': add})
                    cargas -= 1
                else:
                    pass

def show():

    elecList.append(orb1)
    elecList.append(orb2['s'])
    elecList.append(orb2['p'])
    elecList.append(orb3['s'])
    elecList.append(orb3['p'])
    elecList.append(orb4['s'])
    elecList.append(orb3['d'])
    elecList.append(orb4['p'])
    elecList.append(orb5['s'])
    elecList.append(orb4['d'])
    elecList.append(orb5['p'])
    elecList.append(orb6['s'])
    elecList.append(orb4['f'])
    elecList.append(orb5['d'])
    elecList.append(orb6['p'])
    elecList.append(orb7['s'])
    elecList.append(orb5['f'])
    elecList.append(orb6['d'])
    elecList.append(orb7['p'])
    
    for i,j in zip(elecList,letras):
        if i == 0:
            pass
        else:
            print(j + ':' + str(i), end = ' ')



#Interface do usuario
print("Olá e bem vindo ao Distribuídor eletronico!")
print("O programa funciona da seguinte maneira:\nVocê indica o numero atômico do atomo desejado, e nós faremos a distribuíção de seus eletrons para você!")
print("Nada mais!")
print()
sleep(3)

while True:
    ask = 'n'
    ask = input("Vamos começar?")
    ask = ask.lower()
    if ask == 's' or ask == '1':
        print("Ok, iniciando programa!")
        print()
        break
    else:
        print("Ok, aguardando!")
        sleep(1)

#Distribuíção dos Eletrons
nElec = electronAsk()
nAtm = nElec
carg, ion = cargas(nElec)
cargElec = carg
print("Iniciando a distribuição eletronica...")
distribute()
rCargas(carg, ion)
sleep(0.5)
print("...")
sleep(0.5)
print("...")
sleep(0.5)
print("...")
sleep(0.5)
print("Distribuíção pronta!")
if ion == None:
    print('A distribuíção eletronica do {} é:'.format(tabelaPeriodica[nAtm]), end = ' ')
elif ion == False:
    print('A distribuíção eletronica do {}{}- é:'.format(tabelaPeriodica[nAtm],cargElec), end = ' ')
elif ion == True:
    print('A distribuíção eletronica do {}{}+ é:'.format(tabelaPeriodica[nAtm],cargElec), end = ' ')
show()#Fazer a distribuíção eletronica de um atômo.