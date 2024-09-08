#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --mem=30GB                        #optional: amount of memory, default is 4GB per cpu
#SBATCH --job-name=ht_34                  #optional: job name
conda activate QAA
/usr/bin/time -v htseq-count --stranded=yes ../STAR_mouse_aln_part3/34_4H_mouse_aln/Aligned.out.sam ../mouse_genome_part3/Mus_musculus.GRCm39.112.gtf