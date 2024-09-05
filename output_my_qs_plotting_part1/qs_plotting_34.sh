#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --mem=16GB                        #optional: amount of memory, default is 4GB per cpu
#SBATCH --job-name=stats                  #optional: job name

#get means
/usr/bin/time -v python /home/jujo/bgmp/bioinfo/PS/Demultiplex/Assignment-the-first/part1.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/34_4H_both_S24_L008_R1_001.fastq.gz -R2 False> 34_4H_R1_means.txt
#/usr/bin/time -v python /home/jujo/bgmp/bioinfo/PS/Demultiplex/Assignment-the-first/part1.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/34_4H_both_S24_L008_R2_001.fastq.gz -R2 True > 34_4H_R2_means.txt

#graph means
/usr/bin/time -v python /home/jujo/bgmp/bioinfo/PS/Demultiplex/Assignment-the-first/part1_graphs.py -f 34_4H_R1_means.txt
#/usr/bin/time -v python /home/jujo/bgmp/bioinfo/PS/Demultiplex/Assignment-the-first/part1_graphs.py -f 34_4H_R2_means.txt

