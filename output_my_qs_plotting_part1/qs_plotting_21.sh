#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --mem=16GB                        #optional: amount of memory, default is 4GB per cpu
#SBATCH --job-name=stats                  #optional: job name

#/usr/bin/time -v python /home/jujo/bgmp/bioinfo/PS/Demultiplex/Assignment-the-first/part1.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/21_3G_both_S15_L008_R1_001.fastq.gz -R2 False> 21_3G_R1_means.txt
#/usr/bin/time -v python /home/jujo/bgmp/bioinfo/PS/Demultiplex/Assignment-the-first/part1.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/21_3G_both_S15_L008_R2_001.fastq.gz -R2 True > 21_3G_R2_means.txt

/usr/bin/time -v python /home/jujo/bgmp/bioinfo/PS/Demultiplex/Assignment-the-first/part1_graphs.py -f 21_3G_R1_means.txt
/usr/bin/time -v python /home/jujo/bgmp/bioinfo/PS/Demultiplex/Assignment-the-first/part1_graphs.py -f 21_3G_R2_means.txt