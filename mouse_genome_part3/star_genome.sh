#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --mem=100GB                        #optional: amount of memory, default is 4GB per cpu
#SBATCH -c 8
#SBATCH --job-name=stats                  #optional: job name

/usr/bin/time -v STAR --runThreadN 8 --runMode genomeGenerate --genomeDir /home/jujo/bgmp/bioinfo/PS/QAA/mouse_genome_part3/star_genome/ \
 --genomeFastaFiles Mus_musculus.GRCm39.dna_rm.primary_assembly.fa\
 --sjdbGTFfile Mus_musculus.GRCm39.112.gtf