#Distribuição Eletronica V2

from time import sleep

orb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
elementos = [None, 'Hidrogênio', 'Hélio', 'Lítio', 'Berílio', 'Boro', 'Carbono', 'Nitrogênio', 'Oxigênio', 'Flúor', 'Neônio', 'Sódio','Magnésio','Alumínio','Silício','Fósforo','Enxofre','Cloro','Argônio','Potássio','Calcio','Escândio','Titânio','Vanádio','Cromo','Maganês','Ferro','Cobalto','Níquel','Cobre','Zinco','Gálio','Germânio','Arsênio','Selênio','Bromo','Criptônio','Rubídio','Estrôncio','Ítrio','Zircônio','Nióbio','Molibdénio','Tecnécio','Rutênio','Ródio','Paládio','Prata','Cádmio','Índio','Estanho','Antimônio','Telúrio','Iodo','Xenônio','Césio','Bário','Lantânio','Cério','Praseodímio','Neodímio','Promécio','Samário','Európio','Gadolínio','Térbio','Disprósio','Hólmio','Érbio','Túlio','Itérbio','Lutécio','Háfnio','Tântalo','Tungstênio','Rênio','Ósmio','Irídio','Platina','Ouro','Mercúrio','Tálio','Chumbo','Bismuto','Polônio','Ástato','Rádon','Frâncio','Rádio','Actínio','Tório','Protactínio','Urânio','netúnio','Plutônio','Amerício','Cúrio','Berquélio','Califórnio','Einsténio','Férmio','Mendelévio','Nobélio','Laurêncio','Rutherfórdio','Dúbnio','Seabórgio','Bóhrio','Hássio','Meitnério','Darmstácio','Roentgénio','Copernício','Nipônio','Fleróvio','Moscóvio','Livermório','Tenesso','Oganésson']

elecOrder = [0,1,2,3,4,6,5,7,10,8,11,14,9,12,15,17,13,16,18]
letras = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
finalDist = ""
electronList = []


def getIon(n):
  print("Seu atomo é:")
  print("1- Neutro\n2- Um cation (+)\n3- Um anion (-)")
  print()
  while True:
    ask = '0'
    ask = int(input())

    if ask == 1:

      print("Otimo, um atomo neutro!\n")
      return 0, None

    elif ask == 2:

      if n != 1:

        print("Otimo, um cation\n")
        while True:
          atm = int(input("Quantas cargas positivas tem sua espécie?"))
          if atm <= 0:
            print("ENTRADA INVÁLIDA\nFavor inserir um número maior que 0")
          else:
            print("Otimo, seu atomo tem +{} cargas positivas!\n".format(atm))
            break
          return atm, False #False representa um cation, ou seja, são removidos eletrons

      else:
        print("Favor escolher Anion ou Neutro! O programa não suporta o cation de Hidrogênio")

    elif ask == 3:

      if n != 118:

        print("Otimo, um anion\n")
        while True:
          atm = int(input("Quantas cargas negativas tem a sua espécie?"))
          if atm <= 0:
            print("ENTRADA INVÁLIDA\nFavor inserir um número maior que 0")
          else:
            print("Otimo, seu atomo tem -{} cargas negativas!\n".format(atm))
            break
          return atm, True #True representa un anion, ou seja, são adicionados eletrons

      else:
        print("Favor escolher Cation ou Neutro! O programa não suporta o anion de Oganessônio")

    else:
      print("ENTRADA INVÁLIDA\nFavor inserir um número entre 1 e 3\n")


def getAtmNumber():
  while True:
    electrons = int(input("Qual o numero atômico do seu elemento?"))

    if 0 < electrons <= 118:
      print("Certo, estamos fazendo a distribuição eletronica do {}, de numero atomico {}!\n".format(elementos[electrons],electrons))
      return electrons

    else:
      print("ENTRADA INVALIDA!\n Favor inserir um numero maior que zero e menor que 119!")


def distribute(nElec):

  global orb

  while nElec > 0:
    index = None

    if orb[0] < 2: #1s
      index = 0

    elif orb[1] < 2: #2s
      index = 1

    elif orb[2] < 6: #2p
      index = 2

    elif orb[3] < 2: #3s
      index = 3

    elif orb[4] < 6: #3p
      index = 4

    elif orb[6] < 2: #4s
      index = 6

    elif orb[5] < 10: #3d
      index = 5

    elif orb[7] < 6: #4p
      index = 7

    elif orb[10] < 2: #5s
      index = 10

    elif orb[8] < 10: #4d
      index = 8

    elif orb[11] < 6: #5p
      index = 11

    elif orb[14] < 2: #6s
      index = 14

    elif orb[9] < 14: #4f
      index = 9

    elif orb[12] < 10: #5d
      index = 12

    elif orb[15] < 6: #6p
      index = 15

    elif orb[17] < 2: #7s
      index = 17

    elif orb[13] < 14: #5f
      index = 13

    elif orb[16] < 10: #6d
      index = 16

    elif orb[18] < 6:  #7p
      index = 18

    orb[index] += 1 #Adiciona um eletron para a camada correta
    nElec -= 1 #Remove um eletron dos eletrons faltantes


