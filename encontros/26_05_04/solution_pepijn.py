seq_1 = 'ATGCTTAGCGTACGATCGATCGATCGATCGATCGATCGATCGA-TCG'
seq_2 = 'ATGCTTAGCGTACGATCGATCGTTTCGATCGATCGATCGATCGACTC'
#seq_1 = 'ATGCTTAGCGTACGATCGATCGA-TCGATCGATCGATCGATCGA-TCG'
#seq_2 = 'ATGCTTAGCGTACGATCGATCGTTTCGATCGATCGATCGATCGACTC-'

def basepairdiff(seq_1, seq_2):
    count = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            count = count+1
    return count

print("Number of base pair differences =", basepairdiff(seq_1, seq_2))

def percentident(seq_1, seq_2):
    percent = 0
    numberdiff = basepairdiff(seq_1, seq_2)
    percent = (numberdiff/len(seq_1))*100
    return 100 - percent

print("Percent identity =", percentident(seq_1, seq_2), "%")