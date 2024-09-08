#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --mem=100GB                        #optional: amount of memory, default is 4GB per cpu
#SBATCH -c 8
#SBATCH --job-name=34                  #optional: job name

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads --outFilterMultimapNmax 3 \
 --outSAMunmapped Within KeepPairs \
 --alignIntronMax 1000000 --alignMatesGapMax 1000000 \
 --readFilesCommand zcat \
 --readFilesIn /home/jujo/bgmp/bioinfo/PS/QAA/output_trimmomatic_part2/34_4H_R1.paired.fastq.gz \
 /home/jujo/bgmp/bioinfo/PS/QAA/output_trimmomatic_part2/34_4H_R2.paired.fastq.gz \
 --genomeDir /home/jujo/bgmp/bioinfo/PS/QAA/mouse_genome_part3/star_genome/ \
 --outFileNamePrefix 34_4H_mouse_aln/
