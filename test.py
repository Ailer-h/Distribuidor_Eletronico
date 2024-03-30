orb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
elementos = [None, 'Hidrogênio', 'Hélio', 'Lítio', 'Berílio', 'Boro', 'Carbono', 'Nitrogênio', 'Oxigênio', 'Flúor', 'Neônio', 'Sódio','Magnésio','Alumínio','Silício','Fósforo','Enxofre','Cloro','Argônio','Potássio','Calcio','Escândio','Titânio','Vanádio','Cromo','Maganês','Ferro','Cobalto','Níquel','Cobre','Zinco','Gálio','Germânio','Arsênio','Selênio','Bromo','Criptônio','Rubídio','Estrôncio','Ítrio','Zircônio','Nióbio','Molibdénio','Tecnécio','Rutênio','Ródio','Paládio','Prata','Cádmio','Índio','Estanho','Antimônio','Telúrio','Iodo','Xenônio','Césio','Bário','Lantânio','Cério','Praseodímio','Neodímio','Promécio','Samário','Európio','Gadolínio','Térbio','Disprósio','Hólmio','Érbio','Túlio','Itérbio','Lutécio','Háfnio','Tântalo','Tungstênio','Rênio','Ósmio','Irídio','Platina','Ouro','Mercúrio','Tálio','Chumbo','Bismuto','Polônio','Ástato','Rádon','Frâncio','Rádio','Actínio','Tório','Protactínio','Urânio','netúnio','Plutônio','Amerício','Cúrio','Berquélio','Califórnio','Einsténio','Férmio','Mendelévio','Nobélio','Laurêncio','Rutherfórdio','Dúbnio','Seabórgio','Bóhrio','Hássio','Meitnério','Darmstácio','Roentgénio','Copernício','Nipônio','Fleróvio','Moscóvio','Livermório','Tenesso','Oganésson']

elecOrder = [0,1,2,3,4,6,5,7,10,8,11,14,9,12,15,17,13,16,18]
letras = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
finalDist = ""
electronList = []

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

# distribute(10)
# operateCation(3)
# print(orb)

for i in elecOrder:
  print("Normal - ", i, end=";")

print("\n")

for i in elecOrder[::-1]:
  print("Inv - ", i, end=";")