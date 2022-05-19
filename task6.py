import os.path
def read_file(seq_file):
    if not seq_file:
        raise TypeError("Не указано имя файла")
    elif not os.path.exists(seq_file):
        raise FileNotFoundError(f'Файл {seq_file} не найден ')
    elif '.fa' not in seq_file:
        raise TypeError('Файл должен быть в формате *.fasta')
    else:
        try:
            with open(seq_file) as seq:
                name_sequence = []
                sequence = []
                for l in seq:
                    if '>' in l:
                        name_sequence.append(l.strip())
                    else:
                        sequence.append(l.strip())
        except:
            print('Ошибка ввода данных')
    return sequence
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
def ORF100(orf):
    orf100=[]
    for i in orf:
        if len(i)>10:
            orf100.append(i)
    return orf100
seq_file=input('Введите название файла в формате fasta: ')
sequence=read_file(seq_file)
if sequence==[]:
    print('В файле нет последовательности.')
else:
    orf=ORFfind(sequence)
    orf100=ORF100(orf)
    for i in orf100:
        print(f'ORF:{i} Length:{len(i)}')