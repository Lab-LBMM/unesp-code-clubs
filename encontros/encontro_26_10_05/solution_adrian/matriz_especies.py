#!/usr/bin/env python3

import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

parser = argparse.ArgumentParser()

parser.add_argument(
	"-e", "--especies",
	type=str,
	required=False,
	help="Path to the input file",
)
parser.add_argument(
	"-x", "--cordenadax",
	type=int,
	required=False,
)
parser.add_argument(
	"-y", "--cordenaday",
	type=int,
	required=False,
)
parser.add_argument(
	"-g", "--grafico",
	type=str,
	required=False,
)
parser.add_argument(
	"-l", "--levantamento",
	type=str,
	required=False,
)

args = parser.parse_args()

dados_csv = "dados.csv"

if args.especies and args.cordenadax and args.cordenaday:
    novos_dados = {"especie": [args.especies],
    "x": [args.cordenadax],
    "y": [args.cordenaday]}

    dataframe = pd.DataFrame(novos_dados)

    if not os.path.exists(dados_csv):
        dataframe.to_csv(dados_csv, index=False)
    else:
        dataframe.to_csv(dados_csv, mode="a", header=False, index=False)

    print("Dados salvos")
    
if args.levantamento:
    os.path.exists(dados_csv)
    dados_completos = pd.read_csv(dados_csv)
    levantamento = dados_completos["especie"].value_counts()
    print(levantamento)
    
if args.grafico:
    os.path.exists(dados_csv)
    dados_completos = pd.read_csv(dados_csv)

    sns.scatterplot(data=dados_completos, x="x", y="y", hue="especie", style="especie", s=80, alpha=0.80)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.show()
    