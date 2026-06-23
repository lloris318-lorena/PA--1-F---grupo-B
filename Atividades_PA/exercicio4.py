# ---------------------------------------------------------
# QUESTÃO 04 – Fatorial (4 pontos)
# ---------------------------------------------------------

# Solicite ao usuário um número inteiro positivo e calcule
# seu fatorial utilizando um laço de repetição.

# Exemplo:

# Digite um número: 5

# Fatorial = 120

# Pois:

# 5! = 5 × 4 × 3 × 2 × 1

# Observação:
# O programa deve validar se o número informado é positivo.

numero = int(input("Digite um número inteiro : "))

while numero <= 0: 
    print("numero invalido, por favor tente um numero inteiro e positivo.")

    mult = 1

    for i in range(1, numero + 1):
        mult *= i

    print(mult)