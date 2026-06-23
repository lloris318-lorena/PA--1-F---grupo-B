# ---------------------------------------------------------
# QUESTÃO 03 – Tabuada (2 pontos)
# ---------------------------------------------------------

# Solicite ao usuário um número inteiro e exiba sua tabuada
# de 1 até 10.

# Exemplo:

# Digite um número: 7

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 10 = 70

numero = int (input("digite um número interiro: "))

for i in range (1, 11):
    print (f"{numero} x {i} = {numero * i}")