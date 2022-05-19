def statistic(seq):
    alphabet = ['A', 'C', 'G', 'T']
    stats=[]
    for i in range(0,4):
        stat = seq.count(alphabet[i])
        stats.append(str(alphabet[i])+'-'+str(stat))
    return stats
with open('seq.fasta') as seq_file:
    name_sequence = []
    sequence = []
    for l in seq_file:
        if '>' in l:
            name_sequence.append(l.strip())
        else:
            sequence.append(l.strip())
def width(name, seq):
    width1=0
    width2=0
    for i in name:
        if width1<len(i):
            width1=len(i)
    for j in seq:
        if width2<len(str(len(j))):
            width2=len(str(len(j)))
        if width2<6:
            width2=7
    return width1, width2
w1,w2=width(name_sequence,sequence)
print(w1,w2)
print(f"{'Name':{w1}} {'Length':{w2}} {'Frequency:':50}")
for i in range(len(name_sequence)):
    print(f'{name_sequence[i]:{w1}} {len(sequence[i]):{w2}} {statistic(sequence[i]):}')