def operateCation(nIon): #Remove eletrons das camadas

  global orb

  while nIon > 0:

    index = None

    if orb[18] != 0: #7p
      index = 18

    elif orb[16] != 0: #6d
      index = 16

    elif orb[13] != 0: #5f
      index = 13

    elif orb[17] != 0: #7s
      index = 17

    elif orb[15] != 0: #6p
      index = 15

    elif orb[12] != 0: #5d
      index = 12

    elif orb[9] != 0: #4f
      index = 9

    elif orb[14] != 0: #6s
      index = 14

    elif orb[11] != 0: #5p
      index = 11

    elif orb[8] != 0: #4d
      index = 10

    elif orb[10] != 0: #5s
      index = 10

    elif orb[7] != 0: #4p
      index = 7

    elif orb[5] != 0: #3d
      index = 5

    elif orb[6] != 0: #4s
      index = 6

    elif orb[4] != 0: #3p
      index = 4

    elif orb[3] != 0: #3s
      index = 3

    elif orb[2] != 0: #2p
      index = 2

    elif orb[1] != 0: #2s
      index = 1

    elif orb[0] != 0: #1s
      index = 0

    orb[index] -= 1 #Remove um eletron da camada escolhida
    nIon -= 1 #Remove um eletron da contagem de eletrons a remover


def operateAnion(nIon): #Adiciona eletrons nas camadas

  global orb

  while nIon > 0:

    index = None

    if orb[1] == 0: #2s vazio -> C.V. = 1
      if orb[0] < 2:
        index = 0

    elif orb[3] == 0: #3s vazio -> C.V. = 2
      if orb[1] < 2:
        index = 1

      elif orb[2] < 6:
        index = 2

    elif orb[6] == 0: #4s vazio -> C.V. = 3
      if orb[3] < 2:
        index = 3

      elif orb[4] < 6:
        index = 4

      elif orb[5] < 10:
        index = 5

    elif orb[10] == 0: #5s vazio -> C.V. = 4
      if orb[6] < 2:
        index = 6

      elif orb[7] < 6:
        index = 7

      elif orb[8] < 10:
        index = 8

      elif orb[9] < 14:
        index = 9

    elif orb[14] == 0: #6s vazio -> C.V. = 5
      if orb[10] < 2:
        index = 10

      elif orb[11] < 6:
        index = 11

      elif orb[12] < 10:
        index = 12

      elif orb[13] < 14:
        index = 13

    elif orb[17] == 0: #7s vazio -> C.V. = 6
      if orb[14] < 2:
        index = 14

      elif orb[15] < 6:
        index = 15

      elif orb[16] < 10:
        index = 16

    else: #Nesse caso, C.V. só pode ser = 7
      if orb[17] < 2:
        index = 17

      elif orb[18] < 6:
        index = 18

    orb[index] += 1 #Adiciona um eletron para a camada correta
    nIon -= 1 #Remove um eletron dos eletrons faltantes


def interpretIon(nIon,ion):

  if ion == None:
    pass #não altera a distribuição

  elif ion == False: #Cation

    operateCation(nIon)

  elif ion == True: #Anion

    operateAnion(nIon)

def show():

  global finalDist

  for i in elecOrder: electronList.append(orb[i])

  for i,j in zip(electronList,letras):
    if i == 0:
      pass

    else:
      finalDist += j + ':' + str(i) + ' '


def interface():
  # nElec = getAtmNumber()
  # carga, ion = getIon(nElec)

  # nAtm = nElec
  # nCarga = carga

  nAtm = 29
  nCarga = 2

  nElec = 29
  carga = 2
  ion = True

  print("Iniciando distribuição eletrônica...")
  distribute(nElec)
  interpretIon(carga,ion)
  show()

  for i in range(3):
    print("...")
    sleep(0.5)

  print("Distribuição pronta!")

  if ion == None:
    print('A distribuíção eletronica do {} é: {}'.format(elementos[nAtm], finalDist))
  elif ion == False:
    print('A distribuíção eletronica do {}{}- é: {}'.format(elementos[nAtm],nCarga, finalDist))
  elif ion == True:
    print('A distribuíção eletronica do {}{}+ é: {}'.format(elementos[nAtm],nCarga, finalDist))

interface()