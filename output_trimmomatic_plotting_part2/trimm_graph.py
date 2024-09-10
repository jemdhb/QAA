#!/usr/bin/env python
import argparse
import matplotlib.pyplot as plt


def get_args():
    parser = argparse.ArgumentParser(description="Demultiplex interpreter")
    #R1 file
    parser.add_argument("-f", "--filename", help="input file",required=False,
                        type=str)
    #R2 file
    parser.add_argument("-f2", "--f2",help="input file",required=False,
                        type=str)
    return parser.parse_args()

args = get_args()
#r1 file handle
fh=open(args.filename,"rt")
#r2 file handle
fh2=open(args.f2,"rt")

r1_list=fh.read().strip().split("\n")
r1_list=[int(x) for x in r1_list]
#get proportion of reads trimmed
r1_prop_trimmed=((len(r1_list)-r1_list.count(101))/len(r1_list))*100

#get name fragment for labeling
file_assign=args.filename[:args.filename.index(".")]
file_assign=file_assign[:file_assign.rfind("_")]

r2_list=fh2.read().strip().split("\n")
r2_list=[int(x) for x in r2_list]
#get proportion of reads trimmed
r2_prop_trimmed=((
    len(r2_list)-r2_list.count(101))/len(r2_list))*100

print(f"{file_assign} proportion trimmed {r1_prop_trimmed}")
print(f"{file_assign} proportion trimmed {r2_prop_trimmed}")

#subplot so I can remove spines
fig,ax=plt.subplots()
plt.yscale('log')

#plot two histograms together
plt.hist([r1_list, r2_list],bins=60,label=["R1","R2"],
         color=["mediumslateblue","seagreen"], alpha=0.7)

#add relevant labels
plt.legend(loc='upper left')
plt.title(f"Log-based read length counts for {file_assign}")
plt.xlabel("Read length")
plt.ylabel("Log based counts")

#remove spines
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
#save 
fig.savefig(f"{file_assign}_trimmed.png")
