import gzip
import argparse


def main(file, gene_name, output_file):
    """
    This main function creates a .txt file of sample ID's and counts
    for a given gene of interest.

    Parameter:
    - file(str): The gene count file
    - gene_name(str): The gene of interest
    - output_file(str): The output file of sample ID's and counts

    """
    out = open(output_file, 'w')

    version = None
    dim = None
    header = None
    file = gzip.open(file, 'rt')
    for line in file:
        line = line.strip().split("\t")

        if version is None:
            version = line
            continue

        if dim is None:
            dim = line
            continue

        if header is None:
            header = line
            print(len(header))
            continue

        if line[1] == gene_name:
            for i in range(2, len(header)):
                out.write(header[i] + ' ' + line[i] + '\n')

    file.close()
    out.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get gene counts")

    parser.add_argument('file',
                        type=str,
                        help="Path to gene count file")

    parser.add_argument('gene_name',
                        type=str,
                        help="Name of the gene")

    parser.add_argument("output_file",
                        type=str,
                        help="File with sample ids and counts for gene")

    args = parser.parse_args()

    main(args.file, args.gene_name, args.output_file)
