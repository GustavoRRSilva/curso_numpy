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
print(str(Acessorios) + '\n' + str(Acessorios_2))