import os,sys
from Bio import SeqIO

gene_files = [x for x in os.listdir('.') if x.endswith("fasta")]

seqs_to_write = []

for gene in gene_files:
    gene_name = gene.split("_")[0]
    for seq in SeqIO.parse(gene,'fasta'):
        seq.id = seq.id + "-{}".format(gene_name)
        seq.description=""
        seq.seq = seq.seq.ungap('-')
        seqs_to_write.append(seq)
        
SeqIO.write(seqs_to_write,sys.stdout,"fasta")