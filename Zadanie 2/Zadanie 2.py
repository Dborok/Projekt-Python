import pandas as pd
import matplotlib.pyplot as plt

Wallets = pd.read_table("../../Projekt Python/Zadanie 2/Pareto Front.txt")
Instruments = pd.read_table("../../Projekt Python/Zadanie 2/assets.txt")
plt.scatter(Wallets['Variance'], Wallets['Mean'], color='black')
plt.scatter(Instruments['Variance'], Instruments['Mean'], color='red')
plt.xlabel('Variance')
plt.ylabel('Mean')
plt.show()
