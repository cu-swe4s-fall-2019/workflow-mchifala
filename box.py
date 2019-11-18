import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def make_boxplot(tissues, genes, tissue_counts, output_file):
    width = len(genes)
    height = len(tissues)*2
    fig = plt.figure(figsize=(width,height), dpi=300)
    for t, tissue in enumerate(tissues):
        ax = fig.add_subplot(len(tissues), 1,1+t)
        ax.boxplot(tissue_counts[tissue])
        ax.set_xticklabels(genes)
        ax.set_title(tissue)
        ax.set_ylabel("Count")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches='tight')

def main(tissues, genes, output_file):
    tissue_counts = {tissue:[] for tissue in tissues}
    
    for gene in genes:

        sample_count_dict = {}
        file = open(gene + '_counts.txt')
        for line in file:
            line = line.rstrip().split()
            sample_count_dict[line[0]] = int(line[1])
        file.close()
        
        for tissue in tissues:
            counts = []
            file = open(tissue + '_samples.txt')
            for line in file:
                sample = line.rstrip()
                if sample in sample_count_dict:
                    counts.append(sample_count_dict[sample])
            file.close()

            tissue_counts[tissue].append(counts)
    
    make_boxplot(tissues, genes, tissue_counts, output_file)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot gene expression")

    parser.add_argument('--tissues',
                        type=str,
                        nargs="+",
                        help="Tissue groups of interest")

    parser.add_argument('--genes',
                        type=str,
                        nargs="+",
                        help="Genes of interest")

    parser.add_argument("--output_file",
                        type=str,
                        help="Output file for boxplot")

    args = parser.parse_args()

    main(args.tissues, args.genes, args.output_file)