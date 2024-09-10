#!/usr/bin/env python
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter
def get_args():
    parser = argparse.ArgumentParser(description="Demultiplex interpreter")
    #R1 file
    parser.add_argument("-f", "--filename", help="input file",required=False,
                        type=str)
    return parser.parse_args()

args = get_args()
fh=open(args.filename,"rt")
def get_counts(fh):
    mapped_counts=[int(item.split()[1].strip()) for item in fh if item.split()[0].startswith("ENS")]
    _,ax=plt.subplots()
    #counts are high set to log
    plt.yscale("log")
    plt.hist(mapped_counts,bins=50,color="seagreen",alpha=0.7)
    #remove scientific notation
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)

    ax.set(title=f"{args.filename[:args.filename.index(".")]}: Log-scaled number of genes with certain counts",ylabel="Number of genes",
           xlabel="Counts")
    sns.despine(top=True,right=True)
    out_file=args.filename[:args.filename.index(".")]+".png"
    plt.savefig(out_file)


def get_categories(fh):
    data=fh.read().split("\n")

    #for our summary categories, create a list of counts
    #tack on mapped
    cats=[item.split()[0].replace("_"," ").strip() for item in data if item.split("\t")[0].startswith("__")]+["mapped"]
    
    #anything that is not a summary stat (__) is mapped content
    counts=[int(item.split()[1].strip()) for item in data if item.split("\t")[0].startswith("__")]+\
           [sum([int(item.split()[1].strip()) for item in data if item.split("\t")[0].startswith("ENS")])]
    _,ax=plt.subplots(figsize=(15,8))

    #barh so use x-scale 
    plt.xscale("log")
    plt.barh(cats,counts,color="seagreen",alpha=0.7)
    sns.despine(top=True,right=True)
    ax.set(title=f"{args.filename[:args.filename.index(".")]}: Log-scaled number of reads per category",ylabel="Counts",
           xlabel="Category")
    out_file="cats_"+args.filename[:args.filename.index(".")]+".png"
    plt.savefig(out_file)


#get_counts(fh)
get_categories(fh)