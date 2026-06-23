# ---------------------------------------------------------
# QUESTÃO 02 – Soma dos Números (2 pontos)
# ---------------------------------------------------------

# Solicite ao usuário um número inteiro positivo.

# Utilizando um laço de repetição, calcule e exiba a soma de
# todos os números de 1 até o número informado.

# Exemplo:

# Digite um número: 5

# Resultado: 15

# Pois:

# 1 + 2 + 3 + 4 + 5 = 15

numero = int(input("Digite um número inteiro : "))

soma = 0

for i in range(numero + 1):
  soma =   soma + i
print(soma)
