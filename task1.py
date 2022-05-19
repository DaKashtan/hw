#name=input('Имя файла  - ')
with open('seq.fasta') as seq_file:
    for l in seq_file:
        if '>' in l:
            print('Description:{}'.format(l.strip()))
        else:
            print('Sequence:{}'.format(l.strip()))