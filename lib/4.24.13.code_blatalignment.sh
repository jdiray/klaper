#Purdue strugeon assembly and public EST ::: BLAT

/Users/charlesmurphy/bin/x86_64/blat -t=dna -q=dna -minIdentity=80 Trinity.sturgeon.purdue.fa ncbi.acipenser.fulvescens.fasta ../results/4.24.13.blat_Trinity.sturgeon.purdue.fa_ncbi.acipenser.fulvescens.fasta.80id.psi

/Users/charlesmurphy/bin/x86_64/blat -t=dna -q=dna -minIdentity=90 Trinity.sturgeon.purdue.fa ncbi.acipenser.fulvescens.fasta ../results/4.24.13.blat_Trinity.sturgeon.purdue.fa_ncbi.acipenser.fulvescens.fasta.90id.psi

/Users/charlesmurphy/bin/x86_64/blat -t=dna -q=dna -minIdentity=95 Trinity.sturgeon.purdue.fa ncbi.acipenser.fulvescens.fasta ../results/4.24.13.blat_Trinity.sturgeon.purdue.fa_ncbi.acipenser.fulvescens.fasta.95id.psi

/Users/charlesmurphy/bin/x86_64/blat -t=dna -q=dna -minIdentity=95 ncbi.acipenser.fulvescens.fasta Trinity.sturgeon.purdue.fa ../results/4.24.13.blat_Trinity.sturgeon.purdue.fa_ncbi.acipenser.fulvescens.fasta.95id2.psi

/Users/charlesmurphy/bin/x86_64/blat -t=rna -q=rna ./sturgeon/ncbi.acipenser.fulvescens.fasta ./sturgeon/Trinity.sturgeon.purdue.fa ../results/4.25.13_blat_Trinity.sturgeon.purdue.fa_ncbi.acipenser.fulvescens.fasta_default.psi

/Users/charlesmurphy/bin/x86_64/blat -t=dna -q=rna -minIdentity=80 L_oculatus_v1.assembly.fa ./sturgeon/Trinity.sturgeon.purdue.fa ../results/4.25.13.blat_Trinity.sturgeon.purdue.fa_L_oculatus_v1.assembly.fa.80id2.psi

#Purdue sturgeon assembly and public EST ::: Blastn

makeblastdb -in Trinity.sturgeon.purdue.fa -dbtype nucl -out Trinity.sturgeon.purdue.fa

makeblastdb -in ncbi.acipenser.fulvescens.fasta -dbtype nucl -out ncbi.acipenser.fulvescens.fasta

blastn -db ../data/sturgeon/ncbi.acipenser.fulvescens.fasta -query ../data/sturgeon/Trinity.sturgeon.purdue.fa -out ../results/4.25.13_blastn_QUERY.Trinity.sturgeon.purdue_DATABASE.ncbi.acipenser.fulvescens.out -num_threads 4 -outfmt "6 qseqid qlen qstart qend sseqid slen sstart send length score bitscore nident mismatch"

blastn -db ../data/sturgeon/Trinity.sturgeon.purdue.fa -query ../data/sturgeon/ncbi.acipenser.fulvescens.fasta -out ../results/4.25.13_QUERY.blastn_ncbi.acipenser.fulvescens_DATABASE.Trinity.sturgeon.purdue.out -num_threads 4 -outfmt "6 qseqid qlen qstart qend sseqid slen sstart send length score bitscore nident mismatch"

#sturgeon assembly against spotted gar

/Users/charlesmurphy/bin/x86_64/blat -t=dna -q=dna -minIdentity=95 L_oculatus_v1.assembly.fa Trinity.sturgeon.purdue.fa ../results/4.24.13.blat_Trinity.sturgeon.purdue.fa_L_oculatus_v1.assembly.fa.95id.psi

/Users/charlesmurphy/bin/x86_64/blat -t=dna -q=rna -minIdentity=80 L_oculatus_v1.assembly.fa ./sturgeon/Trinity.sturgeon.purdue.fa ../results/4.25.13.blat_Trinity.sturgeon.purdue.fa_L_oculatus_v1.assembly.fa.80id2.psi