# Desafio: Transcrição de DNA para RNA
# **Responsável:** Lara Cavalari Santello

#Uma sequência de RNA é formada pelo alfabeto contendo os caracteres 'A', 'C', 'G' e 'U'.

#Dada uma sequência de DNA 'input_data', correspondente a uma fita codificadora, sua sequência de RNA transcrita 'output_data' é formada substituindo todas as ocorrências de 'T' em "input_data" por 'U' em 'output_data'.

## Entrada
#Uma sequência de DNA 'input_data' com comprimento máximo de 1000 nucleotídeos (nt).

## Saída
#A sequência de RNA transcrita de 'input_data', chamada agora de 'output_data'.

# Exemplo

## Entrada 
#input_data = "ACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"

DNA = "ACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"
DNA2= "AGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTTTTTTTT"

def DNA_transcription(DNA):
    RNA = DNA.replace("T", "U")
    return RNA

print(DNA_transcription(DNA))
print(DNA_transcription(DNA2))