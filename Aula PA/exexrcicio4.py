# Escrever um programa que solicite um valor de saque de dinheiro para o usuario e informe quais notas e quantidades serão utilizadas.

valor = int (input("digite um valor:"))

qtd100 = 0
while valor >= 100:
    valor -= 100
    qtd100 +=1

qtd50 = 0
while valor >= 50:
    valor -= 50
    qtd50 +=1

qtd10 = 0
while valor >= 10:
    valor -= 10
    qtd10 +=1

qtd2 = 0
while valor >= 2:
    valor -= 2
    qtd2 +=1

qtd5 = 0
while valor >= 5:
    valor -= 5
    qtd5 +=1

print(f"notas de 100: {qtd100}")
print(f"notas de 50: {qtd50}")
print(f"notas de 10: {qtd10}")
print(f"notas de 2: {qtd2}")
print(f"notas de 5:{qtd5}")