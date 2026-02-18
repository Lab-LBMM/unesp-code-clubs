## **Desafio:** Levantamento de Abelhas sem Ferrão
**Responsável:** Thiago Dietrich

Durante um levantamento biológico, foram observados ninhos de diferentes espécies de abelhas sem ferrão.
Cada ninho foi registrado pelo nome científico da espécie.

A lista abaixo contém os ninhos observados durante o levantamento:

levantamento = [
    "Melipona scutellaris",
    "Scaptotrigona postica",
    "Tetragonisca angustula",
    "Melipona scutellaris",
    "Scaptotrigona postica",
    "Scaptotrigona depilis",
    "Melipona quadrifasciata",
    "Friesiomelita varia",
    "Scaptotrigona postica"
]

Tarefas:

1) Enumere os ninhos observados na ordem em que aparecem na lista.
2) Mostre o total de ninhos observados.
3) Calcule quantos ninhos existem de cada espécie.

Crie uma estrutura para guardar essas contagens:
contagem_especies = {}

4) Calcule quantos ninhos existem de cada gênero.

> Dica: O gênero é a primeira palavra do nome científico e você pode separar o nome usando .split().