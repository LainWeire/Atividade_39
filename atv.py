# Faça um programa que receba a temperatura média
# de cada mês do ano e armazene-as em uma lista
# Em seguida, calcule a média anual das temperaturas
# e mostre a média calculada juntamente com todas as
# temperaturas acima da média anual, e em que mês
# elas ocorreram (mostrar o mês por extenso: 1
# Janeiro, 2 - Fevereiro,...).
soma = 0

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


t = [float(input("Digite a temperatura média de um mês:   ")) for item in range(12)]

for temp in t:
    soma += temp

ma = soma / 12
print("Média anual: ", ma)

print("Temperaturas acima da média anual:")

for i in range(12):
    if t[i] > ma:
        print(f"{meses[i]}: {t[i]:.2f}°C")