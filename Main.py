# Precisamos imprimir um número para cada andar de um hotel de 20 andares.
# Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.
# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#Resolução 1

# for i in range(20,0,-1):
#     if(i == 13):
#         continue
#     print("Andar Nº:",i)

#Resolução 2

# andares = 20

# while(andares != 0):
#     if(andares != 13):
#         print("Andar Nº:",andares)
#     andares = andares-1