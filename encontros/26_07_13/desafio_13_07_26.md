## **Desafio:** Tradução de DNA para Proteína
**Responsável:** Tobias

Durante a tradução, o RNA mensageiro (mRNA) é lido em trincas de nucleotídeos chamadas **códons**. Cada códon (64 no total) especifica um aminoácido ou um sinal de parada.

Existem três códigos especiais:
- **AUG**: códon de início da tradução, codifica o aminoácido **Metionina (M)**
- **UAA, UAG, UGA**: códons de parada (*stop codons*), que sinalizam o término da proteína

A tabela do código genético padrão (códon de RNA → aminoácido) é apresentada abaixo:

---

### **Tabela do Código Genético (RNA)**

| Códon | AA | Códon | AA | Códon | AA | Códon | AA |
|-------|----|-------|----|-------|----|-------|----|
| UUU | F | UCU | S | UAU | Y | UGU | C |
| UUC | F | UCC | S | UAC | Y | UGC | C |
| UUA | L | UCA | S | UAA | STOP | UGA | STOP |
| UUG | L | UCG | S | UAG | STOP | UGG | W |
| CUU | L | CCU | P | CAU | H | CGU | R |
| CUC | L | CCC | P | CAC | H | CGC | R |
| CUA | L | CCA | P | CAA | Q | CGA | R |
| CUG | L | CCG | P | CAG | Q | CGG | R |
| AUU | I | ACU | T | AAU | N | AGU | S |
| AUC | I | ACC | T | AAC | N | AGC | S |
| AUA | I | ACA | T | AAA | K | AGA | R |
| AUG | M | ACG | T | AAG | K | AGG | R |
| GUU | V | GCU | A | GAU | D | GGU | G |
| GUC | V | GCC | A | GAC | D | GGC | G |
| GUA | V | GCA | A | GAA | E | GGA | G |
| GUG | V | GCG | A | GAG | E | GGG | G |

---

## Entrada

Uma sequência de DNA com 109 nucleotídeos:

```
CAGTCCATGGCTCTACGTCCTGAATTTGGTCATATCAAACTCATGTTCCCGCAGCGTTCTACAGTTTGGTACGCTCTTAGTCCAGGACGCGAGTAAGCTGATGCCTTAG
```

---

## Objetivos

1) Dada uma entrada (DNA) retorne o RNAm do mesmo

2) Encontre todas as **ORFs** (*Open Reading Frames*) — regiões que vão de um AUG até um códon de parada — retorne todas em ordem crescente de tamanho

3) Usando a **Tabela do Código Genético (RNA)** traduza cada **ORF** para sua respectiva proteína (usando o código de uma letra) e retorne 

**Extra (Mantendo a leva de gráficos)**
Gere um gráfico discriminando os aminoácidos produzidos por essa cadeia de DNA

---

**Referência:** Adaptado de Rosalind — *Translating RNA into Protein* (http://rosalind.info/problems/prot/)
