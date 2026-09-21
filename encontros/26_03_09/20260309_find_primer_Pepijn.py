# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    RevComPattern = Reverse(Pattern) # reverse all letters in a string
    RevComPattern = Complement(RevComPattern) # complement each letter in a string
    return RevComPattern

# Copy your Reverse() function here.
def Reverse(Pattern):
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev

# Copy your Complement() function here.
def Complement(Pattern):
    compl = ""
    bp_lib = {"A":"T", "T":"A", "C":"G", "G":"C"}
    for char in Pattern:
        compl += bp_lib.get(char)
    return compl

# Copy your PatternCount function from the previous step below this line
def PatternCount(Genome, Pattern):
    count = 0
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

sequencia = 'ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTATGCGTACGTTAGCTAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGAT'
Genome = sequencia

primer = "ATGCGTACGTTAGCTA"
Pattern = primer

print("Primer =", Pattern)
print("Primer Count =",PatternCount(Genome, Pattern))
print("Primer Matching Positions =",PatternMatching(Pattern, Genome))
print("Reverse Complement =",ReverseComplement(Pattern))
print("Reverse Complement Primer Count =",PatternCount(Genome, ReverseComplement(Pattern)))
print("Reverse Complement Primer Positions =",PatternMatching(ReverseComplement(Pattern), Genome))