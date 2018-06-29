from Bio import SeqIO
from Bio import Entrez
Entrez.email="shijia.zhou@student.adelaide.edu.au"
genome_list=open('/home/leo/PycharmProjects/whispovirus/genomes/all_genomes.txt')
for line in genome_list:
    record_id = line.lstrip('VERSION     ').strip('\n')
    print(record_id)
    new_handle = Entrez.efetch(db="nucleotide", id=record_id, rettype="gb", retmode="genbank")
    print(record_id+"new_handle created")
    seq_record = SeqIO.read(new_handle, "genbank")
    print(record_id+"seq_record generated")
    print(seq_record.annotations)
    SeqIO.write(seq_record, (record_id+'.gb').strip('?'), "genbank")