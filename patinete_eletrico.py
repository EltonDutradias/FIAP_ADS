#Calculando a velocidade média de um patinete elétrico. 
print("Esse programa calacula a velocidade médio de um patinete") 
distancia = input("Qual foi a distância em metros percorrida pelo patinete? ") 
tempo = input("Quantos minutos o patinete demorou para percorrer essa distância? ") 
velocidade_media = float(distancia) / float(tempo) 
print("O patinete atingiu uma velocidade de {0:.2f} m/min".format(velocidade_media))