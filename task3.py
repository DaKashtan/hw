import re
import os.path
def pattern(fprimer, rprimer):
    if not fprimer or rprimer:
        raise TypeError("Не задана последовательность праймера!")

    fprimer, rprimer = fprimer.upper(), rprimer.upper()
    fdict = {'A': 'A', 'T': 'T', 'C': 'C', 'G': 'G', 'B': '[CGT]', 'D': '[AGT]', 'H': '[ACT]', 'K': '[GT]',
                 'M': '[AC]', 'N': '[ACGT]', 'R': '[GA]', 'S': '[GC]', 'V': '[ACG]', 'W': '[AT]', 'Y': '[CT]'}
    rdict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'B': '[GCA]', 'D': '[TCA]', 'H': '[TGA]', 'K': '[CA]',
               'M': '[TG]', 'N': '[ACGT]', 'R': '[CT]', 'S': '[CG]', 'V': '[TGC]', 'W': '[TA]', 'Y': '[GA]'}
    pattern = ''
    for i in fprimer:
        pattern += fdict[i]
    pattern += '.+'
    for j in rprimer:
        pattern += rdict[j]
    return pattern
file=input('Введите имя файла в формате fasta: ')
if not file:
    raise TypeError("Не указано имя файла")
elif not os.path.exists(file):
    raise FileNotFoundError(f'Файл {file} не найден ')
elif '.fa' not in file:
    raise TypeError('Файл должен быть в формате *.fasta')
else:
    with open(file) as seq_file:
        name_sequence = []
        sequence = []
        for l in seq_file:
            if '>' in l:
                name_sequence.append(l.strip())
            else:
                sequence.append(l.strip())
fprimer = input('Прямой праймер: ')
rprimer = input('Обратный праймер: ')
patt = pattern(fprimer, rprimer)
for i in range(len(sequence)-1):
    res_search = re.findall(patt, sequence[i])
    if res_search==[]:
        continue
    print(res_search)

