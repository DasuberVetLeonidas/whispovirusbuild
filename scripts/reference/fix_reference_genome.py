output = open('whispo_reference_fixed.gb', 'w')
gene_list_fl = open('/home/leo/PycharmProjects/whispovirus/scripts/genomes/gene_list.txt')
gene_names = []
# Extract gene name to the gene_names array
for line in gene_list_fl:
    line = line.strip().lstrip('     gene            ')
    gene_names.append(line)


genebank_fl = open('/home/leo/PycharmProjects/whispovirus/reference/whispovirus_reference.gb')
i = 0
j = 0
for line in genebank_fl:
    if line.startswith('     gene'):
        line = line+'                     '+'/gene='+'"'+gene_names[i]+'"'
        i += 1
        output.write(line+'\n')
    elif line.startswith('     CDS             '):
        line=line.strip('\n')
        line = line+'\n'+'                     '+'/gene='+'"'+gene_names[j]+'"'
        j += 1
        output.write(line+'\n')
    else:
        output.write(line)

