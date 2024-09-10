#!/usr/bin/env python
import argparse
file_name="/home/jujo/bgmp/bioinfo/PS/QAA/htseq_count_part3/34H_stranded_reverse.out"
def get_args():
    parser = argparse.ArgumentParser(description="Demultiplex interpreter")
    #R1 file
    parser.add_argument("-f", "--filename", help="input file",required=False,
                        type=str)
    return parser.parse_args()

args = get_args()

#grab file name
file_name=args.filename
fh=open(file_name,"r")

#base output name on input 
output=open(file_name[:file_name.rfind(".")]+".tsv","w")
for line in fh:
    #only include mapped or summary statistic reads
    if line.startswith("ENSM") or line.startswith("__"):
        output.write(line)
#close my files
fh.close()
output.close()