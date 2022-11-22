import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando o csv
data = pd.read_csv("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# Exércicio 1
print('\033[1m' + 'Exercício 1' + '\033[0m')

euaCompany = data['Company Name'].where(
    data['Location'].str.contains('USA')).unique()
chinaCompany = data['Company Name'].where(
    data['Location'].str.contains('China')).unique()
num_euaCompany = euaCompany.size
num_chinaCompany = chinaCompany.size

plt.title('Empresas Espaciais')
plt.bar('EUA', num_euaCompany, color='blue')
plt.bar('China', num_chinaCompany, color='red')
plt.show()

print(num_euaCompany)
print(num_chinaCompany)

print(f"Número de Empresas espaciais dos EUA é {num_euaCompany}.")
print(f"Número de Empresas espaciais da China é {num_chinaCompany}.")


# Exércicio 2
print('\033[1m' + 'Exercício 2' + '\033[0m')

paises = pd.read_csv("paises.csv", delimiter=";", dtype=str, encoding="utf-8")

north = paises[paises['Region'].str.contains('NORTHERN AMERICA')]

country = north['Country']
deathrate = north['Deathrate']
birthrate = north['Birthrate']


plt.xlabel('Países')
plt.ylabel('Taxa de Natalidade e Mortalidade')
plt.plot(country, birthrate, 'x--k', country, deathrate, 'x--b')
plt.show()
