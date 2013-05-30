apt-get upgrade

apt-get update

apt-get -y --force-yes install libbz2-1.0 libbz2-dev libncurses5-dev openjdk-6-jre-headless zlib1g-dev

cd /mnt

curl -L 'http://downloads.sourceforge.net/project/trinityrnaseq/trinityrnaseq_r2013-02-25.tgz' > trinityrnaseq_r2013-02-25.tgz

tar xzf trinityrnaseq_r2013-02-25.tgz

cd trinityrnaseq_r2013-02-25

export FORCE_UNSAFE_CONFIGURE=1

make

./Trinity.pl --CPU 8 --output /mnt/sturgeon --seqType fq --JM 60G --left /mnt/sturgeon_data/002894_03F1L_AGTCAA_R1_filtered1.fastq /mnt/sturgeon_data/002895_09F1L_AGTTCC_R1_filtered1.fastq --right /mnt/sturgeon_data/002894_03F1L_AGTCAA_R2_filtered2.fastq /mnt/sturgeon_data/002895_09F1L_AGTTCC_R2_filtered2.fastq