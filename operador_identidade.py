#Operadores de identidade: Utilizamos para verificar se dois objetos ocupam o mesmo lugar na memória no Python 
cidade_p1 = "São Paulo" 
cidade_p2 = "São Paulo" 
cidade_p3 = "Rio de Janeiro" 
print(id(cidade_p1)) 
print(id(cidade_p2)) 
print(id(cidade_p3)) 
print(cidade_p1 is cidade_p2)