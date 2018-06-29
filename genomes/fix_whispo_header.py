import sys
from dateutil.parser import parse
fasta_fl = open('/home/leo/PycharmProjects/whispovirus/genomes/whispo.fasta')
gb_fl = open('/home/leo/PycharmProjects/whispovirus/genomes/genome_fl_list.txt')
output = open('whispo_edited.fasta', 'w')
gb_dict = {'date':{}, 'country':{}, 'host':{}}
for fl in gb_fl:
    fl_name = fl.strip('\n')
    open_fl = open(fl_name)
    for line in open_fl:
        line = line.strip()
        if line.startswith('/collection_date'):
            date = parse(line.lstrip('/collection_date=').strip('"')).strftime('%Y-%m-%d')
            gb_dict['date'][fl_name.rstrip('.gb')]=date
        if line.startswith('/country='):
            country = line.lstrip('/country=').strip('"').strip(' ').strip('\n').lower()
            gb_dict['country'][fl_name.rstrip('.gb')] = country
        if line.startswith('/host='):
            host = line.lstrip('/host=').strip('"').strip('\n').lower()
            gb_dict['host'][fl_name.rstrip('.gb')] = host
        if gb_dict['date'].has_key(fl_name.rstrip('.gb')) == 0:
            gb_dict['date'][fl_name.rstrip('.gb')]=('0-0-0')
        if gb_dict['country'].has_key(fl_name.rstrip('.gb')) == 0:
            gb_dict['country'][fl_name.rstrip('.gb')]=('No_country')
        if gb_dict['host'].has_key(fl_name.rstrip('.gb')) == 0:
            gb_dict['host'][fl_name.rstrip('.gb')]=('No_host')
print(gb_dict)
for line in fasta_fl:
    line = line.strip()
    if line.startswith('>'):
        items = line.split(' ')
        accession = items[0].lstrip('>')
        output.write('>'+accession+'|whispo|'+accession+'|'+gb_dict['date'][accession]+'|'+gb_dict['country'][accession]+'| | | |'+gb_dict['host'][accession]+'\n')
    else:
        output.write(line+'\n')