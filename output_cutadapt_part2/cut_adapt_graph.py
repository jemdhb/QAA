#!/usr/bin/env python
import argparse
import matplotlib.pyplot as plt

def get_args():
    parser = argparse.ArgumentParser(description="Demultiplex interpreter")
    parser.add_argument("-f", "--filename",
                     help="input file",
                     required=False, type=str)
    parser.add_argument("-f2", "--f2",
                     help="input file",
                     required=False, type=str)
    return parser.parse_args()
args = get_args()
fh=open(args.filename,"r")
fh2=open(args.f2,"r")

l=fh.read().strip().split("\n")
l=[int(x) for x in l]
l_prop_trimmed=((len(l)-l.count(101))/len(l))*100



m=fh2.read().strip().split("\n")
m=[int(x) for x in m]
m_prop_trimmed=((len(m)-m.count(101))/len(m))*100
print(f"21_3G_R1 proportion trimmed {l_prop_trimmed}")
print(f"21_3G_R2 proportion trimmed {m_prop_trimmed}")

#subplot so I can remove spines
fig,ax=plt.subplots()
plt.yscale('log')

#plot two histograms together
plt.hist([l, m],bins=60,label=["R1","R2"],color=["mediumslateblue","seagreen"],
         alpha=0.7)

#add relevant labels
plt.legend(loc='upper left')
plt.title("Log-based read length counts for 21_3G")
plt.xlabel("Read length")
plt.ylabel("Log based counts")

#remove spines
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
#save 
fig.savefig("21_3G_trimmed.png")
