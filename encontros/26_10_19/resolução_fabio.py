import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as ani

#Importação dos dados
deslocamentos = pd.read_csv("Dados_deslocamento.csv")

#Conta o número de observações
print("O número de observações foi", len(deslocamentos))

#Quantas e quais são as formigas
id_unicos = list(set(deslocamentos["id"]))
quantidade_formigas = len(id_unicos)
print(f"O deslocamento de {quantidade_formigas} formigas foi observado! \nAs formigas observadas são: {id_unicos}")

#Seleciona uma formiga para criar os gráficos
Formiga1 = deslocamentos[deslocamentos["id"] == id_unicos[0]]

#Animação
X = list(Formiga1["pos_x"])
Y = list(Formiga1["pos_y"])

fig, ax = plt.subplots()
ax.set_ylim(min(Y), max(Y))
ax.set_xlim(min(X), max(X))

def animation(posicao):
    ax.scatter(X[posicao], Y[posicao], s=0.5, edgecolors="blue")

ani_desloc = ani.FuncAnimation(fig, animation, frames = len(X), interval=20)

plt.show()

