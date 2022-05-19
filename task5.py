with open(input('Введите название файла в формате fasta: ')) as seq_file:
    name_sequence = []
    sequence = []
    for l in seq_file:
        if '>' in l:
            name_sequence.append(l.strip())
        else:
            sequence.append(l.strip())
def ORFfind(sequence):
    lst=[]
    for i in sequence:
        if 'ATG' in i:
            start=i[i.find('ATG'):]
            if 'TAA' in start:
                ind=start.index('TAA')
                lst.append(start[:(ind+3)])
            elif 'TGA' in start:
                ind = start.index('TGA')
                lst.append(start[:(ind+3)])
            elif 'TAG'in start:
                ind = start.index('TAG')
                lst.append(start[:(ind+3)])
    orf=[]
    for i in lst:
        if len(i)%3==0:
            orf.append(i)
    return orf
orf=ORFfind(sequence)
def ORF100(orf):
    orf100=[]
    for i in orf:
        if len(i)>100:
            orf100.append(i)
    return orf100
orf100=ORF100(orf)
for i in orf100:
    print(f'ORF:{i} Length:{len(i)}')

