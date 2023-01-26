import numpy as np;

km = np.loadtxt(r"C:\Users\Gustavo Rodrigues\Desktop\Python_Data_Science\Numpy\data\carros-km.txt")
anos = np.loadtxt(r"C:\Users\Gustavo Rodrigues\Desktop\Python_Data_Science\Numpy\data\carros-anos.txt")
media = km/(2023 - anos);

#print(media)
ano_atual, ano_fabricacao , km_total = 2023, 2019, 0 ;

#print(f'O ano atual é {ano_atual}, o ano de fabricacao e {ano_fabricacao} e o km total do seu carro é {km_total}');

#Criando listas
Acessorios = ['Rodas de liga', 'Travas eletricas', 'Piloto automatico', 'Bancos de Couro', 'Ar condicionado']
#print(type(Acessorios))
carro_1 = ['Jetta', 'Motor 4.0 turbo', 2003, 44410.0, False,Acessorios,88078.64]
carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False,['Central Multimídia','Teto panorâmico','Freios ABS'],106161.94]

#Trabalhando com listas
#print(str(carro_1) + '\n' + str(carro_2))
carros = [carro_1,carro_2]
items = []
for i in range(len(carro_2)):
  if(carro_1[i] == 'Jetta'):
      items.append(True)
  else:
      items.append(False)

#print('Rodas de liga' in Acessorios)#verifica se possui esse item nos Acessorios
#print('4x4' not in Acessorios)#verifica se não possui esse item nos Acessorios

carros_concat = carro_1 + carro_2
#print(carros_concat)
#print(len(carros_concat))#tamanho da lista
#print(carros)
#print(carros[1][5][-1])

#Metodos de listas
Acessorios = ['Rodas de liga', 'Travas elétricas','Piloto automático', 'Bancos de Couro', 'Ar condicionado', 'Sensor De Estacionamento',
              'Sensor crepuscular','Sensor de chuva'
              ]
Acessorios.sort() #ordena a lista
#print(Acessorios)

Acessorios.append('4 x 4');#Adiciona o valor no fim da lista
#print(Acessorios)

Acessorios.pop(0)#Se não passar nenhum argumento remove do fim da lista, caso passe remove o item do index passado
#print(Acessorios)

Acessorios_2 = Acessorios;#Dessa forma copia a referencia também, se mudar de uma lista, muda da outra também
Acessorios.append('Valores');

#print(str(Acessorios) + '\n' + str(Acessorios_2))

Acessorios_2 = Acessorios.copy()#Dessa forma realmente faz uma copia
Acessorios_2.pop();
#print(str(Acessorios) + '\n' + str(Acessorios_2))

#Estrutura de repetição
valores_ao_quadrado = [];
#for items in range(len(Acessorios)):
    #print(items)

#for items in Acessorios:
    #print(items)


for i in range(1,11):
    #print(f'{i} ^ 2 = {i**2}')
    valores_ao_quadrado.append(i**2);

#for i in valores_ao_quadrado:
    #print(i)

#Loops Aninhados
dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

Acessorios = []
#forma 1 de transformar um array com mais de uma dimensão, em uma dimensão só
Acessorios = []
for i in dados:
    for j in i:
        Acessorios.append(j)
Acessorios = []
Acessorios = [j for i in dados for j in i]
Acessorios = set(Acessorios); #remove duplicatas da lista

#Condicionais
# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
carros_usados = []
zero_km = []
#só printa os carros verdadeiros
for i in dados:
   if(i[-1] == True):
       zero_km.append(i)
   elif():
       print('diferente')
   else:
       carros_usados.append(i)

print("Carros Usados:")
for carros in carros_usados:
    print(carros)

print("\n")

print("Carros Zero KM:")
for carros in zero_km:
    print(carros)